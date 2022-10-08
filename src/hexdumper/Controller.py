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


    def writeFileHeader(self, outfile, path, isOffset=False, offset = 0, noOfBytes = 0):
        with open(outfile, "w") as f:
            f.write("         Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
            f.write("\n")
            f.write("Investigated File: " + path + "\n")
            f.write("         MD5 Hash: " + self.md5 + "\n")
            f.write("      SHA256 Hash: " + self.sha256 + "\n")
            f.write("\n")

            if(isOffset):
                e = open(path,"rb")
                e.seek(offset, 0)
                b = e.read(noOfBytes)
                e.close()
                h = HashCalc.fromBytes(b)
                f.write("           Offset: " + str(offset) + "\n")
                f.write("     No. of bytes: " + str(noOfBytes) + "\n")
                f.write("         MD5 Hash: " + h.md5 + "\n")
                f.write("      SHA256 Hash: " + h.sha256 + "\n")
                f.write("\n")


    def printExecutionTime(self):
        end = time.time()
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")