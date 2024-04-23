"""
    Ez a modul jeleníti meg az tokenizálók eredményeiről szóló dokumentumot
"""

import os
import webview


def tokenizer_info():
    """
        A tokenizálók oldal megnyitását végző függvény
    """

    package_directory = os.path.dirname(__file__)
    html_file_path = os.path.join(package_directory,
                                  "pages", "tokenizers.html")
    webview.create_window("Tokenizálók", html_file_path, width=1000,
                          height=750)
    webview.start()
