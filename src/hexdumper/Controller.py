import os
import time

from datetime import datetime

from hash_calc.HashCalc import HashCalc

class Controller():
    def __init__(self, path, hashingAllowed) -> None:
        self.startTime = time.time()
        self.md5 = "-"
        self.sha256 = "-"
        self.path = path
        if(hashingAllowed):
            h = HashCalc(path)
            self.md5 = h.md5
            self.sha256 = h.sha256

    def printHeader(self):
        print("######################################################################################################################")
        print("")
        print("Hexdump by 5f0")
        print("Prints the hexdump of a selected file")
        print("")
        print("Current working directory: " + os.getcwd())
        print("        Investigated file: " + self.path)
        print("")
        print("                 MD5 Hash: " + self.md5)
        print("              SHA256 Hash: " + self.sha256)
        print("")
        print("                 Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("######################################################################################################################")
        print("")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")