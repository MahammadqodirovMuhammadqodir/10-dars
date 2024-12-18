import math

son = int(input("Butun son kiriting: "))
if son > 0:
    son += 1
print(f"Hosil bo'lgan son: {son}")

son = int(input("Butun son kiriting: "))
if son > 0:
    son += 1
elif son < 0:
    son-=2
print(f"Hosil bo'lgan son: {son}")

a = int(input("Butun son kiriting: "))
if a > 0:
    a += 1
elif a < 0:
    a-=2
elif a ==0:
    a+=10
print(f"Hosil bo'lgan son: {a}")

a = int(input("1-Butun son kiriting: "))
b = int(input("2-Butun son kiriting: "))
c = int(input("3-Butun son kiriting: "))
d = 0
if a > 0:
    d = d + 1
if b > 0:
    d = d + 1
if c > 0:
    d = d + 1
print(d)


a = float(input("1-Butun son kiriting: "))
b = float(input("2-Butun son kiriting: "))
c = float(input("3-Butun son kiriting: "))
s = 0
d = 0
if a > 0:
    s = s + 1
elif a < 0:
     d = d + 1
if b > 0:
    s = s + 1
elif b < 0:
     d = d + 1
if c > 0:
    s = s + 1
elif c < 0:
     d = d + 1
print(s)
print(d)

a = int(input("1-sonni kiriting"))
b = int(input("2-sonni kiriting"))
if a > b:
    print(a)
elif b > a:
    print(b)


a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
kichik_son_tartib = 1 if a < b else 2
print(f"Kichik sonning tartib raqami: {kichik_son_tartib}")

a = int(input("1-sonni kiriting"))
b = int(input("2-sonni kiriting"))
if a > b:
    print(f"Katta {a}, Kichik{b}")
else:
    print(f"Katta {b}, Kichik{a}")



a = float(input("A sonini kiriting: "))
b = float(input("B sonini kiriting: "))
if a < b:
    print(f"Kichik {a}, Katta{b}")
else:
    print(f"Kichik {b}, Katta{a}")



A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))
if A != B:
    A = B = A + B
else:
    A = B = 0
print(f"A: {A}, B: {B}")


A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))
if A != B:
    katta = max(A, B)
    A = B = katta
else:
    A = B = 0
print(f"A: {A}, B: {B}")

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiritimg: "))
d = min(a, b, c)
print(f"Eng kichik son {d}")



a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiritimg: "))
d = sorted([a, b, c])[1]
print(f"O`rtacha son {d}")



a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
kichik_son = min(a, b, c)
katta_son = max(a, b, c)
print(f"Kichik son: {kichik_son}, Katta son: {katta_son}")

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
yigindi = a + b + c
katta_ikkitasi = sorted([a, b, c])[1:]
print(f"Yig'indi: {yigindi}, Katta ikkita son: {katta_ikkitasi}")



A = float(input("A sonini kiriting: "))
B = float(input("B sonini kiriting: "))
C = float(input("C sonini kiriting: "))
if A < B < C:
    A, B, C = A*2, B*2, C*2
else:
    A, B, C = -A, -B, -C
print(f"A: {A}, B: {B}, C: {C}")


A = float(input("A sonini kiriting: "))
B = float(input("B sonini kiriting: "))
C = float(input("C sonini kiriting: "))
if A < B < C or A > B > C:
    A, B, C = A*2, B*2, C*2
else:
    A, B, C = -A, -B, -C
print(f"A: {A}, B: {B}, C: {C}")


a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
if a == b or b == c or a == c:
    teng_son = [a, b, c].count(a) > 1 or [a, b, c].count(b) > 1
    tartib = 3 if teng_son else 1
    print(f"Uchinchisining tartib raqami: {tartib}")


a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: ")) 
c = int
c = int(input("3-sonni kiriting: "))
d = int(input("4-sonni kiriting: "))
if a == b == c or b == c == d or a == b == d or a == c == d:
    print("Uchchisi teng, bitta sonning tartib raqami aniqlansin")