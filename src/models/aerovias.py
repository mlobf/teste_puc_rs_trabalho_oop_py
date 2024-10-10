class Aerovias:

    def __init__(
        self, identificador, aeroporto_origem, aeroporto_destino, tamanho_aerovia
    ) -> None:
        self.__identificador = identificador
        self.__aeroporto_origem = aeroporto_origem
        self.__aeroporto_destino = aeroporto_destino
        self.__tamanho_aerovia = tamanho_aerovia

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, new_identificador):
        self.__identificador = new_identificador

    @property
    def aeroporto_origem(self):
        return self.__aeroporto_origem

    @aeroporto_origem.setter
    def aeroporto_origem(self, new_aeroporto_origem):
        self.__aeroporto_origem = new_aeroporto_origem

    @property
    def aeroporto_destino(self):
        return self.__aeroporto_destino

    @aeroporto_destino.setter
    def aeroporto_destino(self, new_aeroporto_destino):
        self.__aeroporto_destino = new_aeroporto_destino

    @property
    def tamanho_aerovia(self):
        return self.__tamanho_aerovia

    @tamanho_aerovia.setter
    def tamanho_aerovia(self, new_tamanho_aerovia):
        self.__tamanho_aerovia = new_tamanho_aerovia

    def __str__(self) -> str:
        return f"O identificador é {self.identificador},\n o aeroporto de origem é {self.aeroporto_origem},\n o aeroporto de destino é{self.aeroporto_destino}\n o tamanho da aerovia é {self.tamanho_aerovia}"




