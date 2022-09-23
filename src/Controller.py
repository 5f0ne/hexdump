import os
import time
import hashlib

from datetime import datetime

class Controller():
    def __init__(self, path) -> None:
        self.startTime = time.time()
        self.md5 = "-"
        self.sha256 = "-"
        self.path = path
        self.__calculateFileHash()

    def printHeader(self):
        print("####################################################################################################################")
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
        print("####################################################################################################################")
        print("")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")

    def getHexList(self, bytes_, offset):
        # Convert the bytes to a list of hex values
        hexlist = [hex(x).split('x')[-1].upper() for x in list(bytes_)]
        result = [offset]

        for hex_ in hexlist:
            # While converting the bytes, the leading zeros gets cut of
            # the following instructions check if there are 2 characters
            # and adds a leading zero if necessary
            if (len(hex_) == 2):
                result.append(hex_)
            elif (len(hex_) == 1):
                result.append("0" + hex_)

        return result

    def printHexTableHeader(self):
        h = "{:4}     {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:5}".format("  Offset", " 0", " 1", " 2", " 3", " 4", " 5",
                                                                                                                          " 6", " 7", " 8", " 9", " A", " B",
                                                                                                                          " C", " D", " E", " F", "ASCII")
        print(h)
        print("--------     -------------------------------------------------------------------------------        ----------------")

    def printHexTable(self, h):
        formatStr = "{:4}     {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}"

        # Padding for lines with less than 16 bytes
        while True:
            if (len(h) < 17):
                h.append("  ")
            else:
                break

        a = [""]
        for i in range(1, 17):
            a.append(self.hexToAscii(h[i]))

        r = formatStr.format(h[0],
                             h[1], h[2],  h[3],  h[4],  h[5],  h[6],  h[7],  h[8],
                             h[9], h[10], h[11], h[12], h[13], h[14], h[15], h[16],
                             a[1], a[2],  a[3],  a[4],  a[5],  a[6],  a[7],  a[8],
                             a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16])
        print(r)

    def formatOffset(self, offset):
        r = hex(offset).split('x')[-1]
        return r.rjust(8, "0").upper()

    def hexToAscii(self, hex_):
        result = "."
        if (hex_ != "  "):
            d = int(hex_, 16)
            if (d >= 32 and d <= 126):
                result = chr(d)
        return result

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