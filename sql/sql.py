#!/usr/bin/python3
# vim: ts=4 sw=4 et

from datetime import datetime
from app.models import *
from app import db, create_app
import csv
import sys

REGIOES = [
    "Norte",
    "Nordeste",
    "Leste",
    "Sudeste",
    "Sul",
    "Sudoeste",
    "Oeste",
    "Noroeste"
]

ESCOLARIDADE = [
    "Fundamental incompleto",
    "Fundamental completo",
    "Médio completo",
    "Superior completo"
]

OCUPACAO = [
    "",
    "Trabalho",
    "Estudo",
    "Trabalho e Estudo",
]

RENDA = [
    "Até 1 salário mínimo",
    "1 a 3 salários mínimos",
    "4 a 6 salários mínimos",
    "7 a 10 salários mínimos",
    "11 ou mais salários mínimos",
    "Prefiro não informar",
]

CONTAGIO = [
    ("Nenhuma", 0),
    ("Uma", 1),
    ("Duas", 2),
    ("Três ou mais", 3)
]

TIPO_MORADIA = [
    "Casa",
    "Apartamento",
]

FONTE_INFORMACAO = [
    "Amigos e familiares",
    "Internet (redes sociais, sites oficiais)",
    "Mídia tradicional (TV, rádio, jornal)",
    "Profissionais de saúde",
]

TRATAMENTO = [
    "Nunca tive dengue",
    "Insatisfatório",
    "Pouco satisfatório",
    "Moderadamente satisfatório",
    "Satisfatório",
    "Muito satisfatório",
]

ACAO = [
    "Nunca",
    "Raramente",
    "Às vezes",
    "Frequentemente",
    "Sempre",
]

PREOCUPACAO = [
    "Nada preocupado",
    "Pouco preocupado",
    "Moderadamente preocupado",
    "Muito preocupado",
    "Extremamente preocupado",
]

VACINA = [
    "Não tomaria",
    "Talvez tomaria",
    "Certamente tomaria",
]

def insert_static():

    for nome in REGIOES:
        e = Regiao()
        e.nome = nome
        db.session.add(e)

    for nome in ESCOLARIDADE:
        e = Escolaridade()
        e.nome = nome
        db.session.add(e)

    for nome in OCUPACAO:
        e = Ocupacao()
        e.nome = nome
        db.session.add(e)

    for nome, val in CONTAGIO:
        e = Contagio()
        e.nome = nome
        e.val = val
        db.session.add(e)

    for nome in RENDA:
        e = Renda()
        e.nome = nome
        db.session.add(e)

    for nome in TIPO_MORADIA:
        e = TipoMoradia()
        e.nome = nome
        db.session.add(e)

    for nome in FONTE_INFORMACAO:
        e = FonteInformacao()
        e.nome = nome
        db.session.add(e)

    for nome in TRATAMENTO:
        e = Tratamento()
        e.nome = nome
        db.session.add(e)

    for nome in ACAO:
        e = Acao()
        e.nome = nome
        db.session.add(e)

    for nome in PREOCUPACAO:
        e = Preocupacao()
        e.nome = nome
        db.session.add(e)

    for nome in VACINA:
        e = Vacina()
        e.nome = nome
        db.session.add(e)

def insert_csv():

    estados = open("estados.csv", "r").readlines()
    for e in csv.reader(estados[1:]):
        E = Estado()
        E.id_estado = e[0]
        E.sigla = e[2]
        E.nome = e[1]
        db.session.add(E)

    cidades = open("cidades.csv", "r").readlines()
    for c in csv.reader(cidades[1:]):
        C = Cidade()
        C.nome = c[2]
        C.id_estado = c[0]
        db.session.add(C)

    bairros = open("bairros.csv", "r").readlines()
    for b in csv.reader(bairros[1:]):
        B = Bairro()
        B.nome = b[0]
        B.cidade = Cidade.query.filter_by(nome="Joinville").first()
        B.regiao = Regiao.query.filter_by(nome=b[1]).first()
        db.session.add(B)

def insert_answers():

    data = open("out-joi.csv", "r").readlines()
    data = data[1:]

    for line in csv.reader(data):

        R = Resposta()
        R.timestamp = datetime.strptime(line[0], "%Y/%m/%d %I:%M:%S %p GMT-3")
        R.idade = line[1]
        R.faixa_etaria = line[2]
        R.genero = line[3][0]
        R.escolaridade = Escolaridade.query.filter_by(nome=line[4]).first()
        R.ocupacao = Ocupacao.query.filter_by(nome=line[5]).first()
        R.renda = Renda.query.filter_by(nome=line[6]).first()
        R.contagio = Contagio.query.filter_by(nome=line[7]).first()
        R.contagio_familia = line[8][0]
        R.estado = Estado.query.filter_by(sigla=line[9]).first()
        R.cidade = Cidade.query.filter_by(nome=line[10]).first()
        R.bairro = Bairro.query.filter_by(nome=line[11]).first()
        R.tipo_moradia = TipoMoradia.query.filter_by(nome=line[13]).first()
        R.coabitacao = int(line[14])
        R.fonte_informacao = FonteInformacao.query.filter_by(nome=line[15]).first()
        R.microorganismo = line[16]
        R.nota_microorganismo = line[17]
        R.formas_contagio = line[18]
        R.nota_formas_contagio = line[19]
        R.sintomas = line[20]
        R.nota_sintomas = line[21]
        R.prevencao = line[22]
        R.nota_prevencao = line[23]
        R.combate = line[24]
        R.nota_combate = line[25]
        R.nota_final = line[26]
        R.tratamento = Tratamento.query.filter_by(nome=line[27]).first()
        R.saneamento = int(line[28])
        R.governo = int(line[29])
        R.acao = Acao.query.filter_by(nome=line[30]).first()
        R.preocupacao = Preocupacao.query.filter_by(nome=line[31]).first()
        R.vacina = Vacina.query.filter_by(nome=line[32]).first()

        db.session.add(R)

def main():

    a = create_app()
    a.app_context().push()

    db.drop_all()
    db.create_all()

    insert_static()
    insert_csv()
    insert_answers()

    db.session.commit()

if __name__ == "__main__":
    main()
