from http.client import SWITCHING_PROTOCOLS
import win32gui

handles = []

def a(hwnd, wh):
  print(hwnd, win32gui.GetDlgCtrlID(hwnd))
  print(win32gui.GetClassName(hwnd))
  if win32gui.GetClassName(hwnd)=="WindowsForms10.EDIT.app.0.141b42a_r6_ad1":
    handles.append([hwnd, win32gui.GetDlgItemText(wh, hwnd)])

wh = win32gui.FindWindow(None, "test")
print(wh)
win32gui.EnumChildWindows(wh, a, wh)

print(handles)
