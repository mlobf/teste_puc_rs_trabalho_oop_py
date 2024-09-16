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
    def autonomia(self) -> float:
        return self._autonomia

    @autonomia.setter
    def autonomia(self, new_autonomia: float) -> None:
        self._autonomia = new_autonomia

    def __str__(self):
        return (
            f"{self.tipo}, {self.prefixo}, {self.velocidade_cruzeiro}, {self.autonomia}"
        )


class AeronaveParticular(Aeronaves):
    """Classe para aeronaves particulares."""

    def __init__(
        self,
        tipo: str,
        prefixo: str,
        velocidade_cruzeiro: float,
        autonomia: float,
        responsavel_manutencao: str,
    ):
        super().__init__(tipo, prefixo, velocidade_cruzeiro, autonomia)
        self._responsavel_manutencao: str = responsavel_manutencao

    @property
    def responsavel_manutencao(self) -> str:
        return self._responsavel_manutencao

    @responsavel_manutencao.setter
    def responsavel_manutencao(self, new_responsavel_manutencao: str) -> None:
        self._responsavel_manutencao = new_responsavel_manutencao

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.responsavel_manutencao}"


class AeronaveComercial(Aeronaves):
    """Classe para aeronaves particulares."""

    nome_da_cia: str

    def __init__(
        self,
        tipo: str,
        prefixo: str,
        velocidade_cruzeiro: float,
        autonomia: float,
        nome_da_cia: str,
    ):
        super().__init__(tipo, prefixo, velocidade_cruzeiro, autonomia)
        self._nome_da_cia: str = nome_da_cia

    @property
    def nome_da_cia(self) -> str:
        return self._nome_da_cia

    @nome_da_cia.setter
    def nome_da_cia(self, new_nome_da_cia: str) -> None:
        self._nome_da_cia = new_nome_da_cia

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.nome_da_cia}"


class AeronavePassageiros(AeronaveComercial):
    """Classe para aeronaves particulares."""

    max_de_passageiros: int


class AeronaveCarga(AeronaveComercial):
    """Classe para aeronaves particulares."""

    max_de_carga: int
