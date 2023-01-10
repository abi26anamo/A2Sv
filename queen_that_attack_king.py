class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        queen_can_attack =[]
        queens= [(x,y) for x,y in queens]
        
     
        
        directions = {(-1,-1),(0,-1),(-1,0),(1,1),(1,0),(0,1),(1,-1),(-1,1)}
        
        for x_dir,y_dir in directions:
            
                x_king,y_king = king[0],king[1]

                while 0<=x_king+x_dir<8 >y_king+y_dir>=0:
                    x_king+=x_dir
                    y_king+=y_dir

                    if (x_king,y_king) in queens:
                        queen_can_attack+=[[x_king,y_king]]
                        break

        return queen_can_attack
