klucz  = "30daa3363d4571".decode("hex")
tekst =  "siema co tam kumplu"

def xor(dane,klucz):
    klucz = bytearray(klucz)
    dane = bytearray(dane)

    output = []
    for i, d in enumerate(dane):
        output.append(chr(d ^ klucz[i % len(klucz)]))

    return ''.join(output)

#print tekst
#print xor(tekst,klucz)

d = open("dane2.txt").read()
e = xor(d,klucz)

open("data.xorred","wb").write(e)


