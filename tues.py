# comparison operators (<, >, ==, !=, <=, >=)
# these compare two values and return a boolean
# let's declare some variables
comp1 = 10
comp2 = 15
print(comp1 < comp2)
print(comp1 > comp2)
print(comp1 >= comp2)
print(comp1 <= comp2)
print(comp1 != comp2)
print(comp1 == comp2)

# logical Operators (and (&), or (||), not(!)) we use & when all the statements are true
log1 = 5
log2 = 6
print((log1 > log2) and (log2 < log1))
print(not(log2 < log1)) # not only starts a statement
print((log1 > log2) or (log2 < log1)) # or works when all the statements are false

print(True and True)
print(True and False)
print(True or False) # one the statement has to be true
print(True or True)
print(not True)
print(False or False)

# Membership Operators (in, not in)
numbers = (20, 30, 40, 50)
print(20 in numbers)
print(20 not in numbers)

name = "Madrine"
print("a" not in name)
print("A" not in name)

# Identity Operators (is, is not )
print(20 is not numbers)
print(20 is 20)
