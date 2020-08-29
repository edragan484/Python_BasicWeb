
def Funccia (a,b):
    return a+b
x = Funccia (2,8)
y = Funccia (x,10)
print(y)


a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)


def h():
  print(12)

def f():
  g(h)

def g(a):
  a()

g(f)
