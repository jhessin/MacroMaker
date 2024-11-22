#!/usr/bin/env python3
# import win32com.client
# import win32con, win32api
# import ctypes
import mouse
import keyboard
# import pyautogui

# Resources to look at:
# https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
# https://stackoverflow.com/questions/2791839/which-is-the-easiest-way-to-simulate-keyboard-and-mouse-on-python
# https://www.geeksforgeeks.org/how-to-create-a-hotkey-in-python/

# API docs for mouse
# https://github.com/boppreh/mouse#api
# API docs for keyboard
# https://github.com/boppreh/keyboard#api


# API docs for ctypes
# https://docs.python.org/3/library/ctypes.html

# This is a simple test to ensure key sending works in python using pywin32
# https://github.com/mhammond/pywin32

# To use this we need to install using

"""
python -m pip install --upgrade pywin32
python Scripts/pywin32_postinstall.py -install
"""

def openTaskManager():
  # shell = win32com.client.Dispatch("Wscript.Shell")
  # shell.SendKeys("^+{ESCAPE}")
  keyboard.send("ctrl + shift + escape")
  
def click(x, y):
  # Using pywin32
  # win32api.SetCursorPos((x, y))
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
  
  # Using ctypes (no package download)
  # ctypes.windll.user32.SetCursorPos(x, y)
  # ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
  # ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

  # Using mouse (better api documentation)
  old_x, old_y = mouse.get_position()
  mouse.move(x, y)
  mouse.click()
  mouse.move(old_x, old_y)
  
def poll_mouse():
  print(f"mouse position: {mouse.get_position()}")


if __name__ == "__main__":
  # pyautogui.click(20, 20)
  # click(1807, 17)
  # openTaskManager()
  keyboard.add_hotkey('ctrl + 0', openTaskManager)
  keyboard.wait('esc')
  # while True:
  #   poll_mouse()
