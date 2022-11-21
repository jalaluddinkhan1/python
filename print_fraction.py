class fration:
    def __init__(self,n,d):
        self.num=n
        self.dec=d
    def __str__(self):
        return "{}/{}".format(self.num,self.dec)

n=fration(10,20)
print(n)