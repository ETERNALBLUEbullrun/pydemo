#TestIo.py exercises various Python input/output
import sys
import io
import locale
import os

inmemoryFile = io.StringIO("default 1")
fullStr = "This sentence should be on a single line.\n"
if "default 1" != inmemoryFile.getvalue():
    raise Exception("E: inmemoryFile should = 'default 1', not '" + inmemoryFile.getvalue() + "'")
print("This sente", "nce should", sep = '', end = '', file = inmemoryFile)
print(" be on a single line.", end='\n', file = inmemoryFile)
if fullStr != inmemoryFile.getvalue():
    raise Exception("E: inmemoryFile should = '" + fullStr + "', not '" + inmemoryFile.getvalue() + "'")
inmemoryFile.close()

try:
    fd = open("out.tmp", mode = 'r')
    raise Exception("E: file 'out.tmp' already exists")
except IOError:
    pass
#fd = io.TextIOWrapper(open("out.tmp", mode = 'x', buffering = -1, errors = None, newline = None, encoding = locale.getpreferredencoding(False), closefd = True, opener = None))
fd = io.TextIOWrapper(open("out.tmp", mode = 'xb', buffering = -1, errors = None, newline = None, closefd = True, opener = None))
print("This sente", "nce should", sep = '', end = '', file = fd)
print(" be on a single li", end='', file = fd)
fd.close()
if fd := open("out.tmp", mode = 'a', newline = None):
    print("ne.\n", end='', file = fd)
    fd.close()
else:
    raise Exception("E: failed to reopen in append mode'")
if fd := open("out.tmp", mode = 'r', newline = None):
    foundStr = fd.read();
    fd.close()
    if fullStr != foundStr:
        raise Exception("E: fd should = '" + fullStr + "', not '" + foundStr + "'")
else:
    raise Exception("E: failed to reopen in read mode'")
if os.path.exists("out.tmp"):
    os.remove("out.tmp")
else:
    raise Exception("E: out.tmp not found")

