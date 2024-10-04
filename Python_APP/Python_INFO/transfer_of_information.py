import psutil

class CPU:
    def __init__(self) -> None:
        pass
    
    def info_CPU(self) -> float:
        info_cpu = psutil.cpu_percent(interval=2)
        return info_cpu