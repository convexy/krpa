from time import time
import win32con, win32gui

class RPA:
  def __init__(self, title, timeout=10):
    self._title = title
    self._timeout = timeout

    self._hwnd = 0
    def get_hwnd(hwnd, title):
      if win32gui.GetWindowText(hwnd) == title:
        self._hwnd = hwnd
    win32gui.EnumWindows(get_hwnd, title)
    if self._hwnd == 0:
      raise RPAException("Window with title '" + self._title + "' not found.")

  def activate(self):
      start = time()
      while True:
        if win32gui.IsIconic(self._hwnd):
          win32gui.ShowWindow(self._hwnd, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(self._hwnd)
        win32gui.ShowWindow(self._hwnd, win32con.SW_SHOW)
        # win32gui.SetWindowPos(self._hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        # win32gui.SetWindowPos(self._hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE | win32con.SWP_SHOWWINDOW)
        if win32gui.GetForegroundWindow() == self._hwnd:
          break
        if time() - start > self._timeout:
          raise RPAException("Window with title '" + self._title + "' not activated.")

    
class RPAException(Exception):
  pass

if __name__ == "__main__":
  rpa = RPA("test")
  rpa.activate()
  rpa.a()