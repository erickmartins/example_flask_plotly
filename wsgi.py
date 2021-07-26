#!/usr/bin/env python

import sys
import site

site.addsitedir('/home/ratame/miniconda3/envs/dashboard/lib/python3.9/site-packages/')

sys.path.insert(0, '/home/ratame/example_flask_plotly')

from app import app as application
