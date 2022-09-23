import os
import argparse

from src.Controller import Controller

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
args = parser.parse_args()

c = Controller(args.path)

c.printHeader()

if(os.path.isfile(args.path)):
    with open(args.path, "rb") as f:
        offset = 0
        c.printHexTableHeader()
        while True:
            bytes_ = f.read(16)
            if not bytes_:
                break
            hexList = c.getHexList(bytes_, c.formatOffset(offset))
            c.printHexTable(hexList)
            offset += 16
else:
    print("The provided path is not a file!")
    pass      

print("")
print("####################################################################################################################")

c.printExecutionTime()