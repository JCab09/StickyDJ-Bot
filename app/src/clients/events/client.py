#!/usr/bin/env python3
"""
Event-Client Base-Class
This is the parent-class of all "Event-based client-classes".
It holds properties and functions which every event-client needs.

Author: Jason Cabezuela
"""
import src.clients.client as BaseClient


class EventClient(BaseClient.BaseClient):
    """Event-Client Base-Class"""
    def __init__(self, configpath, configtype):
        print("INIT EventClient")
        BaseClient.BaseClient.__init__(self, configpath, configtype)

        _defaultCmdSymbol = "!"
        self._cmdSymbol = _defaultCmdSymbol

        self._messageList = []

        print("INIT_END EventClient")

    @property
    def cmdSymbol(self):
        return self._cmdSymbol

    def _getCredentials(self):
        """Function for retrieving the token from its file"""
        _path = self._clientConfig.get('token').get('path')
        print(_path)
        try:
            _file = open(_path, 'rt')
        except:
            print("WARNING - Token ERROR: Could not open token-file at '" + _path + "'")
            return None

        _credentials = _file.readlines()
        _file.close()
        return _credentials

    def _add_newMessage(self, message, user = None):
        """Function for adding a new Message to the list.
        Adds a tuple of type (user, message) to the internal _messageList.
        'User' defaults to 'None' if not specified
        """
        self._messageList.append((user, message))
        print("message added to list")
        

    def get_newMessage(self):
        """
        Returns 'messageauthor', 'message'
        """
        if self._messageList:
            messageContext = self._messageList.pop(0)
            print("get_newMessage SUCCESS")
            return messageContext[0], messageContext[1]
        else:
            return None, None

    def startup(self):
        """Override this function"""

    def shutdown(self):
        """Override this function"""
