class Participant:
    def __init__(self, name):
        self.choiceValue = 0
        self.choice = ""
        self.name = name
    
    def isChooseRight(self, choice):
        return choice.lower() in "rock, paper, scissor"
    
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        if self.isChooseRight(self.choice):
            self.choiceValue = self.toNumericalChoice(self.choice)
        else:
            print("eleccion no valida")
        return self.choice.lower()
    
    def toNumericalChoice(self, choice):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]     

class GameRound:  
    def __init__(self, persona1, persona2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        self.participant = persona1
        self.participant1 = persona2 
        self.compareChoices(self.participant, self.participant1)
             
    def compareChoices(self, participant, participant1):
        self.participant.choose()
        self.participant1.choose()
        self.rules[self.participant.choiceValue][self.participant1.choiceValue]



class Game:
    def __init__(self, name1, name2):
        self.isNotGameOver = True
        self.participant = Participant(name1)
        self.participant1 = Participant(name2)

        while self.isNotGameOver:
            GameRound(self.participant, self.participant1)
                        

game = Game("Juanito", "Pepita")