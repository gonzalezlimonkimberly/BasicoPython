class Enemigo:
    tipo_enemigo: str
    punto_energia: int = 10
    ataque = 1

    def __init__(self, tipo_enemigo, punto_energia = 10 , ataque = 1):
       self.__tipo_enemigo = tipo_enemigo
       self.punto_energia = punto_energia
       self.ataque = ataque

    def get_tipo_enemigo(self):
        return self.__tipo_enemigo

    def habla(self):
        print(f"Yo soy {self.__tipo_enemigo}. Preparado para peleaar!!")

    def camina(self):
        print(f"{self.__tipo_enemigo} se mueve cerca de tii!!!")

    def atacar(self):
        print(f"{self.__tipo_enemigo} ataca con un {self.ataque} de daño!!")