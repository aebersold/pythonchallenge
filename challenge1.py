import sys

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#text = "http://www.pythonchallenge.com/pc/def/map.html"

for c in text:
    i = ord(c)

    if i in [121,122]:
        c = chr(i - 26 + 2)
        
    elif 97 <= i <= 120:
        c = chr(i + 2)
    
    sys.stdout.write(c)

print ''