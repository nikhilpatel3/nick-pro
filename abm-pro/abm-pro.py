#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    from aarm64 import pro_main
    pro_main()
elif bit == '32bit':
    from aarm32 import pro_main
    pro_main()
