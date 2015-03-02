import urllib

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?%s'
params = {'nothing': 12345}

while True:
    encoded = urllib.urlencode(params)
    f = urllib.urlopen(url % encoded)
    line = f.read()

    if 'and the next nothing is' in line:
        parts = line.rpartition(' ')
        params['nothing'] = int(parts[2])
        print parts[2]
    elif 'Divide by two' in line:
        print line
        params['nothing'] = params.get('nothing') / 2
    else:
        print line
        break