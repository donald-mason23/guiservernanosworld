import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog, QLabel, QLineEdit, \
    QCheckBox, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        console_label = QLabel("Console:")
        self.console = QLineEdit()

        start_button = QPushButton("Start")
        stop_button = QPushButton("Stop")
        restart_button = QPushButton("Restart")
        update_button = QPushButton("Update")
        settings_button = QPushButton("Settings")
        package_button = QPushButton("Package")
        assets_button = QPushButton("Assets")
        exit_button = QPushButton("Exit")

        start_button.clicked.connect(self.on_start)
        stop_button.clicked.connect(self.on_stop)
        restart_button.clicked.connect(self.on_restart)
        update_button.clicked.connect(self.on_update)
        settings_button.clicked.connect(self.on_settings)
        package_button.clicked.connect(self.on_package)
        assets_button.clicked.connect(self.on_assets)
        exit_button.clicked.connect(self.on_exit)

        button_layout = QVBoxLayout()
        button_layout.addWidget(start_button)
        button_layout.addWidget(stop_button)
        button_layout.addWidget(restart_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(settings_button)
        button_layout.addWidget(package_button)
        button_layout.addWidget(assets_button)
        button_layout.addWidget(exit_button)

        central_widget = QWidget()
        central_widget.setLayout(button_layout)

        self.setCentralWidget(central_widget)

    def on_start(self):
        print("Start button clicked")

    def on_stop(self):
        print("Stop button clicked")

    def on_restart(self):
        print("Restart button clicked")

    def on_update(self):
        print("Update button clicked")

    def on_settings(self):
        settings_dialog = SettingsDialog(self)
        settings_dialog.exec_()

    def on_package(self):
        print("Package button clicked")

    def on_assets(self):
        print("Assets button clicked")

    def on_exit(self):
        sys.exit()


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(400, 500)

        layout = QVBoxLayout()

        # Add your input fields, checkboxes, and dropdowns here
        # Example:
        self.name_input = QLineEdit()
        self.description_input = QLineEdit()
        self.ip_input = QLineEdit()
        # ...

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.description_input)
        layout.addWidget(QLabel("IP:"))
        layout.addWidget(self.ip_input)
        # ...

        # Add more widgets (checkboxes, dropdowns, etc.) based on your requirements.

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
