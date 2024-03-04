marcas = [
    ('1005', 'TACOMITER'),
    ('101', 'DELLOFIX'),
    ('1033', 'YALE'),
    ('1034', 'ESFREBOM'),
    ('1046', 'ESPRESSIONE'),
    ('105', 'MODULUZ'),
    ('1050', 'EIRILAR'),
    ('1051', 'EIRILAR'),
    ('1074', 'IMPERIO'),
    ('1081', 'TUBOARTE'),
    ('1095', 'UNIK HOME'),
    ('1097', 'NOBRE'),
    ('1123', 'ESTOFADOS GERMANIA'),
    ('1124', 'FISCHER'),
    ('1125', 'RAFIA'),
]

contagem_marcas = {}
marcas_repetidas = []

for codigo, marca in marcas:
    if marca in contagem_marcas:
        contagem_marcas[marca] += 1
        if contagem_marcas[marca] == 2:
            marcas_repetidas.append(marca)
    else:
        contagem_marcas[marca] = 1

print("Marcas repetidas:", marcas_repetidas)
