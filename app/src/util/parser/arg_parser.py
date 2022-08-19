#!/usr/bin/env python3
"""
ArgumentParser Class for client startup
Author: Jason Cabezuela
"""
import argparse


class arg_parser():
    """Class for parsing startup parameters"""
    def __init__(self):
        print("PARSING ARGS")
        self._args = dict()
        parser = argparse.ArgumentParser(description="Configure StickyDJ-Bot")
        parser.add_argument('-c', '--config', dest='config', 
                            help='specify path to main-config')

        parser.add_argument('-t', '--type', dest='type', default = '.yaml',
                            help='specify main-config type. Defaults to ".yaml"')

        parser.add_argument('-d', '--debug', action='store_const', dest='debug',
                            const=True, default=False,
                            help='Set Debugging-Flag to True')
        try:
            self._args = vars(parser.parse_args())
        except:
            print("No Startup-Arguments received")
            self._args = None

#        k = input("Press 'Enter' to exit")

    def getArgs(self):
        return self._args
