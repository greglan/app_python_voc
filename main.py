# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
from core import App

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "s.txt"

app = App.App(filename)
app.run()