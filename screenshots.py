import time 
import pyautogui  #pytautogui module allows python to control the mouse and keyboard and take screenshots

def screenshot():
    time.sleep(3) #gives you 3 seconds to prepare
    img = pyautogui.screenshot() # its used to take screenshot of the entire screen and return a pillow image object
    img.save("test.png") # this saves the screenshot to a file name test.png 
    img.show() # this open the saved image using the default system viewer

screenshot()