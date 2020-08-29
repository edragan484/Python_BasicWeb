print("Task 1-----DATA-TYPES")
print("Hello, world!")

a = 3
print(a)

str = "Hello world"
print(str)

b, c, d = 5, 6.4, "Great"

# print("Value is" + b) #is not correct

print("{} {}".format("Value is", b))

print("Task 2-----TYPES")

print(type(b))
print(type(c))
print(type(d))

print("Task 3-----LIST")

values = [1, 2, "rahul", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0])  # 1
print(values[3])  # 4
print(values[-1])  # 5
print(values[1:3])  # 2 rahul
values.insert(3, "shetty")  # to insert
print(values)

values.append("End")  # to add in the end
print(values)

values[2] = "RAHUL" # Updating

del values[0]  # Deleting item in index 0

print(values)


print("Task 4-----")

# Tuple - Same as LIST Data type but immutable
val = (1, 2, "rahul", 4.5)
print(val[1])

# val[2] = "RAHUL" - is not correct

print(val)

print("Task-----DICTIONARY")

# a simple dictionary variable

a = {1: "first name", 2: "last name", "age": 33}

# print value having key=1
print(a[1])

# print value having key=2
print(a[2])

# print value having key="age"
print(a["age"])

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello world"}
print(dic[4])
print(dic["c"])

#
dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
dict["gender"] = "Male"

print(dict)
print(dict["lastname"])












