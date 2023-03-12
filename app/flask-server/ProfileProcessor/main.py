from ProfileProcessor.content.ChampList import ChampList
from ProfileProcessor.content.PlayerProfile import PlayerProfile
from ProfileProcessor.content.Translator import Translator

from ProfileProcessor.response.nameResponse import nameResponse
from ProfileProcessor.response.mainsResponse import mainsResponse
from ProfileProcessor.response.rankedResponse import rankedResponse
from ProfileProcessor.response.gamesResponse import gamesResponse

from riotwatcher import LolWatcher, ApiError

class main:
    def __init__(self, name):
        self.myName = name


    def validate(self):

        lol_watcher = LolWatcher('RGAPI-e7c1910d-0bc7-4b7b-b7be-bec96285118a') #API Key
        my_region = 'na1' #Region

        valid = True

        try:
            api = lol_watcher.summoner.by_name(my_region, self.myName)
        except:
            valid = False

        print(valid)

        return valid


    def run(self):

        sumName = self.myName

        lol_watcher = LolWatcher('RGAPI-e7c1910d-0bc7-4b7b-b7be-bec96285118a') #API Key
        my_region = 'na1' #Region
        latest = lol_watcher.data_dragon.versions_for_region(my_region)['n']['champion']
        staticChampList = lol_watcher.data_dragon.champions(latest, False, 'en_US')
        champTranslate = Translator(staticChampList)


        #sumName = "The Payload"


        api = lol_watcher.summoner.by_name(my_region, sumName)
        



        playerData = PlayerProfile(api)
        sumName = playerData.getName()
        self.myName = sumName
        

        try:
            topChamps = lol_watcher.champion_mastery.by_summoner(my_region, playerData.getId())
            champList = ChampList(topChamps, staticChampList, champTranslate)
            playerData.addChampList(champList)
        except:
            print('Not enough data')
            return ['Not enough data', '']

        self.mains = playerData.seeMains()   #Returns an array of top 10 champs


        


        rankData = lol_watcher.league.by_summoner(my_region, playerData.getId())
        playerData.addRank(rankData)

        if(playerData.hasRanked()):
            #Grab ranked data
            #self.rankedData = playerData.seeRanked()
            self.rankedData = [playerData.getTier(), playerData.getRank(), playerData.getWinRate(), playerData.getTotGames()]
            #Indexes: 0 = rank, 1 = tier, 2 = WR, 3 = total games
        else:
            self.rankedData = ['No ranked data available']

        
        #Grab match history up to past 10 games by match ID
        gameDataArrID = lol_watcher.match.matchlist_by_puuid(my_region, playerData.getPuuid(), 0, 10)

        #Big array of match details per game


        #gameData = [Arr of lost games][Kills, deaths, assists, CS, Champ]
        gameData = []
        matchIndex = 0
        lossStreak = 0
        currStreak = 0
        lastLoss = -1
        for gameNum in gameDataArrID:
            currGame = lol_watcher.match.by_id(my_region, gameNum)
            playerList = currGame.get("metadata").get("participants")
            
            #Finds index of which player number you are
            for i in range(len(playerList)):
                if playerList[i] == playerData.getPuuid():
                    currPlayerNum = i
                    break
            
            #If you lost the game, appends to game data and checks for loss streak
            if currGame.get("info").get("participants")[currPlayerNum].get("win") == False:
                if currStreak == 0:
                    lastLoss = matchIndex
                    currStreak = 1

                elif matchIndex == lastLoss + 1:
                    currStreak += 1
                    lastLoss = matchIndex
                    

                if currStreak > lossStreak:
                    lossStreak = currStreak
                    startStreak = len(gameData) - lossStreak + 1
                    endStreak = len(gameData)



                curKills = currGame.get("info").get("participants")[currPlayerNum].get("kills")
                curDeaths = currGame.get("info").get("participants")[currPlayerNum].get("deaths")
                curAssists = currGame.get("info").get("participants")[currPlayerNum].get("assists")
                curLaneCS = currGame.get("info").get("participants")[currPlayerNum].get("totalMinionsKilled")
                curJgCs = currGame.get("info").get("participants")[currPlayerNum].get("neutralMinionsKilled")
                curCS = curLaneCS + curJgCs
                curChamp = currGame.get("info").get("participants")[currPlayerNum].get("championName")
                duration = currGame.get("info").get("gameDuration")

                gameData.append([curKills, curDeaths, curAssists, curCS, curChamp, duration])

 
            else:
                currStreak = 0

            matchIndex += 1

        #Game data finds losses in past 10 games
        #lossStreak counts largest loss streak in 10 games
        #startStreak is index of gameData of where loss streak starts
        #endStreak is index of gameData where loss streak ends
        print(len(gameData))
        print(lossStreak)
        print(startStreak)
        print(endStreak)
        print(gameData)

        returnGameData = [gameData, lossStreak, startStreak, endStreak]


        self.gameData = returnGameData









        self.returnData = [self.mains, self.rankedData, self.gameData]    

    def getData(self):
        return self.returnData 

    def startFlame(self):
        responseName = nameResponse(self.myName)
        #nameFlame = self.myName + '? ' + responseName.start()



        responseMains = mainsResponse(self.mains)   

        

        responseRanked = rankedResponse(self.rankedData) 

        responseGames = gamesResponse(self.gameData)

    

           


        array = [self.myName, responseName.start(), responseMains.start(), responseRanked.start(), responseGames.start()]
        print(array)   #[Name flame, [Main Percentages], [Elo, WR, Games], [Worst Game, [Loss Streak Games]]]
        return array
        







        #playerData.seeMains(champList)
        #playerData.seeRanked()
















        #if name == "__main__":
        #    main()






        #me = lol_watcher.summoner.by_name(my_region, 'The Payload')
        #print(me)

        # all objects are returned (by default) as a dict
        # lets see if i got diamond yet (i probably didnt)
        #my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
        #print(my_ranked_stats)

        # First we get the latest version of the game from data dragon
        #versions = lol_watcher.data_dragon.versions_for_region(my_region)
        #champions_version = versions['n']['champion']

        # Lets get some champions
        #current_champ_list = lol_watcher.data_dragon.champions(champions_version)
        #print(current_champ_list)

        # For Riot's API, the 404 status code indicates that the requested data wasn't found and
        # should be expected to occur in normal operation, as in the case of a an
        # invalid summoner name, match ID, etc.
        #
        # The 429 status code indicates that the user has sent too many requests
        # in a given amount of time ("rate limiting").

        #
        #try:
        #   response = lol_watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
        #except ApiError as err:
        #    if err.response.status_code == 429:
        #       print('We should retry in {} seconds.'.format(err.headers['Retry-After']))
        #      print('this retry-after is handled by default by the RiotWatcher library')
        #     print('future requests wait until the retry-after time passes')
            #elif err.response.status_code == 404:
            #   print('Summoner with that ridiculous name not found.')
            #else:
            #   raise