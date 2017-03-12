# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:36:33 2017

@author: Uwe Ziegenhagen

Source: http://stackoverflow.com/questions/4485610/python-message-box-without-huge-library-dependancy

"""

# using ctypes
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Hello World', 'This is the window title', 0)

# using win32ui
import win32ui
win32ui.MessageBox('This is the message', 'Window Title')

# using win32con
import win32con

result = win32ui.MessageBox('The Message', 'The Title', win32con.MB_YESNOCANCEL)

if result == win32con.IDYES:
    win32ui.MessageBox('You pressed "Yes"')
elif result == win32con.IDNO:
    win32ui.MessageBox('You pressed "No"')
elif result == win32con.IDCANCEL:    
    win32ui.MessageBox('You pressed "Cancel"')
    
