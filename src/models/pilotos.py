class Piloto:
    def __init__(self, nome, matricula, habilitacao_ativa) -> None:
        self.__nome = nome
        self.__matricula = matricula
        self.__habilitacao_ativa = habilitacao_ativa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_nome):
        self.__nome = new_nome

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, new_matricula):
        self.__matricula = new_matricula

    @property
    def habilitacao_ativa(self):
        return self.__habilitacao_ativa

    @habilitacao_ativa.setter
    def habilitacao_ativa(self, new_habilitacao_ativa):
        self.__habilitacao_ativa = new_habilitacao_ativa

    def __str__(self) -> str:
        return f"{self.nome}, {self.matricula}, {self.habilitacao_ativa}"
