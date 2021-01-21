import sys
from PyQt5 import QtCore, QtWidgets, uic
import threading
import pynput.keyboard as keyboard
from PyQt5 import QtCore

class KeyMonitor(QtCore.QObject):
    wordPressed = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.word = ""

        self.listener = threading.Thread(target=self._task, daemon=True)

    def _task(self):
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "space":
                    self.wordPressed.emit(self.word)
                    self.word = ""
                elif len(event.name) == 1:
                    self.word += event.name

    def start_monitoring(self):
        self.listener.start()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("gui.ui", self)
        self.show()

    @QtCore.pyqtSlot(str)
    def on_word_pressed(self, word):
        try:
            x = int(word)
        except ValueError:
            print("You must enter a whole number")
        else:
            self.label.setText("{}".format(x + 2))
            self.label_2.setText("Changed {}".format(x - 2))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    monitor = KeyMonitor()
    monitor.wordPressed.connect(window.on_word_pressed)
    monitor.start_monitoring()
    sys.exit(app.exec_())