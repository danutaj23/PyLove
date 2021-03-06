# Stwórz konstruktor (__init__) dla klasy "Człowiek",
# który oprócz imienia pobierze też wzrost i wagę.

class Czlowiek:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def speak(self):
        print('Mowie prawdę')

    def count_bmi(self):
        pass

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass


class Polityk(Czlowiek):
    bribed = False

    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print('Kłamie, bo mogę')

    def recive_bribe(self):
        self.bribed = True


adam = Czlowiek('Adam', 180, 120)
ewa = Czlowiek('Ewa', 165, 60)

print(adam.wzrost)
print(adam.waga)
print(ewa.wzrost)
print(ewa.waga)

