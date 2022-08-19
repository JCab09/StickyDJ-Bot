#!/usr/bin/env python3
"""
Base-Client Class
This is the parent-class of all client-classes and holds properties and functions they all depend on.

Author: Jason Cabezuela
"""
import src.util.debugger as Debugger
import src.util.configmaker as configmaker


class BaseClient(object):
    """Base-Client Class"""
    def __init__(self, configpath, configtype, debugFlag = False):
        self._Debug = Debugger.Debugger(debugFlag)
        self._Debug.write("INIT BaseClient")

        defaultPrompt = "-"

        self._prompt = defaultPrompt
        self._clientConfig = configmaker.getConfig(configpath, configtype)
                
        self._Debug.write("INIT_END BaseClient")

    @property
    def prompt(self):
        return self._prompt

    def get_client_configuration():
        """Base Class for getting client configuration"""
        

    def load_client_configuration():
        """Base Class for loading client configuration into memory"""
