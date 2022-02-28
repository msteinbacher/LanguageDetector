import sys
from PyQt6.QtWidgets import QApplication
import model
import view


class Controller:
    """
    controls the programm
    """

    def __init__(self):
        self.model = model.RESTClient()
        self.view = view.View(self)

    def check(self):
        """
        checks the given input
        :param self
        :return: None
        """
        try:
            self.model.check_language(self.view.get_input())
            self.view.set_output(self.model.lang_long, self.model.lang_short, self.model.is_reliable,
                                 self.model.probability)
        except model.InternetConnectionError:
            self.view.set_error("There is no network connection available")
        except model.InvalidValueError:
            self.view.set_error("The given input is invalid")

    def reset(self):
        """
        resets the software
        :param self
        :return: None
        """
        self.view.reset()


if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
