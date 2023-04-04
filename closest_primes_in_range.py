class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def primesInRange(n):
            if n <2:
                return 0
            is_prime:list[bool] = [True for _ in range(n)]
            is_prime[0]= is_prime[1]= False
            i =2
            while i*i <=n:
                if is_prime[i]:
                    j=i*i
                    while j<n:
                        is_prime[j]=False
                        j+=i
                i+=1
            primes = []
            for i in range(n):
                if is_prime[i]==True and i>=left:
                    primes.append(i)
            return primes
        primes = primesInRange(right+1)
        if len(primes)<=1:
            return [-1,-1]
        prev = primes[0]
        res = None
        closest = float('inf')
        for i in range(1,len(primes)):
            diff = primes[i]-prev
            if diff <closest:
                res = [prev,primes[i]]
                closest = diff
            prev = primes[i]
        return res
