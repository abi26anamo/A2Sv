class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bit_mask_for_word = [0]*n
        for i in range(n):
            for ch in words[i]:
                bit_mask_for_word[i]|=1<<(ord(ch)-97)

        max_product = 0
        for i in range(n):
            for j in range(i+1,n):
                if bit_mask_for_word[i] & bit_mask_for_word[j]==0:
                    max_product = max(max_product,len(words[i])*len(words[j]))
        return max_product
