"""Use this module to generate a basic window and run the example widgets
"""

import sys  # TODO know exactly why you need this

from PySide2 import QtWidgets


class WidgetExplorer(QtWidgets.QMainWindow):
    """Create the main window to test our widgets
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        """Create the UI elements
        """
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Base Widget Explorer")
        self.setMinimumSize(500, 500)

    def _connect_signals(self):
        """Connect all the UI signals
        """
        pass


def run():
    """Run the thing!
    """
    app = QtWidgets.QApplication(sys.argv)
    explorer = WidgetExplorer()
    explorer.show()
    sys.exit(app.exec_())  # TODO know why you need to do this


if __name__ == "__main__":
    run()
