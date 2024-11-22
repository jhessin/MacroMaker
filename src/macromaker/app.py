"""
A utility for managing keybinds and macros.
"""

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
        self.SetSize(50,50)
        self.SetTransparent(220)
        self.Show(True)

    def OnKeyDown(self, event):
        """quit if user press q or Esc"""
        if event.GetKeyCode() == 27 or event.GetKeyCode() == ord("Q"):  # 27 is Esc
            self.Close(force=True)
        elif event.GetKeyCode() == ord('H'):
            self.Show()
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


class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st: wx.StaticText = wx.StaticText(pnl, label="Hello World!")
        font: wx.Font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer: wx.BoxSizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(
            -1,
            "&Hello...\tCtrl-H",
            "Help string shown in status bar for this menu item",
        )
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the twe menus to it. the '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keybeard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnHello(self, event: wx.Event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox(
            "This is a wxPython Hello World sample",
            "About Hello World!!",
            wx.OK | wx.ICON_INFORMATION,
        )


def main():
    # Create an application object.
    app = wx.App()

    # Then a frame.
    # frm = wx.Frame(None, title="Hello World")
    # frm = HelloFrame(None, title="Hello World")
    frm = FancyFrame()

    # Show it.
    frm.Show()

    # Start the event loop.
    app.MainLoop()
