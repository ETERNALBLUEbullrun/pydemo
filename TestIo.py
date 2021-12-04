#TestIo.py exercises various Python input/output
import sys
import io
import locale
import os

inmemoryFile = io.StringIO("default str")
fullStr = "This sentence should be on a single line.\n"
if "default str" != inmemoryFile.getvalue():
    raise Exception("E: inmemoryFile should = 'default', not '" + inmemoryFile.getvalue() + "'")
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
fd = io.TextIOWrapper(open("out.tmp", mode = 'x', buffering = -1, errors = None, newline = None, encoding = locale.getpreferredencoding(False), closefd = True, opener = None))
if "default str" != fd.getvalue():
    raise Exception("E: fd should = 'default', not '" + fd.getvalue() + "'")
print("This sente", "nce should", sep = '', end = '', file = fd)
print(" be on a single li", end='\n', file = fd)
fd.close()
if fd := open("out.tmp", mode = 'a', newline = None):
    print("ne.", end='\n', file = fd)
else:
    raise Exception("E: failed to reopen in append mode'")
if fullStr != fd.getvalue():
    raise Exception("E: fd should = '" + fullStr + "', not '" + fd.getvalue() + "'")
if os.path.exists("out.tmp"):
    os.remove("out.tmp")
else:
    raise Exception("E: out.tmp not found")

