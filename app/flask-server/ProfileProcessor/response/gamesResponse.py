class gamesResponse:
    def __init__(self, data):
        self.gamesData = data[0] #Array of game data, [[Kills, deaths, assists, cs, champ, duration], []]
        self.lossStreak = data[1] #Int of longest loss streak
        self.streakStart = data[2] #Index of first game in loss streak
        self.streakEnd = data[3]    #Index of last game in loss streak

    

    def start(self):
        print(self.gamesData)
        #Finds worst game in gamesData weighing kills, assists, and deaths.
        #Score = (Kills * 2 + Assists) / (Deaths * 2)
        worstScore = 99999999999
        worstScoreIndex = 0
        print(self.gamesData)
        for gameIndex in range(len(self.gamesData)):
            killScore = self.gamesData[gameIndex][0] * 2
            posScore = killScore + self.gamesData[gameIndex][2]
            score = posScore / (self.gamesData[gameIndex][1] * 2)
            if score < worstScore:
                worstScoreIndex = gameIndex
        worstGame = self.gamesData[worstScoreIndex]

        #Creates new array of loss streak games
        lossStreakGames = []
        for gameNum in range(self.streakStart, self.streakEnd + 1):
            lossStreakGames.append(self.gamesData[gameNum])


        return [worstGame, lossStreakGames]


        
        
    
