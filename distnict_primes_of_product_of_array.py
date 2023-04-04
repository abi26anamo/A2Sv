class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors = set()
        for num in nums:
            prime = 2
            while prime*prime<=num:
                if num%prime==0:
                    prime_factors.add(prime)
                    while num%prime==0:
                        num//=prime
                prime+=1
            if num>1:
                prime_factors.add(num)
        return len(prime_factors)
