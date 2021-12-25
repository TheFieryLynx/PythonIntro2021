import zipfile
import sys
import io

def dir_check(a):
    return not a.is_dir()

inputZip = sys.stdin.read()
hex_to_byte = bytearray.fromhex(inputZip)

with zipfile.ZipFile(io.BytesIO(hex_to_byte), "r") as zp:
    files = []
    for i in zp.filelist:
        if dir_check(i):
            files.append(i)
    ssum = 0
    for i in files:
        ssum += i.file_size
    print(len(files), ssum)

