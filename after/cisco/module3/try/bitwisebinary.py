x = 4
y = 1

a = x & y
#100 & 001 will be 000 so 0
b = x | y
#101 so 5
c = ~x  # tricky!
# ~x is 1011 whis is two's complement of 0101 so -5
d = x ^ 5
#100 ^ 101 that is 001 so 1
e = x >> 2
#100>>2 so 1
f = x << 2
#100<<2 is 10000 so 16
print(a, b, c, d, e, f)
