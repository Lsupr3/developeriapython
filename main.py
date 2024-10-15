class Participant:
    def __init__(self, name):
        self.points = 0
        self.choice = ""
        self.name = name
    
    def isChooseRight(self, choice):
        return choice in "rock, paper, scissor"
    
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        if self.isChooseRight(self.choice):
            print("{name} selects {choice}".format(name=self.name, choice = self.choice))
        else:
            print("eleccion no valida")

class GameRound:
    def __ini__(self):
        self.winner



class Game:
    def __init__(self, name1, name2):
        self.isNotGameOver = True
        self.participant = Participant(name1)
        self.secondParticipant = Participant(name2)

        while self.isNotGameOver:
            self.participant.choose()
            self.secondParticipant.choose()
            

game = Game("Juanito", "Pepita")