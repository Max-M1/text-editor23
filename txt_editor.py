import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTextEdit
from PyQt5.QtGui import QKeySequence


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.create_menu()

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Текстовий редактор")
        self.show()

    def create_menu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("Файл")
        editMenu = menuBar.addMenu("Редагувати")

        openAction = QAction("Відкрити", self)
        openAction.triggered.connect(self.open_file)
        fileMenu.addAction(openAction)

        saveAction = QAction("Зберегти", self)
        saveAction.triggered.connect(self.save_file)
        fileMenu.addAction(saveAction)

        exitAction = QAction("Вийти", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        cutAction = QAction("Вирізати", self)
        cutAction.triggered.connect(self.text_edit.cut)
        cutAction.setShortcut(QKeySequence.Copy)
        editMenu.addAction(cutAction)

        copyAction = QAction("Копіювати", self)
        copyAction.triggered.connect(self.text_edit.copy)
        copyAction.setShortcut(QKeySequence.Copy)
        editMenu.addAction(copyAction)

        pasteAction = QAction("Вставити", self)
        pasteAction.triggered.connect(self.text_edit.paste)
        pasteAction.setShortcut(QKeySequence.Paste)
        editMenu.addAction(pasteAction)

        undoAction = QAction("Скасувати", self)
        undoAction.triggered.connect(self.text_edit.undo)
        undoAction.setShortcut(QKeySequence.Undo)
        editMenu.addAction(undoAction)

        redoAction = QAction("Повторити", self)
        redoAction.triggered.connect(self.text_edit.redo)
        redoAction.setShortcut(QKeySequence.Redo)
        editMenu.addAction(redoAction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
