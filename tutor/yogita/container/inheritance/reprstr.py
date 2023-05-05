class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __repr__(self):
        return "retional (%s,%s)" % (self.real, self.imag)
    def __str__(self):
        return "%s + %sj" % (self.real, self.imag)
obj = complex(10,20)
print(str(obj))
print(repr(obj))
