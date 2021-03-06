# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def main():
    
    a=1
    b=1
    total=0
    even_fib=0
    
    while (even_fib < 4000000):
        total = a+b
        if (total%2 == 0):
            even_fib = even_fib+total # keep track of sum of even fibonacci numbers
        a=b
        b=total
            
    print even_fib        
if __name__ == "__main__":
    main()