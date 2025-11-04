import pyautogui
import time

# 等待几秒，方便将鼠标移动到目标位置
time.sleep(5) 
# 获取当前鼠标位置的坐标
print(pyautogui.position()) 