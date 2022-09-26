import os
import sys

import argparse

from hexdumper.Hexdump import Hexdump
from hexdumper.Controller import Controller

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to file")
    parser.add_argument("--noHash", "-nH", action="store_false", help="Disable hashing e.g. for big files")
    args = parser.parse_args()

    c = Controller(args.path, args.noHash)

    c.printHeader()

    if(os.path.isfile(args.path)):
        hD = Hexdump(args.path)
        hD.print()
    else:
        print("The provided path is not a file!")
        pass      

    print("")
    print("######################################################################################################################")
    
    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())


