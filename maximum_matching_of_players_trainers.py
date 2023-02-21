class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        players_point = len(players)-1
        trainers_point = len(trainers)-1
        matching = 0
        while players_point>=0 and trainers_point>=0:
            if players[players_point]<=trainers[trainers_point]:
                matching+=1
                trainers_point-=1
                players_point-=1
            else:
                players_point-=1
        return matching

        
