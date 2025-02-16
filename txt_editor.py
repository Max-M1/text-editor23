import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTextEdit
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QFile, QTextStream


class TextEditorModel:
    def __init__(self):
        self.text = ""

    def open_file(self, file_name):
        file = QFile(file_name)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.text = stream.readAll()
            file.close()

    def save_file(self, file_name):
        file = QFile(file_name)
        if file.open(QFile.WriteOnly | QFile.Text):
            stream = QTextStream(file)
            stream << self.text
            file.close()

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = TextEditorModel()
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

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Вибрати файл", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            self.model.open_file(file_name)
            self.text_edit.setText(self.model.get_text())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Зберегти файл", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            self.model.set_text(self.text_edit.toPlainText())
            self.model.save_file(file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
