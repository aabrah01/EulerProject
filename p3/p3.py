# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

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

def largest_prime(num):
    prime = []
    factor = []
    
    #Find prime numbers
    for x in num:
        factor = find_factors(x)
        if len(factor) == 2:
            prime.append(x)
    return max(prime)

def main():
    
    num = raw_input("Enter number to find largerst prime factor for:")
    factors = find_factors (int(num))
    prime = largest_prime(factors)
    print prime


if __name__ == "__main__":
    main()