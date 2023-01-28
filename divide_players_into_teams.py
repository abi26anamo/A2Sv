class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        chemistry = 0
        curr_sum = skill[left]+skill[right]
        
        while left<right:
            if skill[left]+skill[right]!=curr_sum:
                chemistry = 0
                break
            else:
                chemistry+=skill[left]*skill[right]
                left+=1
                right-=1

        return chemistry if chemistry>0 else -1
