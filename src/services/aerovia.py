from src.models.aerovias import Aerovias


class ServicoAerovias:
    base = {}
    contador = 0

    def new_aerovia(self, lista_de_requisitos):

        aerovia = Aerovias(*lista_de_requisitos)
        self.base[self.contador] = aerovia
        self.contador += 1
        return str(self.base.items())

    def show_aerovias(self):
        for key, value in self.base.items():
            print(key, value)

    def get_aerovias_id(self, id):
        if self.base.get(id):
            return self.base.get(id)
