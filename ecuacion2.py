import math
import os


a=int(input("valor a:"))
b=int(input("valor b:"))
c=int(input("valor c:"))
b2: float = math.pow(b, 2)

res = -4*a*c
res2 = b2+res
rai = math.sqrt(res2)

sp: object = ((-b+rai)/(2*a))
sn: object = ((-b-rai)/(2*a))

print("Primera Solucion:")
print(sp)
print("Segunda Solucion")
print(sn)




os.system("pause")