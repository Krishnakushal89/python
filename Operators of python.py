a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
print(a,b)
# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Comparison Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal To:", a >= b)
print("Less Than or Equal To:", a <= b)

# Assignment Operators
a += b   # a = a + b
print("After a += b, a =", a)
a -= b   # a = a - b
print("After a -= b, a =", a)
a *= b   # a = a * b
print("After a *= b, a =", a)
a /= b   # a = a / b
print("After a /= b, a =", a)

# Logical Operators
print("Logical AND:", a > b and b > 0)
print("Logical OR:", a > b or b < 0)
print("Logical NOT:", not(a > b))

# Bitwise Operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)

# Identity Operators
print("Identity (a is b):", a is b)
print("Identity (a is not b):", a is not b)

# Membership Operators (with lists for demonstration)
list_example = [1, 2, 3, 10, 5]
print("Membership (a in list):", a in list_example)
print("Membership (b in list):", b in list_example)

#Ternary Operators
# a = 10, b = 20, c if (a < b) { c = a } else { c = b } print c
print("a") if a > b else print("b") 