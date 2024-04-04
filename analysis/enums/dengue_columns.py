from enum import Enum


class DengueColumns(Enum):
    DATA = "Data"
    IDADE = "Idade"
    GENERO = "Gênero"
    ESCOLARIDADE = "Escolaridade"
    ESTADO = "Estado"
    CIDADE = "Cidade"
    BAIRRO = "Bairro"
    RENDA = "Renda"
    NUMERO_PESSOAS = "Nº Pessoas"
    FORMAS_CONTAGIO = "Formas Contágio"
    MORADIA = "Moradia"
    SINTOMAS = "Sintomas"
    FAMILIAR_DENGUE = "Familiar Dengue"
    QUANTIDADE_DENGUE = "Qtd. Dengue"
    OCUPACAO = "Ocupação"
    ACOES_COMBATE = "Ações Combate"
    SANEAMENTO = "Saneamento"
    AVALIACAO_TRATAMENTO = "Avaliação Tratamento"
    GOV_COMBATE_DENGUE = "Gov. Combate Dengue"
    FONTE_INFORMACAO = "Fonte Informação"
    PREVENCAO_CONTAGIO = "Prevenção Contágio"
    CAUSA_DENGUE = "Causa Dengue"
    FREQUENCIA_ACOES_PREVENCAO = "Freq. Ações Prevenção"
    PREOCUPACAO_DENGUE = "Preocupação Dengue"
    VACINACAO_SUS = "Vacinação SUS"

    @classmethod
    def to_list(cls):
        return [column.value for column in cls]
