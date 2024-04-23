"""
    Ez a modul jeleníti meg az adathalmazokról szóló dokumentumot
"""

import os
import webview


def datasets_info():
    """
        A domains oldal megnyitását végző függvény
    """

    package_directory = os.path.dirname(__file__)
    html_file_path = os.path.join(package_directory, "pages", "domains.html")
    webview.create_window("Domének", html_file_path, width=1000, height=750)
    webview.start()
