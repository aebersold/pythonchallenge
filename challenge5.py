import pickle
import sys

f = open('challenge5.txt', 'r')
deserialized = pickle.Unpickler(f).load()

for d in deserialized:
    for i in d:
        for _ in range(i[1]):
            sys.stdout.write(i[0])
    sys.stdout.write('\n')

print ""
print "configure terminal to min 95 chars width"