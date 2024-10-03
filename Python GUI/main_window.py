from PySide6 import QtWidgets
from PySide6 import QtCore
from style_app import  STYLE_WINDOW, STYLE_NAME, STYLE_INFO, STYLE_GREETINGS

class MainWindow:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Мониторинг системы")
        
        box_h_cpu = QtWidgets.QHBoxLayout()
        box_h_memory = QtWidgets.QHBoxLayout()
        box_h_video_card = QtWidgets.QHBoxLayout()
        box_v = QtWidgets.QVBoxLayout()
        
        greetings = QtWidgets.QLabel("monitoring system ALGORT")
        greetings.setAlignment(QtCore.Qt.AlignCenter)
        
        cpu = QtWidgets.QLabel("Процессор: ")
        info_cpu = QtWidgets.QLabel("0%")
        
        memory = QtWidgets.QLabel("Память: ")
        info_memory = QtWidgets.QLabel("0%")
        
        video_card = QtWidgets.QLabel("Видеокарта: ")
        info_video_card = QtWidgets.QLabel("0%")
        
        box_h_cpu.addWidget(cpu)
        box_h_cpu.addWidget(info_cpu)
        
        box_h_memory.addWidget(memory)
        box_h_memory.addWidget(info_memory)
        
        box_h_video_card.addWidget(video_card)
        box_h_video_card.addWidget(info_video_card)
        
        box_v.addWidget(greetings)
        box_v.addLayout(box_h_cpu)
        box_v.addLayout(box_h_memory)
        box_v.addLayout(box_h_video_card)
        
        self.window.setStyleSheet(STYLE_WINDOW)
        
        greetings.setStyleSheet(STYLE_GREETINGS)
        
        cpu.setStyleSheet(STYLE_NAME)
        memory.setStyleSheet(STYLE_NAME)
        video_card.setStyleSheet(STYLE_NAME)
        
        info_cpu.setStyleSheet(STYLE_INFO)
        info_memory.setStyleSheet(STYLE_INFO)
        info_video_card.setStyleSheet(STYLE_INFO)
        
        self.window.setLayout(box_v)
        
    def run(self):
        self.window.show()
        self.app.exec()