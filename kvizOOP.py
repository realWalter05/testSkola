import random
from abc import ABC, abstractmethod


class SoutezniOtazka(ABC):
    def __init__(self, text, spravna,  benevolent):
        self.text = text
        self.spravna = spravna
        self.benevolent = benevolent

    @abstractmethod
    def je_odpoved_spravna(self):
        pass

    @abstractmethod
    def ask(self):
        pass

class JednoduchaSoutezniOtazka(SoutezniOtazka):
    def je_odpoved_spravna(self, odpoved):
        if self.benevolent:
            right = self.spravna.lower().strip()
            user = odpoved.lower().strip()
            return right == user
        return self.spravna == odpoved
    
    def ask(self):
        print(self.text)
        return(input())
        

class SoutezniOtazkaABCD(SoutezniOtazka):
    def __init__(self, text, moznosti: list, spravnaMoznost, benevolent):
        random.shuffle(moznosti)
        self.text = text
        self.moznosti = moznosti
        self.spravna = spravnaMoznost
        self.benevolent = benevolent

    def je_odpoved_spravna(self, odpoved):
        if not self.benevolent:
            if odpoved == self.spravna:
                return True
        if self.benevolent: 
            if self.spravna.lower().strip() == odpoved.lower().strip():
                return True
        if odpoved == str(self.moznosti.index(self.spravna)):
            return True
        return False

    def ask(self):
        print(self.text)
        for i, moznost in enumerate(self.moznosti):
            print(i, moznost)
        return(input())
        


otazky = [
    JednoduchaSoutezniOtazka("What is the capital of France? ", "Paris", benevolent=True),
    SoutezniOtazkaABCD("Jaký programovací jazyk kompilovaný?", ["C","Python"], "C", benevolent=True),
    JednoduchaSoutezniOtazka("What is the capital of Germany? ", "Berlin", benevolent=True),
    SoutezniOtazkaABCD("Jaký programovací jazyk interpretovaný?", ["C","Python"], "Python", benevolent=True),
    JednoduchaSoutezniOtazka("What is the capital of Italy? ", "Rome", benevolent=True),
    SoutezniOtazkaABCD("Jaký programovací jazyk je nejlepší?", ["C","Python"], "Python", benevolent=False),
    JednoduchaSoutezniOtazka("What is the capital of Spain? ", "Madrid", benevolent=False),
]

class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.score = 0

    def zvys_score(self):
        self.score += 1

    def get_score(self):
        return self.score

class Kviz:
    def __init__(self, otazky, jmeno):
        self.otazky = otazky
        self.score = 0
        self.hrac = Hrac(jmeno)

    def hra(self):
        print("Welcome to the quiz!")
        random.shuffle(self.otazky)
        for otazka in self.otazky:
            user_input = otazka.ask()
            if otazka.je_odpoved_spravna(user_input):
                print("Brilliant!!!!!")
                self.score += 1
            else:
                print("nope, the answer is: ", otazka.spravna)
        
        self.vysledek()
        
    def vysledek(self):
        print(self.hrac.jmeno + ", your score is: ", self.score, "out of", len(otazky))

kviz = Kviz(otazky, "Karel")
kviz.hra()

    