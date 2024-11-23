"""
A utility for managing keybinds and macros.
"""

import keyboard
import wx


class FancyFrame(wx.Frame):
    """
    This will be a simple hitbox. Using self.GetPosition() I can find the top left corder of the box. It can be positioned anywhere on screen and it can be hidden.
    """

    _dragPos: wx.Point | None = None

    def __init__(self):
        style = (
            wx.CLIP_CHILDREN
            | wx.STAY_ON_TOP
            | wx.FRAME_NO_TASKBAR
            | wx.NO_BORDER
            | wx.FRAME_SHAPED
        )
        wx.Frame.__init__(self, None, title="Fancy", style=style)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyDown)
        self.Bind(wx.EVT_MOTION, self.OnMouse)
        self.Bind(wx.EVT_MOUSE_CAPTURE_LOST, self.CaptureLost)
        self.SetSize(50, 50)
        self.SetTransparent(220)
        # self.Show(True)

    def CaptureLost(self):
        pass

    def OnKeyDown(self, event):
        """quit if user press q or Esc"""
        if event.GetKeyCode() == 27 or event.GetKeyCode() == ord("Q"):  # 27 is Esc
            self.Close(force=True)
        elif event.GetKeyCode() == ord("H"):
            self.Hide()
        else:
            event.Skip()

    def OnMouse(self, event: wx.MouseEvent):
        """implement dragging"""
        if not event.Dragging():
            if self.HasCapture():
                self.ReleaseMouse()
            self._dragPos = None
            return
        if not self.HasCapture():
            self.CaptureMouse()
        if not self._dragPos:
            self._dragPos = event.GetPosition()
        else:
            pos = event.GetPosition()
            displacement = self._dragPos - pos
            self.SetPosition(self.GetPosition() - displacement)


def main():
    # Create an application object.
    app = wx.App()

    # Then a frame.
    frm = FancyFrame()

    # Show it.
    def show_frame():
        frm.Show()
        # frm.SetFocus()
        frm.SetFocusFromKbd()

    keyboard.add_hotkey("ctrl + t", show_frame)
    # keyboard.add_hotkey(":", show_frame)
    # frm.Show()

    # Start the event loop.
    app.MainLoop()
