import numpy as np
from sqlalchemy import null


class mainsResponse:
    def __init__(self, mains):
        self.mains = mains

        self.cringeMains = np.array(['Alistar', 'Anivia', 'Bard', 'Blitzcrank', 'Cassiopeia', 'Ekko', 'Diana', 'Ezreal', 'Gragas', 'Illaoi', 'Janna', 'JarvanIV', 'Jinx', 'Karma', 'LeBlanc', 'Lillia', 'MissFortune', 'Morgana', 'Neeko', 'Rell', 'RentaGlasc', 'Ryze', 'Seraphine', 'Shyvanna', 'Sivir', 'Soraka', 'Syndra', 'Tristana', 'Vex', 'XinZhao', 'Yorick', 'Yuumi', 'Zeri', 'Zilean', 'Zoe'])
        self.edgyMains = np.array(['Akali', 'Aphelios', 'Evelynn', 'Kayn', 'Khazix', 'Nocturne', 'Pyke', 'Viego', 'Zed'])
        self.toxicMains = np.array(['Aatrox', 'Annie', 'Brand', 'Camille', 'Darius', 'Draven', 'Fiora', 'Fizz', 'Gangplank', 'Graves', 'Jax', 'Kassadin', 'Katarina', 'Kled', 'Lissandra', 'Lulu', 'MasterYi', 'Olaf', 'Pantheon', 'Qiyana', 'Quinn', 'RekSai', 'Renekton', 'Rengar', 'Riven', 'Samira', 'Shaco', 'Sion', 'Swain', 'Sylas', 'Talon', 'Teemo', 'Twitch', 'Urgot', 'Vayne', 'Vladimir', 'Volibear', 'Xerath', 'Yasuo', 'Yone', 'Zyra']) 
        self.basicMains = np.array(['Ahri', 'Ashe', 'Caitlyn', 'Irelia', 'Jhin', 'Kaisa', 'LeeSin', 'Lux', 'Mordekaiser', 'Nautilus', 'Ornn', 'Senna', 'Sett', 'Sona', 'Thresh', 'Velkoz'])
        self.brainDeadMains = np.array(['Amumu', 'Chogath', 'DrMundo', 'Hecarim', 'Heimerdinger', 'Garen', 'Jayce', 'Karthus', 'Kayle', 'Kennen', 'Leona', 'Malphite', 'Nasus', 'Poppy', 'Rammus', 'Rumble', 'Singed', 'Trundle', 'Tryndamere', 'Udyr', 'Veigar', 'Warwick', 'Wukong'])
        self.acceptableMains = np.array(['Akshan', 'AurelionSol', 'Azir', 'Belveth', 'Corki', 'Braum', 'Elise', 'Fiddlesticks', 'Galio', 'Gnar', 'Gwen', 'Ivern', 'Kalista', 'Kindred', 'Kogmaw', 'Lucian', 'Nami', 'Nidalee', 'Nunu', 'Orianna', 'Rakan', 'Sejuani', 'Shen', 'Skarner', 'TahmKench', 'Taliyah', 'Taric', 'TwistedFate', 'Varus', 'Vi', 'Viktor', 'Xayah', 'Zac', 'Ziggs'])
        


    def start(self):
        i = 0
        cringe = 0
        edgy = 0
        toxic = 0
        basic = 0
        braindead = 0
        valid = 0

        cringeChamps = []
        edgyChamps = []
        toxicChamps = []
        basicChamps = []
        braindeadChamps = []
        validChamps = []



        while i < len(self.mains):
            currMain = self.mains[i]
            if(currMain in self.cringeMains):
                cringe += 1
                cringeChamps.append(currMain)
            elif(currMain in self.edgyMains):
                edgy += 1
                edgyChamps.append(currMain)
            elif(currMain in self.toxicMains):
                toxic += 1
                toxicChamps.append(currMain)
            elif(currMain in self.basicMains):
                basic += 1
                basicChamps.append(currMain)
            elif(currMain in self.brainDeadMains):
                braindead += 1
                braindeadChamps.append(currMain)
            elif(currMain in self.acceptableMains):
                valid += 1
                validChamps.append(currMain)
            else:
                print('ERROR READING' + currMain)
            i += 1

        cringePercent = (cringe / i) * 100
        edgyPercent = (edgy / i) * 100
        toxicPercent = (toxic / i) * 100
        basicPercent = (basic / i) * 100
        braindeadPercent = (braindead / i) * 100
        validPercent = (valid / i) * 100

        champsArr = [cringeChamps, edgyChamps, toxicChamps, basicChamps, braindeadChamps, validChamps]

        array = [cringePercent, edgyPercent, toxicPercent, basicPercent, braindeadPercent, validPercent, champsArr]
        print(array)
        return array


        #
        
