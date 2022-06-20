# Integers kan kodas i andra format: 
print(0x01) # Hexadecimal 0-9, A-F
print(0o01) # Octal 1-7
print(0b00000101) # Binary 0-1 där längst åt höger är 1, och vänster 128.

# Få fram andra kodningar
x = 10
hex(x)
oct(x)
bin(x)

# Skapa komplexa tal
y = complex(3,5)
print(y)

# Expression Operators
# Chained comparisons

X = 2
Y = 4
Z = 6

X < Y < Z
# Blir samma som nedan, fast snabbare att beräkna.
X < Y and Y < Z

1.1 + 2.2 == 3.3 # False, limited precisin (3.30000000000000003)
int(1.1 + 2.2) == int(3.3) # True

# Division






