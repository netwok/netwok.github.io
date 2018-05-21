def sieve(lim=1000000):
    primes = [n for n in range(3,lim,2)]
    for prime in primes:
        #we don't want to bother multiplying through the numbers that we have already marked off as non-primes
        if prime > 2:
            #all primes over 2 are odd so I'm mapping indicies to numbers with n = 2i+3 (e.g. n = 3, 5, 7, etc. for i = 0, 1, 2)
            for mult in range(3,int(lim/prime)+1,2):
                #a sneaky way to make sure 2 is listed as prime, set score for non-primes as 2
                primes[int((prime*mult)/2-1.5)] = 2
    #removes all those extra 2's and condenses output to reduce space
    return [2]+[prime for prime in primes if prime != 2]

primes = sieve()
spri = set(primes)

from itertools import combinations
from itertools import combinations_with_replacement as cwr

def replacer(n):
    N = list(str(n))
    swaps = getcombs(len(N))
    for thisswap in swaps:
        N_temp = N
        reps = cwr('0123456789',len(thisswap))
        for rep in reps:
            for it,dig in enumerate(thisswap):
                N_temp[int(dig)] = rep[it]
                print(int(''.join(N_temp)))
        
        
            
    
def family():
    for prime in primes:
        pass

def getcombs(n):
    N = [i for i in range(n)]
    return [comb for r in range(1, len(N)) for comb in combinations(N,r)]
    
from time import clock   
start = clock()
print(family())
print('answer found in {} seconds'.format(clock()-start))
