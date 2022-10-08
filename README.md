# Description

- Prints the hexdump of a selected file. 
- Filters zero and non-ASCII values.
- Reads x bytes starting from an offset

# Installation

`pip install hexdumper`

# Usage

**From command line:**

`python -m hexdumper [-h] --path PATH [--outfile OUTFILE] [--offset OFFSET] [--noOfBytes NOOFBYTES] [--filterZeroRows] [--filterNonAsciiRows] [--noHash]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file which shall be dumped |
|--outfile | -o | String | result.txt | Path to result file |
|--offset | -s | Int | 0 | No of bytes to offset before read |
|--noOfBytes | -b | Int | - | Starting at offset and read the given number of bytes |
|--noHash | -n | Flag | False | Disable hashing e.g. for big files |
|--filterZeroRows | -f | Flag | False | Filters zero rows in hex dump |
|--filterNonAsciiRows | -e | Flag | False | Filters non ascii rows in hex dump |

# Example

`py -m hexdumper -p .\data\testfile`

**result.txt:**

```
         Datetime: 01/01/1970 10:11:12

Investigated File: result.txt
         MD5 Hash: 57f34e4aacacbd209eaf6990f16d0289
      SHA256 Hash: 162eb0e1083e50dd7832729b6b96cda7ba9ca76d21c8b46f706b204d3d8b8c0f

          Offset   00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F    ASCII           
----------------   -----------------------------------------------    ---------------- 
0000000000000000   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 31 0A    I am testline 1. 
0000000000000010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
0000000000000020   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 32 0A    I am testline 2. 
0000000000000030   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 33 33    I am testline 33 
0000000000000040   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 34 0A    I am testline 4. 
0000000000000050   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
0000000000000060   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
0000000000000070   BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB    ................ 
0000000000000080   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
0000000000000090   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
00000000000000A0   CC CC CC CC CC CC CC CC CC CC CC CC CC CC CC CC    ................ 
00000000000000B0   DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD    ................ 
00000000000000C0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
00000000000000D0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
00000000000000E0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
00000000000000F0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................ 
0000000000000100   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................
```

<hr>

`py -m hexdumper -p .\data\testfile --offset 0 --noOfBytes 120 --filterZeroRows`

**result.txt:**

```
         Datetime: 08/10/2022 23:13:12

Investigated File: result.txt
         MD5 Hash: 57f34e4aacacbd209eaf6990f16d0289
      SHA256 Hash: 162eb0e1083e50dd7832729b6b96cda7ba9ca76d21c8b46f706b204d3d8b8c0f

           Offset: 0
     No. of bytes: 120
         MD5 Hash: 83ad2f110819e0d358a4846352167740
      SHA256 Hash: e00caf06e9b512bd5787bcd08a1717f0bee668d7856d56cf244cdc1a4c5546c8

          Offset   00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F    ASCII           
----------------   -----------------------------------------------    ---------------- 
0000000000000000   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 31 0A    I am testline 1. 

--------------->   Skipped 1 zero rows  

0000000000000020   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 32 0A    I am testline 2. 
0000000000000030   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 33 33    I am testline 33 
0000000000000040   49 20 61 6D 20 74 65 73 74 6C 69 6E 65 20 34 0A    I am testline 4. 

--------------->   Skipped 2 zero rows  

0000000000000070   BB BB BB BB BB BB BB BB                            ........    
```


# License

MIT