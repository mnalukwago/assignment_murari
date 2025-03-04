# sequence
num1, num2, num3 = 100, 300, 500 # 3 memory locations
numbers = [100, 300, 500] # one memory location
numbers1 = [num1, num2, num3]
numbers2 =[]
things =[100, "Hello", 300.0, True, [1, 2, 3]]
trouble = [20, [30, [100, 20 [500]]]]
print(type(num1))
print(numbers[2])
print(things[4][2])
print(trouble[1][1][2][0])
trouble.append(40)
print(trouble)
trouble.pop()
print(trouble)

# tuple
my_tuple =(100, 300, 500)
# tuples are read only sequences

ground = ["Belinda", 5, [1, 2], [0, [True, False]]]
print(ground[0])