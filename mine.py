from bitcoin import *
priv = sha256("MyEcoria")
pub = privtopub(priv)
addr = pubtoaddr(pub)
h = history(addr)

print (priv)
print (pub)
print (addr)
print (h)
