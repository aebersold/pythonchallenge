import sys
import re

f = open('challenge3.txt', 'r')
text = f.read()

m = re.findall('([^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z])', text, re.MULTILINE)

for s in m:
    sys.stdout.write(s[4])

print ''


