from base64 import b64encode, b64decode
from sys import argv
from binascii import Error as decode_error
from os.path import isfile as file_exists


if len(argv) == 1 or (len(argv) == 2 and argv[1] == '--help'):
    print("Usage:", argv[0], "[options] [message]")
    print("{0:6}".format(""), argv[0], "[options] [input_file] [output_file]", end="\n\n")
    print("-e, --encode{0:6}encode message or input file".format(""))
    print("-d, --decode{0:6}decode message or input file".format(""))

elif len(argv) == 3:
    if argv[1] in ('-e', '--encode'):
        print(b64encode(argv[2].encode()).decode())
    elif argv[1] in ('-d', '--decode'):
        try:
            print(b64decode(argv[2].encode()).decode())
        except decode_error:
            print("Error: Cannot decode message to base64. Check if the message is encoded correctly.")
        except UnicodeDecodeError:
            print("Error: Ooops! Got strange decoding. Please, try to decode it as file.")
    else:
        print("Error: Invalid [options] arguments")

elif len(argv) == 4:
    try:
        message = []
        with open(argv[2], "rb") as reading_file:
            for line in reading_file:
                message.append(line)

    except FileNotFoundError:
        print("Error: File {} is not found!".format(argv[2]))
        exit()
    if file_exists(argv[3]):
        if input("File {} already exists! Overwrite that file? (y/n): ".format(argv[3])).lower() != 'y':
            exit()
    if argv[1] in ('-e', '--encode'):
        with open(argv[3], 'wb') as writing_file:
            for line in message:
                writing_file.write(b64encode(line) + b'\n')
    elif argv[1] in ('-d', '--decode'):
        try:
            with open(argv[3], 'wb') as writing_file:
                for line in message:
                    writing_file.write(b64decode(line) + b'\n')
        except decode_error:
            print("Error: Cannot decode text in file to base64. Check if the text is encoded correctly.")
    else:
       print("Error: Invalid [options] arguments")    
else:
    print("Error: Invalid arguments quantity. See {} --help".format(argv[0]))
