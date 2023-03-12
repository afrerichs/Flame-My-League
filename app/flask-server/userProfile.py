#.\venv\Scripts\activate
from ProfileProcessor.main import main
 
class userProfile:
    def __init__(self):
        self.name = ''

    def getName(self):
        return self.name


    def setName(self, name):
        self.name = name




    def startProcess(self):
        calc = main(self.name)
        if(calc.validate()):
            print('Valid name')
            calc.run()
            return calc.startFlame()
        else:
            print('Invalid name')
            return ['No summoner found']





