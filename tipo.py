
# Classe Animal
class Animal:
    def fazer_som(self):
        pass

#Classe cachorro que Herda minha Classe animal
class Cachorro(Animal):
    def fazer_som(self):
        return "au au!"

#Classe gato que Herda minha Classe animal
class Gato(Animal):
    def fazer_som(self):
        return "Miau!!"
        
# A classe polimofica
class Fazer_barulho:
    def fazer_barulho(self, animal: Animal):
        return animal.fazer_som()

som = Gato()

print(som.fazer_som())
