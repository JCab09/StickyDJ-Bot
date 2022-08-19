#!/usr/bin/env python3
"""
This class uses the yaml-parser in order to create the 
apropriate config-dictionary for the client who requested it

Author: Jason Cabezuela
"""
from src.util.parser.yaml_parser import yaml_parser
import string


def getConfig(filepath, type = '.yaml', context = None):
    """PLACEHOLDER
    """
    if type.startswith('.') is False:
        filepath + '.'
    file = filepath + type
    config = parseConfig(file, type)
    if context is not None:
        return config.get(context)
    else:
        return config
    

def parseConfig(file, type):
    """PLACEHOLDER
    """
    if type == '.yaml':
        return yaml_parser.get_config(file)
    else:
        print("ERROR: Config filetype (%s) not supported! ", type)