import re


# Flame for name like M 0 N 0 T 0 N E (Spaces = Letters)
class nameResponse:

    def __init__(self, name):
        self.name = name

        self.numbersMatch = '\d+' 
        self.threePlusSpacesMatch = '\s.*\s.*\s'    
        self.longNameMatch = '\w{14,}' 
        self.startsEndsXMatch = '^[xX].*[xX]$' 
        self.shortNameMatch = '^\w{1,4}$'
        self.allCapsMatch = '^[A-Z]+$'
        self.hasSpacesMatch = '\s'
        self.noCapsMatch = '^[a-z]+$'

        

        



    def start(self):
        numbersMatch = re.search(self.numbersMatch, self.name)
        threePlusSpacesMatch = re.search(self.threePlusSpacesMatch, self.name)
        longNameMatch = re.search(self.longNameMatch, self.name)
        startsEndsXMatch = re.search(self.startsEndsXMatch, self.name)
        shortNameMatch = re.search(self.shortNameMatch, self.name)
        allCapsMatch = re.search(self.allCapsMatch, self.name)
        hasSpacesMatch = re.search(self.hasSpacesMatch, self.name)
        noCapsMatch = re.search(self.noCapsMatch, self.name)
        
        
        if(threePlusSpacesMatch):   #   Stay In The X       
            returnString = "Why not make your username an entire sentence while you're at it."
        elif(startsEndsXMatch):     #   xX_Jhin_Xx
            returnString = "Did you make that when you were twelve?"
        elif(allCapsMatch):         #   GIZMO
            returnString = 'IS YOUR CAPS STUCK ON?.'
        elif(shortNameMatch):       #   1X2
            returnString = 'Too illiterate to type any more than 4 letters?'
        elif(longNameMatch and not (hasSpacesMatch)):       #ILoveThickThighs
            returnString = "Let me guess... wouldn't fit with spaces?"
        elif(noCapsMatch):          #logic 
            returnString = "Ever heard of capitalization?."
        elif(numbersMatch):         #IMMORTAL KING19
            returnString = "Couldn't get the name without numbers?"
        else:           
            returnString = 'Did your grandma make that name for you?'

        return returnString

            
        
        



    

    