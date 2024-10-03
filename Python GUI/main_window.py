from PySide6 import QtWidgets

class MainWindow:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Мониторинг системы")
        
        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        
        cpu = QtWidgets.QLabel("Процессор")
        info_cpu = QtWidgets.QLabel("0%")
        
        memory = QtWidgets.QLabel("Память")
        info_memory = QtWidgets.QLabel("0%")
        
        video_card = QtWidgets.QLabel("Видеокарта")
        info_video_card = QtWidgets.QLabel("0%")
        
    def run(self):
        self.window.show()
        self.app.exec()