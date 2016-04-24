#!/usr/bin/env python

import sys

from app import app

if len(sys.argv) == 1:
    print('Usage: {} {command}'.format(sys.argv[0]))
    sys.exit(1)

command = sys.argv[1]
if command == 'serve':
    app.run(host='0.0.0.0')
