import psutil
import GPUtil

class CPU:
    def __init__(self) -> None:
        pass
    
    def info_CPU(self) -> float:
        info_cpu = psutil.cpu_percent(interval=2)
        return info_cpu
    
class Memory:
    def __init__(self) -> None:
        pass
    
    def info_Memory(self):
        info_memory = psutil.virtual_memory()
        return info_memory[2]
    
    
class GPU:
    def __init__(self) -> None:
        pass
    
    def info_GPU(self):
        info_GPU = GPUtil.getGPUs()
        self.Error = "GPU не обнаружен"
        success = info_GPU        
        info_list = []
        
        if not info_GPU:
            return self.Error
        else:           
            for i, gpu in enumerate(info_GPU):
                info_list.append(f"\nGPU {i + 1} Information:")
                info_list.append(f"ID: {gpu.id}")
                info_list.append(f"Name: {gpu.name}")
                info_list.append(f"Driver: {gpu.driver}")
                info_list.append(f"GPU Memory Total: {gpu.memoryTotal} MB")
                info_list.append(f"GPU Memory Free: {gpu.memoryFree} MB")
                info_list.append(f"GPU Memory Used: {gpu.memoryUsed} MB")
                info_list.append(f"{gpu.load * 100}%")
                info_list.append(f"GPU Temperature: {gpu.temperature}°C")
                
            return info_list[7]