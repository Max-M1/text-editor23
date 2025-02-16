import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Текстовий редактор")
        self.setGeometry(100, 100, 800, 600)

        # Текстове поле
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
