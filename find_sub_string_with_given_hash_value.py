class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]

        curr_hash = 0
        m = pow(power, k - 1, modulo)
        i =0
        # Calculate the initial hash of the first substring of length k
        while i< k:
            val = ord(s[i]) - 96
            curr_hash = (curr_hash * power + val) % modulo
            i+=1

        left = 0
        right = k
        found_idx = -1

        if curr_hash == hashValue:
            found_idx = left

        while right < len(s):
            left_val = ord(s[left]) - 96
            curr_hash = ((curr_hash - left_val * m) * power + (ord(s[right]) - 96)) % modulo
            left += 1

            if curr_hash == hashValue:
                found_idx = left
            right += 1

        # Check if a match was found and return the reversed substring
        if found_idx != -1:
            return s[found_idx:found_idx + k][::-1]
