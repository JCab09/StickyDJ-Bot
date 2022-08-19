#!/usr/bin/env python3
"""MasterConfig Class
This class utilizes the ArgumentParser and creates the Master-Configuration for
StickyDJ-Bot so it can properly operate.

Author: Jason Cabezuela"""
import src.util.parser.arg_parser as ArgumentParser
import src.util.parser.message_parser as MessageParser
import src.util.configmaker as configmaker
import src.util.debugger as Debugger
import src.handler.user.userhandler as UserHandler


class MasterConfig(object):
    def __init__(self):
        botArgs = ArgumentParser.arg_parser().getArgs()

        if botArgs is None:
            self._shutdown = True
            return
        self._shutdown = False

        self._Debug = Debugger.Debugger(botArgs.get('debug'))
        self._Debug.write("INIT MasterConfig")
        
        context = configmaker.getConfig(botArgs.get('config'), type = botArgs.get('type'))

        self._UserHandler = UserHandler.UserHandler()

        self._UserHandler.load_context('userlist',
                                       context.get('user').get('userlist').get('path'),
                                       context.get('user').get('userlist').get('type'))
        self._UserHandler.load_context('blacklist',
                                       context.get('user').get('blacklist').get('path'),
                                       context.get('user').get('blacklist').get('type'))

        self._clientContext = context.get('clients')
        self._moduleContext = context.get('modules')
        self._permissionContext = context.get('permissions')

        self._Debug.write("INIT_END MasterConfig")