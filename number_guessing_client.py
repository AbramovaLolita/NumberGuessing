import sys
import socket
import json
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal, QWaitCondition, QMutex
from gui_app import Ui_MainWindow

class ClientThread(QThread):
    # введенные числа и ответы сервера
    log_signal = Signal(str)
    # подсказки (больше/меньше)
    feedback_signal = Signal(str)
    # отображение количества попыток
    attempts_signal = Signal(int)


    def __init__(self):
        super().__init__()
        self.user_input = ""
        self.input_ready = QWaitCondition()
        self.mutex = QMutex()

    def run(self):
        s = socket.socket()
        try:
            s.connect(('127.0.0.1', 12345))
            self.log_signal.emit("System: Connected to server.")

            while True:
                # ответ сервера
                data = s.recv(1024)
                if not data: break
                msg = json.loads(data.decode().strip())
                # распаковка ответа сервера
                try:
                    msg = json.loads(data.decode().strip())
                    # подсказка
                    feedback = msg.get("feedback", "")
                    self.feedback_signal.emit(feedback)

                    # счетчик попыток
                    if "attempts" in msg:
                        self.attempts_signal.emit(msg["attempts"])

                    # история ввода чисел
                    if "guess" in msg and msg["guess"] != "---":
                        history_msg = f" {msg['guess']}"
                        self.log_signal.emit(history_msg)

                # обработка ошибок
                except json.JSONDecodeError:
                    self.log_signal.emit(f"System: {data.decode().strip()}")

                if 'Great job!' in msg or 'Sorry!' in msg:
                    break

                # ожидание ввода игрока
                self.mutex.lock()
                self.input_ready.wait(self.mutex)
                val = self.user_input
                self.mutex.unlock()
                s.send(f"{val}\r\n".encode())

            # закрытие подключения
            s.close()
            self.log_signal.emit("System: Game Over.")
        except Exception as e:
            self.log_signal.emit(f"System Error: {e}")

    def send_to_server(self, text):
        self.mutex.lock()
        self.user_input = text
        self.input_ready.wakeAll()
        self.mutex.unlock()


class ClientApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.worker = ClientThread()
        # запись сигналов в виджеты
        self.worker.log_signal.connect(self.add_to_history)
        self.worker.feedback_signal.connect(self.ui.lbl_feedback.setText)
        self.worker.attempts_signal.connect(self.ui.attempts.display)

        self.ui.pushButton_2.clicked.connect(self.on_click)
        self.worker.start()


    def add_to_history(self, text):
        self.ui.list_history.addItem(text)
        self.ui.list_history.scrollToBottom()

    def on_click(self):
        val = self.ui.input_number_2.text()
        self.worker.send_to_server(val)
        self.ui.input_number_2.clear()

app = QApplication(sys.argv)
window = ClientApp()
window.show()
sys.exit(app.exec())
