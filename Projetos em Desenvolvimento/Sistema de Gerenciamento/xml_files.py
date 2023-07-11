import os
import xml.etree.ElementTree as Et


class Ler_xml:
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        return [
            os.path.join(self.directory, arq)
            for arq in os.listdir(self.directory)
            if arq.lower().endswith(".xml")
        ]

    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace(".", ",")
            except:
                return var.text
