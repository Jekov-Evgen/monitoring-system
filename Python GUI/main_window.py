from PySide6 import QtWidgets

class MainWindow:
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication()
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Мониторинг системы")
        
        box_h_cpu = QtWidgets.QHBoxLayout()
        box_h_memory = QtWidgets.QHBoxLayout()
        box_h_video_card = QtWidgets.QHBoxLayout()
        box_v = QtWidgets.QVBoxLayout()
        
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
        
        box_v.addLayout(box_h_cpu)
        box_v.addLayout(box_h_memory)
        box_v.addLayout(box_h_video_card)
        
        self.window.setLayout(box_v)
        
    def run(self):
        self.window.show()
        self.app.exec()