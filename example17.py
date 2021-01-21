import sys
import time
import qdarkstyle

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread, QTimer
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QPushButton, QWidget


class Command:
    def __init__(self, **kwargs):
        self.cmd = kwargs.get("cmd", None)
        self.args = kwargs.get("args")


class CommandSignals(QObject):
    command = pyqtSignal(Command)


class WorkToDo(QObject):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.signals = CommandSignals()
        self.timer = QTimer(self, timeout=self.run, interval=1000)

    @pyqtSlot()
    def start(self):
        self.timer.start()

    @pyqtSlot()
    def stop(self):
        self.timer.stop()

    @pyqtSlot(Command)
    def process_command(self, command):
        """
        @brief       process update from gui thread
        @param       self     self
        @param       command  command
        @return      none
        """
        print(f"Update from GUI: {command.__dict__}")
        if command.cmd == "add_to_counter":
            self.counter = self.counter + command.args.get("addition", 0)

    @pyqtSlot()
    def run(self):
        print(self.thread(), self.timer.thread())
        cmd = Command(cmd="update_text", args={"text": f"Hello update {self.counter}"})
        print(f"Update from worker: {cmd.__dict__}")
        self.signals.command.emit(cmd)
        self.counter += 1


class Gui(QWidget):
    def __init__(self):
        super().__init__()
        """ make gui elements """
        layout = QFormLayout()
        self.text_line = QLineEdit()
        self.add_button = QPushButton("Add 10 To Counter")
        layout.addRow(self.text_line)
        layout.addRow(self.add_button)

        self.add_button.clicked.connect(self.issue_button_update)
        self.signals = CommandSignals()
        self.MakeThreadWorker()

        """ finalize gui """
        self.setLayout(layout)
        self.setWindowTitle("Sync Thread Command/Response test")
        self.show()

    def MakeThreadWorker(self):
        self.worker_thread = QThread()
        self.worker = WorkToDo()

        """ incoming gui update command, works """
        self.worker.signals.command.connect(self.process_command)
        """ outgoing update to worker thread, does not work """
        self.signals.command.connect(self.worker.process_command)

        """ signal to start the thread function, works """
        self.worker_thread.started.connect(self.worker.start)

        self.worker_thread.start()
        self.worker.moveToThread(self.worker_thread)

    @pyqtSlot(Command)
    def process_command(self, command):
        """
        @brief       process update from work thread
        @param       self     self
        @param       command  command object
        @return      none
        """
        if command.cmd == "update_text":
            text_update = command.args.get("text", "")
            self.text_line.setText(text_update)

    def issue_button_update(self):
        cmd = Command(cmd="add_to_counter", args={"addition": 10})
        print("Button Clicked!")
        self.signals.command.emit(cmd)


if __name__ == "__main__":
    APPLICATION = QApplication([])
    # APPLICATION.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    gui = Gui()
    sys.exit(APPLICATION.exec_())