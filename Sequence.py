def fibonacci(n):
  if n <= 0:
    raise ValueError("Invalid Input")
  else:
    fib = [0, 1]
    for i in range(1,n-1):
      fib.append(fib[-2]+fib[-1])
    return fib
    
class Triangular:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def sequence(self):
        l = []
        for i in range(1, self.number + 1):
            t = i * (i + 1) // 2
            l.append(t)
        return l

    def number_value(self):
        return self.number * (self.number + 1) // 2

class primeseq:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def primeorder(self):
        prime_no = []

        for i in range(2, self.number + 1):
            factor = []

            for j in range(1, i + 1):
                if i % j == 0:
                    factor.append(j)

            if len(factor) == 2:
                prime_no.append(i)

        return prime_no
    def primefinder(self,place):
        List = self.primeorder()
        if place <= 0 or place>len(List):
            raise ValueError("Invalid position")
        else:
            pos = place - 1
            num = List[pos]
        return num
        
class Powerseq:
    def __init__(self,base,power):
        self.base = base
        self.power = power
    def powerOrder(self):
        num = self.base
        exp = self.power
        series = []
        for i in range(1,num+1):
            series.append(i**exp)
        return series
    def powerFind(self,index):
        expo_list = self.powerOrder()
        if index <= 0 or index>len(expo_list):
            raise ValueError("Invalid position")
        else:
            pos = index - 1
            num = expo_list[pos]
        return num
        
if __name__=="__main__":
    print(fibonacci(8))

    t = Triangular("Triangle", 20)
    print(t.sequence())
    print(t.number_value())

    p = primeseq("Prime", 100)
    print(p.primeorder())
    print(p.primefinder(9))

    e = Powerseq(100,1)
    print(e.powerOrder())
    print(e.powerFind(3))                    
                       
                    
