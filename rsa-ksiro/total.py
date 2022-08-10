z = 20
e = 1
d = 7
f = (e * d) % z
print("inicio", f)
while f != 1:
    print("valor de e: ", e)
    e = e+1
    f = ((d * e) % z)
print("fim", e)
