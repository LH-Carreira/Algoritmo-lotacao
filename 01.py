import pandas as pd

professores_lotados = pd.DataFrame(columns=['URE', 'USE', 'MUNICIPIO', 'COD_ESCOLA', 'COD_MEC','COD_SETOR', 'ESCOLA_MATRICULA', 'VINCULO', 'SERVIDOR','COD_DISCIPLINA', 'DISCIPLINA'])

# Suponha que você tenha um objeto com atributos correspondentes aos nomes das colunas
class Objeto:
    def __init__(self, URE, USE, MUNICIPIO, COD_ESCOLA, COD_MEC, COD_SETOR, ESCOLA_MATRICULA, VINCULO, SERVIDOR, COD_DISCIPLINA, DISCIPLINA):
        self.URE = URE
        self.USE = USE
        self.MUNICIPIO = MUNICIPIO
        self.COD_ESCOLA = COD_ESCOLA
        self.COD_MEC = COD_MEC
        self.COD_SETOR = COD_SETOR
        self.ESCOLA_MATRICULA = ESCOLA_MATRICULA
        self.VINCULO = VINCULO
        self.SERVIDOR = SERVIDOR
        self.COD_DISCIPLINA = COD_DISCIPLINA
        self.DISCIPLINA = DISCIPLINA

# Criação de um objeto com atributos correspondentes aos nomes das colunas
objeto = Objeto('valor1', 'valor2', 'valor3', 1, 101, 'A', 100, 'vinculo1', 'servidor1', 11, 'matematica')

# Preenchendo as colunas do DataFrame com os atributos do objeto
professores_lotados = professores_lotados._append(objeto.__dict__, ignore_index=True)

# Exibindo o DataFrame atualizado
print(professores_lotados)
