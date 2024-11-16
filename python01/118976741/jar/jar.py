class Jar:
    def __init__(self, capacity=12):
        if int(capacity)<0:
            raise ValueError
        self._capacity=capacity
        self._size=0

    def __str__(self):

        return self._size *'🍪'

    def deposit(self, n):
        if (n>self._capacity) :

            raise ValueError("exceed capacity")
        if self._size + n > self._capacity:
             raise ValueError("exceed capacity")

        else:
           self._size += n





    def withdraw(self, n):
        if self.size<n:
            raise ValueError('no more cookies')
        else :
            self._size-=n



    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
jar=Jar()
jar.deposit(5)
jar.withdraw(1)
print(jar)
