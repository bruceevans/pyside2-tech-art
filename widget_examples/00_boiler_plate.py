"""Use this module to generate a basic window and run the example widgets
"""

""" Lecture 0. VS Code, Python, and PySide2 setup

1. Show the download page for vs code
2. Show installing python
3. Pip install PySide2
4. Write the boilerplate main window and show vs code setup
    - Python extension
    - Docstring extension
    - Bear Theme

"""

import sys

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
    """Run the app and window instance
    """
    # NOTE (bevans)
    # Passing sys.argv allows for passing command line arguments to
    # the Qt application
    app = QtWidgets.QApplication(sys.argv)
    explorer = WidgetExplorer()
    explorer.show()

    # NOTE (bevans)
    # This will just give the status code of the app
    # back to the parent process, helpful if other parts of the system need
    # detech the program's status
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
