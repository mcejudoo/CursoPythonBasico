#ordenar una lista por la longitud de sus cadenas
        
L=["zzz","a","x","23xxx","aaaa""vfg"]
L2=["zzz","a","x","23xxx","aaaa""vfg"]

print ("L:", L)
L.sort()
print ("L.sort: ", L)
print ("\n")
print ("L2:", L2)
L2.sort(key=len)
print ("L2.sort: ", L2)
