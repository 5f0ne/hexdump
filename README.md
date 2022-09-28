# Description

Prints the hexdump of a selected file.

# Installation

`pip install hexdumper`

# Usage

**From command line:**

`python -m hexdumper [-h] --path PATH [--noHash] [--filterZeroRows] [--filterNonAsciiRows]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file which shall be dumped |
|--noHash | -n | Flag | False | Disable hashing e.g. for big files |
|--filterZeroRows | -f | Flag | False | Filters zero rows in hex dump |
|--filterNonAsciiRows | -e | Flag | False | Filters non ascii rows in hex dump |

# Example

`python -m hexdumper -p "path/to/file/test.txt" --filterNonAsciiRows > result.txt`

You can find the following result [here](./example/example.txt):

```
######################################################################################################################

Hexdump by 5f0
Prints the hexdump of a selected file

Current working directory: /path/to/file
        Investigated file: ./test.txt

                 MD5 Hash: d797c50d23c9adf6119b06f3d0811e44
              SHA256 Hash: b27bdc8247be9509d9530830ef31cf119ae7efcf36ae334b1c8865d404df675b

                 Datetime: 01/01/1970 13:14:15

######################################################################################################################

    Offset     00   01   02   03   04   05   06   07     08   09   0A   0B   0C   0D   0E   0F        ASCII
----------     -------------------------------------------------------------------------------        ----------------
0000000000     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   31   0A        I am testline 1.

---------------------------------------------> Skipped 1 non-ascii rows <---------------------------------------------

0000000020     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   32   0A        I am testline 2.
0000000030     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   33   33        I am testline 33
0000000040     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   34   0A        I am testline 4.

---------------------------------------------> Skipped 39 non-ascii rows <---------------------------------------------

00000002C0     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   35   0A        I am testline 5.
00000002D0     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   36   0A        I am testline 6.
00000002E0     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   37   0A        I am testline 7.

---------------------------------------------> Skipped 2 non-ascii rows <---------------------------------------------

0000000310     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   38   0A        I am testline 8.
0000000320     49   20   61   6D   20   74   65   73     74   6C   69   6E   65   20   39   0A        I am testline 9.

######################################################################################################################

Execution Time: 0.004000 sec
```

# License

MIT