


class rankedResponse:
    def __init__(self, rankedData):
        self.rankedData = rankedData
        self.lowRanked = ['IRON', 'BRONZE', 'SILVER']
        self.midRanked = ['GOLD', 'PLATINUM', 'DIAMOND']
        self.highRanked = ['MASTER', 'GRANDMASTER', 'CHALLENGER']

        self.fewGames = 20
        self.midGames = 150
        

    def start(self):

        if len(self.rankedData) == 1:
            print(self.noRank())
            return self.noRank()
        #Check for ranked data first

        return [self.getRank(), self.getDiv(), self.getWR(), self.getGames()]
        #rankFlame = self.getRank()
        #wrFlame = self.getWR()
        #gamesFlame = self.getGames()


    def getWR(self):
        return int(self.rankedData[2])

    
        if int(self.rankedData[2]) < 50:
            yourWR = 'Negative WR'
        elif int(self.rankedData[2]) == 50:
            yourWR = 'Even WR'
        else:
            yourWR = 'Positive WR'
        print(yourWR)
        return yourWR

    def getGames(self):
        print("RankedData:")
        print(self.rankedData)
        return self.rankedData[3]

        games = self.rankedData[3]
        if int(games) < 30:
            yourGames = 'Low games'
        elif int(games) >= 30 and int(games) <= 150:
            yourGames = 'Average num games'
        else:
            yourGames = 'Lots of games'
        print(yourGames)
        return yourGames
    def getDiv(self):
        return self.rankedData[1]

    def getRank(self):
        return self.rankedData[0]

        if len(self.rankedData) == 1:
            print(self.noRank())
            return self.noRank()
        #Check for ranked data first


        for i in range(len(self.lowRanked)):
            if self.lowRanked[i] == self.rankedData[0]:
                yourRank = "Talk about pisslow."
        for i in range(len(self.midRanked)):
            if self.midRanked[i] == self.rankedData[0]:
                yourRank = "I hope you don't think you're good."
        for i in range(len(self.highRanked)):
            if self.highRanked[i] == self.rankedData[0]:
                yourRank = "Do you touch grass?"

        print(yourRank)
        return yourRank




    def noRank(self):
        return ['Too insecure to play ranked?'];


