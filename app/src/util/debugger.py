"""
This module contains the debugger-functions

Author: Jason Cabezuela
"""
class Debugger(object):
    def __init__(self, debugFlag = False):
        self._isEnabled = debugFlag
    def write(self, text):
        if self._isEnabled == True:
            print(text)