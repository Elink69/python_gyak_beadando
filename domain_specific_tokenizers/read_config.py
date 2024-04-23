"""
    Config fájl beolvasása
"""
import os
import json


def read_config():
    """
       Config fájl beolvasása
    """

    with open(os.path.join(os.path.dirname(__file__), "config.json"),
              encoding="utf-8") as config_file:
        return json.load(config_file)
