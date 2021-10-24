#coding=utf-8
#!/usr/bin/python2

import os
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    from abm64 import abm_mix
    abm_mix()
elif bit == '32bit':
    from abm32 import abm_mix
    abm_mix()
