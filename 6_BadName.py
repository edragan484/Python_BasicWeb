
class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name")

print(greet("Anton"))
print(greet("anton"))
