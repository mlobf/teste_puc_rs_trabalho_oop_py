from src.models.pilotos import Piloto


class ServicoPilotos:
    base = {}
    contador = 0

    def new_piloto(self, lista_de_requisitos):
        """
        self.__nome = nome
        self.__matricula = matricula
        self.__habilitacao_ativa = habilitacao_ativa
        """

        pi = Piloto(*lista_de_requisitos)
        # str_uuid = str(uuid.uuid4())
        # self.base[str_uuid] = ac
        self.base[self.contador] = pi
        self.contador += 1
        return str(self.base.items())

    def show_pilotos(self):
        for key, value in self.base.items():
            print(key, value)

    def get_piloto_id(self, id):
        if self.base.get(id):
            return self.base.get(id)
