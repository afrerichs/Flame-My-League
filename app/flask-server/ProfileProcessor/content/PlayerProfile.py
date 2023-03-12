class PlayerProfile:
    def __init__(self, data):
        self.id = data.get("id")
        self.accountId = data.get("accountId")
        self.puuid = data.get("puuid")
        self.name = data.get("name")
        self.profileIconId = data.get("profileIconId")
        self.revisionDate = data.get("revisionDate")
        self.summonerLevel = data.get("summonerLevel")

    
    def getId(self):
        return self.id

    def getAccountId(self):
        return self.accountId
    
    def getPuuid(self):
        return self.puuid
    
    def getName(self):
        return self.name
    
    def getProfileIconId(self):
        return self.profileIconId

    def getRevisionDate(self):
        return self.revisionDate

    def getSummonerLevel(self):
        return self.summonerLevel

    def seeMains(self):
        returnList = []


        for i in range(6):
             returnList.append(self.champList.getChampAtN(i))
        
        return returnList



    def addRank(self, rankData):
        soloData = False
        print(rankData)
        for queues in rankData:
            if queues.get('queueType') == 'RANKED_SOLO_5x5':
                self.tier = queues.get('tier')
                self.rank = queues.get('rank')

                self.totGames = queues.get('wins') + queues.get('losses')
                self.winRate = float(queues.get('wins')) / (float(queues.get('losses') + queues.get('wins')))
                self.hasSolo = True
                soloData = True
        if soloData == False:
            self.hasSolo = False
    
    def getTier(self):
        return self.tier

    def getRank(self):
        return self.rank

    def getTotGames(self):
        return self.totGames

    def getWinRate(self):
        return str(int(self.winRate * 100))

    


    def addChampList(self, champList):
        self.champList = champList
        

    def seeRanked(self):
        if(self.hasSolo):
            returnString = ("Rank: " + self.tier + " " + self.rank + " Winrate: " + str(int(self.winRate * 100)) + "% " + "over " + str(self.totGames) +" games.")
        else:
            returnString = 'No ranked data avilable'
        
        return returnString

    def hasRanked(self):
        return self.hasSolo



    





        
