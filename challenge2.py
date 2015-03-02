import sys
f = open('challenge2.txt', 'r')

for c in f.read():
    if 97 <= ord(c) <= 122:
        sys.stdout.write(c)

print ''


