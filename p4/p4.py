# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009=91x99
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

# find_palindrome returns 1 if palindrome, 0 if not.
def find_palindrome(text):
    t = list(str(text))
    right = len(t) - 1
    left = 0
    
    #start at opposite ends of string
    while (right - left > 0):
        if (str(t[right]) != str(t[left])):
            right=0
            left=0
            return 0 # There was a mismatch so return 0
        #move the counters towards the center
        right=right-1
        left=left+1
    return 1
    

def main():
    
    print ("Finding the largest palindrome made from the product of two 3-digit numbers.")
    pal = {}
    #start from smallest product of two 3-digit number and go to largest
    for x in range (10000,998001):
        if (find_palindrome(x)):
             factors = find_factors(x)
             # Go through factors figure out which ones are 3-digit
             for num in factors:
                if (len(str(num)) == 3):
                    if (len(str(x/num)) == 3):
                        pal[x] = [num,x/num]
    print ("The largest palindrome made from the product of two 3-digit numbers is",max(pal, key=int),".")
    print ("Its 3-digit factors are", pal[max(pal, key=int)],".")
                        
             


if __name__ == "__main__":
    main()