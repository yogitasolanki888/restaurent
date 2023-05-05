# x = 5
# print(x)  # 5      x = 8
                    #y = 7
                     #kl = function


                       #5
                       #6
                       #9
                       #None
                       #8
# y = 7

# x = 6
# print(x)  # 6


# def kl():
#     x = 10
#     print(x)  # 9
#     return 0

# x = 9
# print(kl())

# x = 8
# print(x)  # 8

# k=5
# print(k())# error int object is not callable


# class K:
#     a=5  
# l=K()
# a=dir(l)
# print(a)
# print(l) # call
# print(l())# error int object is not callable
#expl
# def nme():
#     a=5
#     return a

# a=nme()
# print(a)
 
# x="name"
# print(type(x))
# a=dir(x)
# print(a)
# x=x.islower
# print(x)

class N:
   def xl(self, ): return 5
   def yl(self, ): return 'name'
   n = 56
   d = list
   def tr(self): return dict
n=N()
# a=dir(n) # all attributes of class 
# n.d # list
# n.n #56
# n.n() # error  int object not callable 
# print(n)
# a=n.xl()
# print(a) # 5
# a=n.yl() 
# print(a) # name
# a=n.yl().islower
# print(a) # true
# a=n.yl()()
# print(a) # error str object is not collable
# 
def tr(self): return dict
x=setattr(n,"tr",tr) # n.re=45
print(dir(x))
# # print(dir(x)) 
# a=n.tr("f")()
# print(a)
# # b=n.re=45
# # print(b)
# a=getattr(n,'re')
# print(a)
kf = getattr(n,'xl')
print(kf()) # 5
