class Aeronaves:
    """Classe base para aeronaves."""

    def __init__(
        self, tipo: str, prefixo: str, velocidade_cruzeiro: float, autonomia: float
    ):
        self._tipo: str = tipo
        self._prefixo: str = prefixo
        self._velocidade_cruzeiro: float = velocidade_cruzeiro
        self._autonomia: float = autonomia

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, new_tipo: str) -> None:
        self._tipo = new_tipo

    @property
    def prefixo(self) -> str:
        return self._prefixo

    @prefixo.setter
    def prefixo(self, new_prefixo: str) -> None:
        self._prefixo = new_prefixo

    @property
    def velocidade_cruzeiro(self) -> float:
        return self._velocidade_cruzeiro

    @velocidade_cruzeiro.setter
    def velocidade_cruzeiro(self, new_velocidade_cruzeiro: float) -> None:
        self._velocidade_cruzeiro = new_velocidade_cruzeiro

    @property
    def autonomia(self):
        return self._autonomia

    @autonomia.setter
    def autonomia(self, new_autonomia):
        self._autonomia = new_autonomia

    def __str__(self):
        return (
            f"{self.tipo}, {self.prefixo}, {self.velocidade_cruzeiro}, {self.autonomia}"
        )


class AeronaveParticular(Aeronaves):
    """Classe para aeronaves particulares."""

    responsavel_manutencao: str


class AeronaveComercial(Aeronaves):
    """Classe para aeronaves particulares."""

    nome_da_cia: str


class AeronavePassageiros(AeronaveComercial):
    """Classe para aeronaves particulares."""

    max_de_passageiros: int


class AeronaveCarga(AeronaveComercial):
    """Classe para aeronaves particulares."""

    max_de_carga: int


aeronave = Aeronaves("Aeronave", "Ptx 9090", 400, 800)
