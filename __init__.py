# -*- coding: utf-8 -*-
#!/usr/bin/env python


from utils import *
import platform

# Os detection
os = platform.system()

if os=="Windows":
    pass
        
app = App('s.txt')
app.run()