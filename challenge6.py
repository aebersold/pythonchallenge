import zipfile
import string

zip = zipfile.ZipFile('challenge6.zip', 'r')
comments = []

nr = '90052'

while True:
    file = zip.open(nr + '.txt', 'r')
    comments.append(zip.getinfo(nr + '.txt').comment)
    line = file.read()

    if any(word in line for word in ['answer', 'welcome', 'comments.']):
        break
    else: 
        parts = line.rpartition(' ')
        nr = parts[2]

print string.join(comments)