# from ..models.aeronaves import AeronaveCarga
# from .models.aeronaves import AeronaveCarga
from src.models.aeronaves import AeronaveCarga
import uuid

# _src/models/aeronaves.py


def oi():
    return "oi"


class ServicoAeronaves:
    base = {}
    contador = 0

    def nova_aeronave(self, lista_de_requisitos):
        """
        tipo: str,
        prefixo: str,
        velocidade_cruzeiro: float,
        autonomia: float,
        nome_da_cia: str
        """
        ac = AeronaveCarga(*lista_de_requisitos)
        # str_uuid = str(uuid.uuid4())
        # self.base[str_uuid] = ac
        self.base[self.contador] = ac
        self.contador += 1
        return str(self.base.items())

    def show_aeronaves(self):
        for key, value in self.base.items():
            print(key, value)

    def get_aeronave_id(self, id):
        if self.base.get(id):
            return self.base.get(id)
