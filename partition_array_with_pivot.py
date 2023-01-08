 smaller_than_pivot = []
        larger_than_pivot =[]
        is_equal = []
        
        
        for i in range(len(nums)):
            if nums[i]>pivot:
                larger_than_pivot.append(nums[i])
            elif nums[i]<pivot:
                smaller_than_pivot.append(nums[i])
            else:
                is_equal.append(nums[i])
                
        return smaller_than_pivot +is_equal+larger_than_pivot
        
