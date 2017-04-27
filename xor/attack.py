from collections import * 

dlugosc_kluczu = 7 

d = open("dane.txt","rb").read().decode("utf-8")
od = []
for ch in d:
    if ord(ch) > 0x7e:
        continue
    od.append(chr(ord(ch)))

d = ''.join(od)
h = Counter(d)
#print h
most_common = ord(h.most_common(1)[0][0])

d = open("data.xorred","rb").read()
hin = []
key= ""

for i in range(dlugosc_kluczu):
    c = Counter(d[i::dlugosc_kluczu])
    hin.append(c)
    print c.most_common(1)
    in_most_common = ord(c.most_common(1)[0][0])
    key+= chr(most_common ^ in_most_common)

print key.encode("hex")

def xor(dane,klucz):
    klucz = bytearray(klucz)
    dane = bytearray(dane)

    output = []
    for i, d in enumerate(dane):
        output.append(chr(d ^ klucz[i % len(klucz)]))

    return ''.join(output)

print xor(d,key)

