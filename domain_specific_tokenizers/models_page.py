"""
    Ez a modul jeleníti meg az modellek eredményeiről szóló dokumentumot
"""

import os
import webview


def model_info():
    """
        A modell oldal megnyitását végző függvény
    """

    package_directory = os.path.dirname(__file__)
    html_file_path = os.path.join(package_directory, "pages", "models.html")
    webview.create_window("Modellek", html_file_path, width=1000, height=750)
    webview.start()
