#!/usr/bin/env python3

import re

try:
    while True:
        a = [ ]
        b = [ ]
        for word in re.split(R"[,;]", input()):
            (a if re.match(R"^(0|[1-9][0-9]*)$", word) else b).append(word)
        print('"%s"' % ','.join(a) if a else '-')
        print('"%s"' % ','.join(b) if b else '-')

except EOFError:
    pass