# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Smallest product of two 3 digit #s is 100*100 = 10,000
# Largest product of two 3 digit #s is 999*999 = 998,001

def find_factors(num):
    x=1
    y=num
    fac = []
    while (x < y):
        if (num%x == 0):
            #add first factor
            fac.append(x)
            y=num/x
            #add second factor
            fac.append(y)
        x=x+1
    return fac

def find_palindrome(text):
    t = list(text)
    length = len(t)
    while (x < length)
        while (y >)
   
    return max(prime)

def main():
    
    print "Finding the largest palindrome made from the product of two 3-digit numbers."
    find_palindrome(101)
#    for x in range (10000,998001)
#        if (find_palindrome() (int(x)))
#            prime = find_factors(factors)
#    print prime


if __name__ == "__main__":
    main()