greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

a = 4

if a > 2:
    print("Good!")
else:
    print("Bad!")

print("Task 2-----LOOPS")

# for loop

obj= [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of First Natural numbers 1+2+3+4+5 = 15
# range(i, j) -> i to j-1
summation = 0
for j in range(1, 6):   # for(i=0; i<5; i++)
    summation = summation + j
print(summation)

print("*******************")
for k in range(1, 10, 2): # iteration begins from 1 each time +2 and continue till 10
    print(k)

for k in range(1, 10, 5): # iteration begins from 1 each time +2 and continue till 10
    print(k)
    print("**********SKIPPING FIRST INDEX")

for m in range(10):
    print(m)







