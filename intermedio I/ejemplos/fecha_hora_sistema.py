# fecha y hora del sistema:

import time

t = time.strftime("%H:%M:%S")
d = time.strftime("%d/%m/%y")
d2 = time.strftime("%d/%m/%Y")
dt = time.strftime("%d/%m/%Y %H:%M:%S")

print ("time: ", t)
print ("date: ", d)
print ("date: ", d2)
print ("datetime: ", dt)
