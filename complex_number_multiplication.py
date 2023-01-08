class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1,imaginary1= num1.split("+")
        real2,imaginary2 = num2.split("+")
        
        
        real1 = int(real1)
        real2 = int(real2)
        
        imaginary1 = int(imaginary1[:-1])
        imaginary2  = int(imaginary2[:-1])
        
        real = str((real1*real2) - (imaginary1*imaginary2))
        
        imaginary = str(real1*imaginary2 +real2*imaginary1)
        
        
    
        return real+"+"+imaginary+"i"
        
        
