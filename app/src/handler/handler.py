"""Base Handler Module
This module contains the BaseHandler class.

Author: Jason Cabezuela
"""
import src.util.configmaker as configmaker


class BaseHandler(object):
    """Base Handler-Class
    This class is the base of all handler classes
    and holds their common properties and functions
    """
    def __init__(self):
        self._handlerContext = {}
    
    def load_context(self, key, path, type):
        """Loads a config file and saves it internally
        Takes a path and a filetype of type str()
        and saves it as a dict() under given key"""
        context = configmaker.getConfig(path, type)
        self._handlerContext.update({key : context})
        print(self._handlerContext)
