"""
A utility for managing keybinds and macros.
"""

import keyboard
import wx
from macromaker.Floating_Window import Floating_Window



def main():
    # Create an application object.
    app = wx.App()

    # Then a frame.
    frm = Floating_Window()

    # Show it.
    def show_frame():
        frm.Show()
        # frm.SetFocus()
        frm.SetFocusFromKbd()

    # keyboard.add_hotkey("ctrl + t", show_frame)
    # keyboard.add_hotkey(":", show_frame)
    frm.Show()

    # Start the event loop.
    app.MainLoop()
