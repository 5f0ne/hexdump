import os
import sys

import argparse

from hexlib.HexTwin import HexTwin
from hexlib.Hexdump import Hexdump

from hexdumper.Controller import Controller

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
    parser.add_argument("--filterZeroRows", "-f", action="store_true", help="Skip zero rows in hexdump output")
    parser.add_argument("--filterNonAsciiRows", "-e", action="store_true", help="Skip non-ascii rows in hexdump output")
    parser.add_argument("--noHash", "-n", action="store_false", help="Disable hashing e.g. for big files")
    args = parser.parse_args()

    c = Controller(args.path, args.noHash)

    c.printHeader()

    if(os.path.isfile(args.path)):
        twin = HexTwin(args.path)
        dump = Hexdump()
        
        if(args.filterNonAsciiRows):
            dump.filter(filterNonAsciiRows=True)
        elif(args.filterZeroRows):
            dump.filter(filterZeroRows=True)
       
        dump.printTwin(twin)
    else:
        print("The provided path is not a file!")
        pass      

    print("")
    print("######################################################################################################################")
    
    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


