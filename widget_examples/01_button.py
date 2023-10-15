"""Push button tests
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html
"""

import sys  # TODO know exactly why you need this

from PySide2 import QtWidgets


# TODO button menu example


class WidgetExplorer(QtWidgets.QMainWindow):
    """Create the main window to test our widgets
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.counter = 0

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        """Create the UI elements
        """
        main_layout = QtWidgets.QVBoxLayout()

        # NOTE (Bevans)
        # Setting the parent allows the widget to return the parent
        # via the widget.parent() method
        self.button_one = QtWidgets.QPushButton("Button 1")
        # self.button_one.setAutoDefault(True)
        main_layout.addWidget(self.button_one)

        # NOTE (bevans)
        # The ampersand in front of a character will make that char a shortcut
        # In this example, Alt B
        # to display an actual ampersand, use ‘&&’
        self.button_two = QtWidgets.QPushButton(f"&Button 2 - Pressed {self.counter} times")
        self.button_two.setToolTip("Tooltip for button 2")
        main_layout.addWidget(self.button_two)

        self.button_toggle = QtWidgets.QPushButton("Toggle Button")
        self.button_toggle.setCheckable(True)
        main_layout.addWidget(self.button_toggle)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)

        # Format the window
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Base Widget Explorer")
        # self.setMinimumSize(500, 500)

    def _connect_signals(self):
        """Connect all the UI signals
        """
        self.button_two.clicked.connect(self._on_button_two_clicked)

    def _on_button_two_clicked(self):
        self.counter += 1
        self.button_two.setText(f"&Button 2 - Pressed {self.counter} times")


def run():
    """Run the thing!
    """
    app = QtWidgets.QApplication(sys.argv)
    explorer = WidgetExplorer()
    explorer.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
