import socket
import random
import threading
import json

# глобальные переменные: количество попыток, максимальное число, перенос строки
MAX_ATTEMPTS = 10
MAX_NUMBER = 1000
NEWLINE = '\r\n'


class RunGame(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        secret_number = random.randint(0, MAX_NUMBER)
        attempt_cnt = 0
        execute = True

        # приветствие
        welcome_data = {
            "feedback": f"Welcome! Guess 0-{MAX_NUMBER}.",
            "guess": "---",
            "attempts": MAX_ATTEMPTS,
            "is_game_over": False
        }
        self.conn.sendall(json.dumps(welcome_data).encode('utf-8'))

        while execute:
            try:
                data = self.conn.recv(1024)
                if not data: break
                # сообщение с числом от игрока
                msg = data.decode().strip()
                if not msg: continue

                try:
                    guess = int(msg)
                    attempt_cnt += 1
                    # обработка введенного игроком числа
                    if guess == secret_number:
                        feedback = f'Great job! You guessed the number.'
                        execute = False
                    elif attempt_cnt >= MAX_ATTEMPTS:
                        feedback = f'Sorry! You have used all your attempt(s) and still haven\'t guessed the number correctly.' \
                         f'{NEWLINE}The number was {secret_number}. Better luck next time!'
                        execute = False
                    elif guess < secret_number:
                        feedback = f"Larger number, please!"
                    else:
                        feedback = f"Smaller number, please!"
                    # формирование ответа
                    response_data = {
                        "feedback": feedback,  # больше/меньше
                        "guess": guess,  # число игрока
                        "attempts": MAX_ATTEMPTS - attempt_cnt, # количество попыток
                        "is_game_over": not execute
                    }
                    json_string = json.dumps(response_data)
                    self.conn.sendall(json_string.encode('utf-8'))
                except ValueError:
                    err_data = {"feedback": "Error: Enter a number!", "guess": "???",
                                "attempts": MAX_ATTEMPTS - attempt_cnt, "is_game_over": False}
                    self.conn.sendall(json.dumps(err_data).encode('utf-8'))
            except Exception as e:
                break
        # закрытие подключения
        self.conn.close()
        print(f"[SERVER] Player {self.addr} disconnected")


# настройка сервера
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen()
print("SERVER IS RUNNING")

# запуск
while True:
    client_conn, client_addr = server_socket.accept()
    RunGame(client_conn, client_addr).start()
