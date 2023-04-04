class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        prime_factors = []
        prime = 2
        while prime*prime<=n:
            while n%prime==0:
                prime_factors.append(prime)
                n//=prime
            prime+=1
        if n>1:
            prime_factors.append(n)
        return sum(prime_factors)
