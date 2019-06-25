# Useful links

[**Karatsuba algorithm** _From Wikipedia, the free encyclopedia_](https://en.wikipedia.org/wiki/Karatsuba_algorithm)

[Karatsuba](https://www.coursera.org/learn/algorithms-divide-conquer/discussions/weeks/1/threads/u0erE0bpEee28BJbhmSN2A)

[Karatsuba’s Algorithm](https://courses.csail.mit.edu/6.006/spring11/exams/notes3-karatsuba)

## Another Karatsuba Algorithm Implementation:

[Karatsuba Multiplication Algorithm – Python Code](https://pythonandr.com/2015/10/13/karatsuba-multiplication-algorithm-python-code/)
courtesy of [Murat Serdar Alperen](https://repl.it/repls/IntentionalConfusedScarab)

```python
from math import *


x = int(input('Enter your digits ? : ))
y = int(input('Enter your digits ? : '))

def karatsuba(x,y):
    # Set B = 10
    B = 10

    # Recursion base case
    if x < 10 or y < 10:
        return x*y

    # m set to be length of x or y, whichever is maximum
    # This can be done using logarithms with base 10 or alternatively,
    # m = max(len(str(x)), len(str(y)))
    # But such a method will be inefficient for very large n
    m = max(int(log10(x)+1), int(log10(y)+1))

    # check whether m is even. If odd, set m lower by 1
    if m % 2 != 0:
        m -= 1
    m_2 = int(m/2)

    a, b = divmod(x, B**m_2)
    c, d = divmod(y, B**m_2)

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d)) - ac - bd

    return ((ac*(10**m)) + bd + ((ad_bc)*(10**m_2)))

s = str(karatsuba(x,y))
print (s)
```

## Master theorem

[Master theorem - _From University of North Texas_](http://www.cse.unt.edu/~tarau/teaching/cf1/Master%20theorem.pdf)

[Stackexchange Master theorem](https://math.stackexchange.com/questions/538268/can-you-help-me-to-solve-the-recurrence-relation-tn-t-sqrt-n-1)
