
        boxes = list(boxes)
        box_len = len(boxes)
        answer = []
        
        for curr_box in range(box_len):
            
            number_of_moves =0
            for box_with_ball in range(box_len):
                
                if boxes[box_with_ball]=='1':
                    number_of_moves+=abs(curr_box-box_with_ball)
                    
            answer.append(number_of_moves)
    
        return answer
