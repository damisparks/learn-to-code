
'''
->> implement one or more of the integer multiplication algorithms

Constraint: 
->> restrict itself to multiplying only pairs of single-digit numbers. e.g grade-school algorithm. 
->> to get the most of this,  implement recursive integer multiplication and/or Karatsuba's algorithm.

Test Case: 
--> So: what's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627
'''


def makeKaratsuba(a, b):
    """Functions takes two inputs, 
    --> This is the working with int version. 
    --> a & b
    --> where both are digits 
    """
    a = int(a)
    b = int(b)
    if len(str(a)) == 1 or len(str(b)) == 1:
        return a*b

    else:
        maxOfBothLength = max(len(str(a)), len(str(b)))
        splitInputIntoTwo = maxOfBothLength / 2

        w = a / 10 ** (splitInputIntoTwo)
        x = a % 10 ** (splitInputIntoTwo)
        y = a / 10 ** (splitInputIntoTwo)
        z = a % 10 ** (splitInputIntoTwo)

        wy = makeKaratsuba(w, y)
        xz = makeKaratsuba(x, z)
        add_wxyz = makeKaratsuba(w+x, y+z) - wy - xz

        result = wy * 10 ** (2*splitInputIntoTwo) + \
            (add_wxyz * 10 ** splitInputIntoTwo) + xz

        return result


a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
print(makeKaratsuba(a, b))
