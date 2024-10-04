from PySide6 import QtWidgets
from PySide6 import QtCore
from Python_GUI.style_app import  STYLE_WINDOW, STYLE_NAME, STYLE_INFO, STYLE_GREETINGS
from Python_INFO.transfer_of_information import CPU
from time import sleep

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
        self.info_cpu = QtWidgets.QLabel("0%")
        
        memory = QtWidgets.QLabel("Память: ")
        info_memory = QtWidgets.QLabel("0%")
        
        video_card = QtWidgets.QLabel("Видеокарта: ")
        info_video_card = QtWidgets.QLabel("0")
        
        box_h_cpu.addWidget(cpu)
        box_h_cpu.addWidget(self.info_cpu)
        
        box_h_memory.addWidget(memory)
        box_h_memory.addWidget(info_memory)
        
        box_h_video_card.addWidget(video_card)
        box_h_video_card.addWidget(info_video_card)
        
        box_h_cpu.setSpacing(15)
        box_h_memory.setSpacing(15)
        box_h_video_card.setSpacing(15)
        box_v.setSpacing(20)
        
        box_v.setContentsMargins(20, 20, 20, 20)
        
        box_v.addWidget(greetings)
        box_v.addLayout(box_h_cpu)
        box_v.addLayout(box_h_memory)
        box_v.addLayout(box_h_video_card)
        
        self.window.setStyleSheet(STYLE_WINDOW)
        
        greetings.setStyleSheet(STYLE_GREETINGS)
        
        cpu.setStyleSheet(STYLE_NAME)
        memory.setStyleSheet(STYLE_NAME)
        video_card.setStyleSheet(STYLE_NAME)
        
        self.info_cpu.setStyleSheet(STYLE_INFO)
        info_memory.setStyleSheet(STYLE_INFO)
        info_video_card.setStyleSheet(STYLE_INFO)
        
        self.set_info()
        
        self.window.setLayout(box_v)
        
    def run(self):
        self.window.show()
        self.app.exec()
        
    def set_info(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_info)
        self.timer.start(2000)
    
    def update_info(self):
        info_CPU = CPU()
        self.info_cpu.setText(f"{info_CPU.info_CPU()}%")