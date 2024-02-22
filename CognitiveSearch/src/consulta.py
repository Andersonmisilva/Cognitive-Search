# src/consulta.py
def realizar_consulta(query, index):
    # Implementar lógica de consulta (exemplo: procurar no índice)
    resultados = [item for item in index.items() if query in item[1]]

    return resultados
