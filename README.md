# Description

Prints the hexdump of a selected file

# Usage

`main.py [-h] --path PATH`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to file which shall be dumped |


# Example

`python main.py -p "path/to/file/test.txt" > result.txt`

You can find the following result [here](./example/example.txt):

```
####################################################################################################################

Hexdump by 5f0
Prints the hexdump of a selected file

Current working directory: /path/to/file
        Investigated file: ./test.txt

                 MD5 Hash: d797c50d23c9adf6119b06f3d0811e44
              SHA256 Hash: b27bdc8247be9509d9530830ef31cf119ae7efcf36ae334b1c8865d404df675b

                 Datetime: 01/01/1970 13:14:15

####################################################################################################################

  Offset      0    1    2    3    4    5    6    7      8    9    A    B    C    D    E    F        ASCII
--------     -------------------------------------------------------------------------------        ----------------
00000000     48   69   2C   20   49   27   61   6D     20   61   20   74   65   73   74   20        Hi, I'am a test 
00000010     66   69   6C   65   20   66   6F   72     20   74   68   65   20   68   65   78        file for the hex
00000020     64   75   6D   70   20   74   6F   6F     6C   0D   0A   21   22   C2   A7   24        dump tool..!"..$
00000030     25   26   2F   28   29   3D   3F   23     2B   2A   7E   2D   5F   2E   3A   2C        %&/()=?#+*~-_.:,
00000040     3B   3C   3E   7C                                                                      ;<>|............

####################################################################################################################

Execution Time: 0.0 sec
```

# License

MIT