print ("Node class test")

class node:
    n=100  # define a CLASS attribute, not required to set while creating the instance
    label="node label 1"
    def __init__(self, p,q):
        self.p=p # define an Instance attribute (required to set while creating an instance)
        self.q=q # define an Instance attribute (required to set while creating an instance)
        print (p*q)
        def z():
            print("instance method")
    def y(self, c):
            print("instance method", c)

    def x(self):
         print(f"this is the node {self.n} of graph")

a=node(1,2) # the class attribute is not set so the class value is used
b=node(11,12)
# a.n=1000
b.n=2000
print("a",a.p, "b",b.p)   # -> a 1 b 11
print("a",a.q, "b",b.q)  # -> a 2 b 12
print("a",a.n, "b",b.n)  # ->a 100 b 2000

node.n=53

print(a.n)  # -> 53
print(a.label)
a.x()
a.y(34)