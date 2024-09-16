from src.models.aeronaves import AeronaveParticular
from src.services.aeronaves import ServicoAeronaves
from src.services.pilotos import ServicoPilotos

# particular = AeronaveParticular("particular", "ptx 8080", 800, 1000, "lito")


sa = ServicoAeronaves()
sp = ServicoPilotos()
"""
tipo: str,
prefixo: str,
velocidade_cruzeiro: float,
autonomia: float,
nome_da_cia: str
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


piloto = ["Marcos", "skdfsfdj", "True"]
sp.new_piloto(piloto)
sp.new_piloto(piloto)
sp.new_piloto(piloto)
sp.new_piloto(piloto)
sp.new_piloto(piloto)
sp.new_piloto(piloto)
sp.new_piloto(piloto)

print(sp.show_pilotos())
