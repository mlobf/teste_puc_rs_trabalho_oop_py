from src.models.aeronaves import AeronaveParticular
from src.services.aeronaves import ServicoAeronaves
from src.services.pilotos import ServicoPilotos
from src.services.aerovia import ServicoAerovias

# particular = AeronaveParticular("particular", "ptx 8080", 800, 1000, "lito")


# sa = ServicoAeronaves()
sp = ServicoPilotos()
sa = ServicoAerovias()
"""
tipo: str,
prefixo: str,
velocidade_cruzeiro: float,
autonomia: float,
nome_da_cia: str
"""
"""
carga = ["Carga", "TEX CARGA", 900, 900, "TAX"]
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
sa.nova_aeronave(carga)
print(sa.show_aeronaves())
print(sa.get_aeronave_id(5))


piloto = ["Marcos", "sdfsdf333", "True"]
piloto1 = ["Joao", "azul", "True"]
piloto2 = ["Marcelo", "39393", "True"]
piloto3 = ["Caio", "skdfsfdj", "True"]
piloto4 = ["Fabio", "skdfsfdj", "True"]
piloto5 = ["Erica", "skdfsfdj", "False"]
sp.new_piloto(piloto)
sp.new_piloto(piloto2)
sp.new_piloto(piloto3)
sp.new_piloto(piloto4)
sp.new_piloto(piloto5)

print(sp.show_pilotos())
print(sp.get_piloto_id(5))
"""
aerovia1 = ["229292", "GRU", "MAD", "4000"]
aerovia2 = ["229293", "GRU", "MAU", "40"]
aerovia3 = ["229291", "GRU", "POA", "900"]

sa.new_aerovia(aerovia1)
sa.new_aerovia(aerovia2)
sa.new_aerovia(aerovia3)


print(sa.show_aerovias())
print(sa.get_aerovias_id(1))
print(sa.get_aerovias_id(0))
