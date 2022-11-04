class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")

b = B()
b.hello()

a = A()
a.hello()