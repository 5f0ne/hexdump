import os
import time
import hashlib

from datetime import datetime

class Controller():
    def __init__(self, path, hashingAllowed) -> None:
        self.startTime = time.time()
        self.md5 = "-"
        self.sha256 = "-"
        self.path = path
        if(hashingAllowed):
            self.__calculateFileHash()

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

    def __calculateFileHash(self):

        sha256 = hashlib.sha256()
        md5 = hashlib.md5()

        with open(self.path, "rb") as f:
            while True:
                data = f.read(65536) 
                if not data:
                    break
                sha256.update(data)
                md5.update(data)

        self.sha256 = sha256.hexdigest()
        self.md5 = md5.hexdigest()