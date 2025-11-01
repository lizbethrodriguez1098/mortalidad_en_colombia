rango_edad_dict = {
    (0, 4): "Mortalidad neonatal (<1 mes)",
    (5, 6): "Mortalidad infantil (1-11 meses)",
    (7, 8): "Primera infancia (1-4 años)",
    (9, 10): "Niñez (5-14 años)",
    (11, 11): "Adolescencia (15-19 años)",
    (12, 13): "Juventud (20-29 años)",
    (14, 16): "Adultez temprana (30-44 años)",
    (17, 19): "Adultez intermedia (45-59 años)",
    (20, 24): "Vejez (60-84 años)",
    (25, 28): "Longevidad / Centenarios (85+ años)",
    (29, 29): "Edad desconocida"
}

def asignar_categoria_edad(valor):
    for (inicio, fin), categoria in rango_edad_dict.items():
        if inicio <= valor <= fin:
            return categoria
    return "Sin información"