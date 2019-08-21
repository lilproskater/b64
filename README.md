# b64

## About project
This is a universal base64 converter which can encode/decode base64 as to console as to file. Do you want to easily encode/decode base64 without going to your browser and searching for a converter? So you are welcome  

## Instruction
All the instrucitons can be given by ```python3 b64.py``` or ```python3 b64.py --help```.
Output:
```Usage: b64.py [options] [message]
       b64.py [options] [input_file] [output_file]

-e, --encode      encode message or input file
-d, --decode      decode message or input file```
As you can see here you can use 2 variations. If you give 3 arguments the [message] will be encoded/decoded, but if you give 4 arguments the text in input_file will be encoded/decoded and written to [output_file] as a new file or you will be asked for overwriting a file if it already exsists.
###Notice:
The script works only on Python 3


