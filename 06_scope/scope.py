username = "rahul"

def func():
    # username = "jharwal"
    print(username)

print(username)
func()

x = 99

def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)

def func3():
    global x
    x = 88

func3()
print(x)

def f():
    x = 96
    def f1():
        print(x)
    f1()
f()

def f():
    x = 96
    def f1():
        print(x)
    return f1
myResult = f()
myResult()

def rahul(num):
    def actual(x):
        return x ** num
    return actual



s = rahul(2)
print(s(2))
print(type(s(2)))