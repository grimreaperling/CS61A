class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work!'
    def __repr__(self):
        return Bourgeoisie.greeting
    
class Bourgeoisie(Worker):
    greeting = 'Peno'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'
