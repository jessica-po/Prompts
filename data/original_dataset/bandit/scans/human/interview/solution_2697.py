# cook your dish here
try:
    def isPrime(n): 
          
        # Corner case 
        if n <= 1 : 
            return False
      
        # check from 2 to n-1 
        for i in range(2, n): 
            if n % i == 0: 
                return False
      
        return True
      
    # Function to print primes 
    def printPrime(n): 
        count = 0
        for i in range(2, n + 1): 
            if isPrime(i): 
                count = count+1 
        print(count)
      
    n = int(input())
    printPrime(n)
except:
    pass