from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):
    """
    controlls the view and commnicates with PYQT
    """

    def __init__(self, c: Controller):
        super().__init__()
        self.c = c
        uic.loadUi("mainwindow.ui", self)
        self.check_btn.clicked.connect(c.check)
        self.reset_btn.clicked.connect(c.reset)
        self.set_statusbar("Language Detector by Moritz Steinbacher. Ready to read!", 6000)

    def reset(self):
        """
        resets Ui
        :param self
        :return None
        """
        self.output.setText("")
        self.input.setText("")
        self.set_statusbar("Reset complete! Ready to read!", 3000)

    def get_input(self) -> str:
        """
        gets input text field
        :param self
        :return Text input from UI
        """
        return self.input.toPlainText()

    def set_output(self, lang_long: str, lang_short: str, is_reliable: bool, probability: float):
        """
        sets output text field
        :param self, lang_long, lang_short, is_reliable, probability
        :return None
        """
        self.output.setHtml(f"reliable: <b>{is_reliable}</b><br>language: <b>{lang_long} ({lang_short})</b><br"
                            f">probability: <b>{probability:.2f}%</b>")

    def set_error(self, message: str):
        """
        called on Error
        :param message
        :return None
        """
        self.set_statusbar(message, 3000)

    def set_statusbar(self, text: str, durration_ms: int):
        """
        sets statusbar value
        :param self, text, durration_ms
        :return None
        """
        self.statusbar.showMessage(text, durration_ms)
