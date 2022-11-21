class fration: # adding two frations
    def __init__(self,n,d):
        self.num=n
        self.dec=d
    def __str__(self):
        return " xx {}/{}".format(self.num,self.dec)
    def __add__(self,ot):
        s= ot.num * self.dec + self.num * ot.dec
        d= self.dec * self.dec

        return " =>  {}/{}".format(s,d)

n=fration(10,20)
x=fration(2,5)
print(x)
print(n+x)