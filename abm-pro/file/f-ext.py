#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    from ext64 import make_file
    make_file()
elif bit == '32bit':
    from ext32 import make_file
    make_file()
