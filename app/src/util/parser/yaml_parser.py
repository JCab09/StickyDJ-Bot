#!/usr/bin/env python3
"""
YAML-Parser Class
This class is for creating objects from config-files
which then are further processed by the configmaker module.

Author: Jason Cabezuela
"""
import yaml


class yaml_parser():   
    def get_config(yaml_document):
        """parse yaml-config_file"""
        print("PARSING: " + yaml_document)
        try:
            document = open(yaml_document, 'rb')
            object = yaml.safe_load(document)
            document.close()
        except:
            print("ERROR YAML-Parser - could not open file: '" + yaml_document + "'")   
        return object
        
        
