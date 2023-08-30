import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget

class TaskWidget(QWidget):
    def __init__(self, task_text, parent=None):
        super().__init__(parent)
        
        self.task_text = task_text
        
        self.layout = QHBoxLayout()
        self.label = QLabel(task_text)
        self.done_button = QPushButton("Done!")
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.done_button)
        
        self.done_button.clicked.connect(self.mark_done)
        
        self.setLayout(self.layout)
        
    def mark_done(self):
        self.label.setStyleSheet("color: gray; text-decoration: line-through;")
        self.done_button.setEnabled(False)

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.setWindowTitle("To-Do List")
        self.center_window(600, 400)

        self.layout = QVBoxLayout()

        self.task_entry = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.clear_button = QPushButton("Clear Tasks")
        self.show_done_button = QPushButton("Show Done Tasks")

        self.add_button.clicked.connect(self.add_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.show_done_button.clicked.connect(self.show_done_tasks)

        self.layout.addWidget(self.task_entry)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.show_done_button)

        self.task_widgets_layout = QVBoxLayout()
        self.layout.addLayout(self.task_widgets_layout)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

    def add_task(self):
        task_text = self.task_entry.text()
        if task_text:
            task_widget = TaskWidget(task_text)
            self.tasks.append(task_widget)
            self.task_widgets_layout.addWidget(task_widget)
            self.task_entry.clear()

    def clear_tasks(self):
        for task_widget in self.tasks:
            task_widget.deleteLater()
        self.tasks = []

    def center_window(self, width, height):
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - width) // 2
        y = (screen_geometry.height() - height) // 2
        self.setGeometry(x, y, width, height)

    def show_done_tasks(self):
        for task_widget in self.tasks:
            if "done" in task_widget.label.styleSheet():
                print(f"Done task: {task_widget.task_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
