class Hexdump():
    def __init__(self, path="") -> None:
        self.path = path
    
    def print(self):
        with open(self.path, "rb") as f:
            offset = 0
            self.printHexTableHeader()
            while True:
                bytes_ = f.read(16)
                if not bytes_:
                    break
                hexList = self.getHexList(bytes_, self.formatOffset(offset))
                self.printHexTableRow(hexList)
                offset += 16

    def printNoOfBytes(self, hexList):
        offset = 0
        # hexList contains hex values ["00", "0A", "FF", ...] etc.
        # We are going to split it into rows of 16 values for correct printing
        splitted = [hexList[x:x+16] for x in range(0, len(hexList), 16)]
        self.printHexTableHeader()
        
        for line in splitted:
            line.insert(0, self.formatOffset(offset))
            self.printHexTableRow(line)
            offset += 16

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
        h = "{:10}     {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:5}".format("    Offset", "00", "01", "02", "03", "04", "05",
                                                                                                                          "06", "07", "08", "09", "0A", "0B",
                                                                                                                          "0C", "0D", "0E", "0F", "ASCII")
        print(h)
        print("----------     -------------------------------------------------------------------------------        ----------------")

    def printHexTableRow(self, h):
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
        return r.rjust(10, "0").upper()

    def hexToAscii(self, hex_):
        result = "."
        if (hex_ != "  "):
            d = int(hex_, 16)
            if (d >= 32 and d <= 126):
                result = chr(d)
        return result