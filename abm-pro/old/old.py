#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("cd 64bit && python2 aro.py")
elif bit == '32bit':
    os.system("cd 32bit && python2 pro.py")
