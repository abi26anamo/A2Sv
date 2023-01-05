     answer =[]
        even_sum =0
        
        for index in range(len(nums)):
            
            if nums[index]%2==0:
                even_sum+=nums[index]

        
        for query in queries:
            
            if nums[query[1]]%2!=0:
                
                nums[query[1]]+=query[0]
                
                if nums[query[1]]%2==0:
                    
                    even_sum+=nums[query[1]]
                    
            elif nums[query[1]]%2==0:
                
                temp = nums[query[1]]
                nums[query[1]]+=query[0]
                
                if nums[query[1]]%2!=0:
                    even_sum-=temp
                    
                else:
                    even_sum+=nums[query[1]]
                    even_sum-=temp

            answer.append(even_sum)
        return answer
