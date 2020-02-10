import math

def PrimeList(n):

    primes = [i for i in range(2,n+1)]
    bool_primes = [True]*(n-1)
    print(primes)

    def Isprime(a):

        for i in range(1,int(math.sqrt(a))):
            if a%i==0:
                return False
        return True

    for i in primes:

        if Isprime(i):
            j=2
            while j*i<n-1:

                print(i,j,i*j)
                bool_primes[i*j]= False
                j=j+1

    for i,j in zip(primes,bool_primes):
        if j==False:
            primes[i]=0

    return primes


print(PrimeList(9))