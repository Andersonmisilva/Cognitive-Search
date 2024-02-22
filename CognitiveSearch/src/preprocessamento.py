# src/preprocessamento.py
def preprocessar_dados(dataset_path):
    # Implementar lógica de preprocessamento (exemplo: remover duplicatas)
    dataset = pd.read_csv(dataset_path)
    dataset_sem_duplicatas = dataset.drop_duplicates()

    return dataset_sem_duplicatas
