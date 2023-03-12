

class ChampList:
    def __init__(self, topChamps, champList, translator):
        self.topChamps = topChamps

        self.champList = champList
        self.champTranslate = translator
        
    def getChampAtN(self, n):
        try:
            return self.champTranslate.getNameFromID(self.topChamps[n].get('championId'))    
        except:
            return ''

    def getIdFromChamp(self, champName):
        return self.champTranslate.getIDFromName(champName)
        

