from random import uniform
from time import sleep
from threading import Thread, Lock

class Filosofo(Thread):
    def __init__(self, nome, garfo1, garfo2, index):  
        Thread.__init__(self)
        self.nome = nome
        self.garfo1 = garfo1
        self.garfo2 = garfo2
        self.index = index;

    def run(self):
        while True:
            print(f"{self.nome} -> pensando ")
            sleep(1)

            try:
                self.comer()
            except RuntimeError:
                pass
            

    def comer(self):
        while True:
            self.garfo1.acquire(True, 2)
            acquired = self.garfo2.acquire(False)

            if acquired:
                print(f"{self.nome} -> começou a comer")
                sleep(1)
                print(f"{self.nome} -> parou de comer")
                score[self.index] += 1  
                print(score)
                self.garfo1.release()  
                self.garfo2.release()
                break

            self.garfo1.release()      

score = [0, 0, 0, 0, 0]
garfos = [Lock(),Lock(),Lock(),Lock(),Lock()]

filosofo1 = Filosofo('UM', garfos[0], garfos[1], 0)
filosofo2 = Filosofo('DOIS', garfos[1], garfos[2], 1)
filosofo3 = Filosofo('TRÊS', garfos[2], garfos[3], 2)
filosofo4 = Filosofo('QUATRO', garfos[3], garfos[4],3 )
filosofo5 = Filosofo('CINCO', garfos[4], garfos[0], 4)

for _ in range(15):
    for filosofo in [
        filosofo1,
        filosofo2,
        filosofo3,
        filosofo4,
        filosofo5
    ]:
        try:
            filosofo.start()
            # sleep(1)
        except RuntimeError:
            pass
    sleep(1)
