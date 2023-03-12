class Translator:
    def __init__(self, staticList):
        #Establish champ translation
        self.staticList = staticList
        #print(staticList['data']['Aatrox'].get('key'))

        #Keys: type, format, version, data
        champ_dict = {}
        for key in staticList['data']:
            row = staticList['data'][key]
            champ_dict[row['key']] = row['id']
        self.dict = champ_dict
        #print(self.dict.values())


    def getNameFromID(self, id):
        return self.dict.get(str(id))

    def getIDFromName(self, name):
        return self.staticList['data'][str(name)].get('key')
