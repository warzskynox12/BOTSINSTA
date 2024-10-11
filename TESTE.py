import os
import json

nombredeclass = len(os.listdir("classe"))
print(f"Nombre de classes : {nombredeclass}")

t = 0
p = 0
s = 0
tsti = 0
psti = 0
tbts = 0
pbts = 0
for file in os.listdir("classe"):
    if file.startswith("T"):
        t = t+1
    if file.startswith("1"):
        p = p+1
    if file.startswith("2"):
        s = s+1
    if file.startswith("TSTI"):
        tsti = tsti+1
    if file.startswith("1STI"):
        psti = psti+1
    if file.startswith("TBTS"):
        tbts = tbts+1
    if file.startswith("1BTS"):
        pbts = pbts+1

print(f"Nombre de classes de terminal : {t}")
print(f"Nombre de classes de première : {p}")
print(f"Nombre de classes de seconde : {s}")
print(f"Nombre de classes de Terminal STI : {tsti}")
print(f"Nombre de classes de premier STI : {psti}")
print(f"Nombre de classes de terminal BTS : {tbts}")
print(f"Nombre de classes de premier BTS : {pbts}")
print(f"nombre de classes :{t+p+s}:{tsti+psti+tbts+pbts}")




