#!/usr/bin/python3
# vim: ts=4 sw=4 et

import csv
import re
import sys

class Answer(object):

    def __init__(self, line):

        self.timestamp = line[0]
        self.idade = line[1]
        self.faixa_etaria = ""
        self.genero = line[2]
        self.escolaridade = line[3]
        self.ocupacao = line[4]
        self.renda = line[5]
        self.contaminacoes = line[6]
        self.familiar = line[7]
        self.estado = line[8]
        self.cidade = line[9]
        self.bairro = line[10]
        self.regiao = ""
        self.imovel = line[11]
        self.moradores = line[12]
        self.informacoes = line[13]
        self.microorganismo = line[14]
        self.nota_microorganismo = 0
        self.contagio = line[15]
        self.nota_contagio = 0
        self.sintomas = line[16]
        self.nota_sintomas = 0
        self.prevencao = line[17]
        self.nota_prevencao = 0
        self.combate = line[18]
        self.nota_combate = 0
        self.nota_final = 0
        self.tratamento = line[19]
        self.saneamento = line[20]
        self.governo = line[21]
        self.acoes = line[22]
        self.preocupado = line[23]
        self.vacina = line[24]

    def as_dict(self):

        print(self.__dict__)

    def as_list(self):

        return list(self.__dict__.values())

    def norm_idade(self):

        self.idade = re.sub("\D", "", self.idade)
        if self.idade:
            self.idade = int(self.idade)
        else:
            self.idade = 0

    def norm_estado(self):

        MAP = {"Amazonas ": "AM",
               "Brilhante primeiro": "XX",
               "Goias": "GO",
               "goiás ": "GO",
               "Goiás ": "GO",
               "Goiás": "GO",
               "Minas gerais": "MG",
               "mucajai": "XX",
               "Paraná ": "PR",
               "Paraná": "PR",
               "RJ": "RJ",
               "Roraima ": "RR",
               "Roraima": "RR",
               "santa catarina ": "SC",
               "santa catarina": "SC",
               "Santa catarina": "SC",
               "Santa Catarina ": "SC",
               "Santa Catarina": "SC",
               "Santa Catarina - SC": "SC",
               "Santa catarins": "SC",
               "São Paulo": "SP",
               "Sc": "SC",
               "S/C": "SC",
               "SC ": "SC",
               "SC": "SC",
               "sp": "SP",
               "SP": "SP",
               "Xique-Xique": "XX"}

        if self.estado not in MAP:
            print(f"Estado {self.estado} não mapeado, usando XX")
            self.estado = "XX"
        else:
            self.estado = MAP[self.estado]

    def norm_cidade(self):

        MAP = {"aparecida de goiânia": "Aparecida de Goiânia",
               "Aparecida de Goiânia": "Aparecida de Goiânia",
               "Araquari": "Araquari",
               "Bahia": "XX",
               "Balneário barra do sul": "Balneário Barra do Sul",
               "Belo Horizonte": "Belo Horizonte",
               "Boa vista": "Boa Vista",
               "Boa Vista": "Boa Vista",
               "Camboriu": "Camboriu",
               "Colombo": "Colombo",
               "Curitiba": "Curitiba",
               "florianopolis": "Florianópolis",
               "Florianópolis": "Florianópolis",
               "Goainia": "Goiânia",
               "Goiania": "Goiânia",
               "Goiânia": "Goiânia",
               "Itajaí": "Itajaí",
               "ITAJAÍ": "Itajaí",
               "joinville": "Joinville",
               "Joinville": "Joinville",
               "JOINVILLE": "Joinville",
               "Jounville": "Joinville",
               "Manaus": "Manaus",
               "mucajai": "XX",
               "rio de janeiro": "Rio de Janeiro",
               "São Bernardo do Campo": "São Bernardo do Campo",
               "São Francisco do Sul SC": "São Francisco do Sul",
               "São José dos Campos": "São José dos Campos",
               "SP": "São Paulo",
               "Trindade": "XX"}

        self.cidade = self.cidade.strip()

        if self.cidade not in MAP:
            print(f"Cidade {self.cidade} não mapeada, usando XX")
            self.cidade = "XX"
        else:
            self.cidade = MAP[self.cidade]

    def norm_bairro(self):

        MAP = {"Ademar Garcia": "Adhemar Garcia",
               "Água Verde": "Água Verde",
               "Alto da Glória": "Alto da Glória",
               "American Park": "American Park",
               "Anita Garibaldi": "Anita Garibaldi",
               "Atiradores": "Atiradores",
               "Aventureiro": "Aventureiro",
               "Boa vista": "Boa Vista",
               "Boa Vista": "Boa Vista",
               "Boehmerwald": "Boehmerwald",
               "Bom retiro": "Bom Retiro",
               "Bom Retiro": "Bom Retiro",
               "Brilhante": "XX",
               "Bucarein": "Bucarein",
               "Buritis": "Buritis",
               "Cacari": "Caçari",
               "Caçari": "Caçari",
               "Caranã": "Caranã",
               "Centenário": "Centenário",
               "Centro": "Centro",
               "cidade livre": "Cidade Livre",
               "Cidade satélite": "Cidade Satélite",
               "cidade universitaria": "Cidade Universitaria",
               "Cidade vera cruz": "Cidade Vera Cruz",
               "Cidade vera Cruz 2": "Cidade Vera Cruz 2",
               "Cidade Vera Cruz 2": "Cidade Vera Cruz 2",
               "Comasa": "Comasa",
               "Costa e Silva": "Costa e Silva",
               "COSTA E SILVA": "Costa e Silva",
               "Costeira": "Costeira",
               "Espinheiro": "Espinheiros",
               "Fátima": "Fátima",
               "Finsocial": "XX",
               "Floresta": "Floresta",
               "Gilberto mestrinho": "XX",
               "Gloria": "Glória",
               "Glória": "Glória",
               "Guanabara": "Guanabara",
               "Ingleses": "Ingleses",
               "Iririu": "Iririú",
               "Iririú": "Iririú",
               "itacorubi": "Itacorubi",
               "Itaipú": "Itaipú",
               "Itaum": "Itaum",
               "Itinga": "Itinga",
               "Jardim floresta": "Jardim Floresta",
               "Jardim Iririú": "Jardim Iririú",
               "Jardim osasco": "Jardim Osasco",
               "Jardim paraíso": "Jardim Paraíso",
               "Jarivatuba": "Jarivatuba",
               "Jd iririu": "Jardim Iririú",
               "joão costa": "João Costa",
               "João Costa": "João Costa",
               "Lauzane": "Lauzane",
               "Limoeiro": "Limoeiro",
               "mangueiral": "Mangueiral",
               "Monte alegre": "Monte Alegre",
               "Morro do meio": "Morro do Meio",
               "MORRO DO MEIO": "Morro do Meio",
               "Nova brasília": "Nova Brasília",
               "Panaguamirim": "Paranaguamirim",
               "Paranaguamirim": "Paranaguamirim",
               "PARANAGUAMIRIM": "Paranaguamirim",
               "Paraviana": "Paraviana",
               "Parque Oeste Industrial": "Parque Oeste Industrial",
               "Petrópolis": "Petrópolis",
               "Polivalente": "Polivalente",
               "Residencial Alvaluz luz": "XX",
               "Residencial recanto do bosque": "XX",
               "Residêncial vieira": "XX",
               "Rio bonito": "Rio Bonito",
               "Rudge Ramos": "XX",
               "Saguaçu": "Saguaçu",
               "Saguaçú": "Saguaçu",
               "Santa Catarina": "Santa Catarina",
               "Santa Regina": "Santa Regina",
               "Santo Antônio": "Santo Antônio",
               "São Marcos": "São Marcos",
               "Setor Bueno": "XX",
               "Setor Faiçalville III": "XX",
               "Setor marista": "XX",
               "Sol nascente": "XX",
               "Ubatuba": "Ubatuba",
               "Ulisses Guimarães": "Ulysses Guimarães",
               "Ullysses Guimarães": "Ulysses Guimarães",
               "Ulysses Guimarães": "Ulysses Guimarães",
               "Vera cruz": "Vera Cruz",
               "Vila nova": "Vila Nova",
               "Vila Nova": "Vila Nova",
               "Vila rosa": "Vila Rosa",
               "Vila Tesouro": "Vila Tesouro"}

        self.bairro = self.bairro.strip()

        if self.bairro not in MAP:
            print(f"Bairro {self.bairro} não mapeado, usando XX")
            self.bairro = "XX"
        else:
            self.bairro = MAP[self.bairro]

    def norm_moradores(self):

        MAP = {"0": "0",
               "01": "1",
               "1": "1",
               "2": "2",
               "3": "3",
               "3 pessoas": "3",
               "4": "4",
               "5": "5",
               "6": "6",
               "7": "7",
               "Cinco": "5",
               "Duas pessoas": "2",
               "Eu": "0",
               "Nenhuma": "0",
               "Só eu": "0",
               "Uma": "1"}

        self.moradores = self.moradores.strip()

        if self.moradores not in MAP:
            print(f"Número de moradores {self.moradores} não mapeado, usando 0")
            self.moradores = 0
        else:
            self.moradores = MAP[self.moradores]

    def norm_informacoes(self):

        MAP = {"Melhor criar campo com múltipla alternativa": "XX",
               "whatsapp do bolsonaro": "XX"}

        self.informacoes = self.informacoes.strip()

        if self.informacoes in MAP:
            self.informacoes = MAP[self.informacoes]

    def norm(self):

        self.norm_idade()
        self.norm_estado()
        self.norm_cidade()
        self.norm_bairro()
        self.norm_moradores()
        self.norm_informacoes()

    def calc_nota_microorganismo(self):

        NOTA_INIC = 0.0
        NOTA_MAX = 100.0

        corretas = ["Vírus"]

        self.nota_microorganismo = NOTA_INIC

        if self.microorganismo in corretas:
            self.nota_microorganismo = NOTA_MAX

    def calc_nota_formas_contagio(self):

        NOTA_INIC = 3.0
        NOTA_MAX = 4.0

        nota = NOTA_INIC
        corretas = ["Picada do mosquito Aedes Aegypt"]
        incorretas = ["Picada do mosquito Tsé-Tsé",
                      "Ingestão de água ou alimentos contaminados",
                      "Contato com pessoas contaminadas"]

        respostas = self.contagio.split(";")
        for r in respostas:
            if r in corretas:
                nota += 1
            if r in incorretas:
                nota -= 1

        self.nota_contagio = round((nota * 100.0) / NOTA_MAX, 2)

    def calc_nota_sintomas(self):

        NOTA_INIC = 3.0
        NOTA_MAX = 6.0

        nota = NOTA_INIC

        corretas = ["Febre", "Dores no corpo", "Manchas pelo corpo"]
        incorretas = ["Perda do olfato e paladar", "Tosse", "Dor de garganta"]

        respostas = self.sintomas.split(";")
        for r in respostas:
            if r in corretas:
                nota += 1
            if r in incorretas:
                nota -= 1

        self.nota_sintomas = round((nota * 100.0) / NOTA_MAX, 2)

    def calc_nota_prevencao(self):

        NOTA_INIC = 1.0
        NOTA_MAX = 3

        nota = NOTA_INIC

        corretas = ["Usar repelente", "Tomar uma vacina"]
        incorretas = ["Usar protetor solar"]

        respostas = self.prevencao.split(";")
        for r in respostas:
            if r in corretas:
                nota += 1
            if r in incorretas:
                nota -= 1

        self.nota_prevencao = round((nota * 100.0) / NOTA_MAX, 2)

    def calc_nota_combate(self):

        NOTA_MAX = 5.0

        nota = len(self.combate.split(";"))

        self.nota_combate = round((nota * 100.0) / NOTA_MAX, 2)

    def calc_notas(self):

        self.calc_nota_microorganismo()
        self.calc_nota_formas_contagio()
        self.calc_nota_sintomas()
        self.calc_nota_prevencao()
        self.calc_nota_combate()

        self.nota_final = round((self.nota_microorganismo +
                                 self.nota_contagio +
                                 self.nota_sintomas +
                                 self.nota_prevencao +
                                 self.nota_combate) / 5.0, 2)

    def calc_faixa_etaria(self):

        if self.idade < 10:
            self.faixa_etaria = "0-9"
        elif self.idade < 20:
            self.faixa_etaria = "10-19"
        elif self.idade < 30:
            self.faixa_etaria = "20-29"
        elif self.idade < 40:
            self.faixa_etaria = "30-39"
        elif self.idade < 50:
            self.faixa_etaria = "40-49"
        elif self.idade < 60:
            self.faixa_etaria = "50-59"
        else:
            self.faixa_etaria = "60-70"

    def def_regiao(self):

        # apenas para bairros de Joinville

        MAP = {"Adhemar Garcia": "Sudeste",
               "Anita Garibaldi": "Centro",
               "Atiradores": "Centro",
               "Aventureiro": "Nordeste",
               "Boa Vista": "Leste",
               "Boehmerwald": "Sul",
               "Bom Retiro": "Norte",
               "Bucarein": "Centro",
               "Centro": "Centro",
               "Comasa": "Leste",
               "Costa e Silva": "Norte",
               "Espinheiros": "Leste",
               "Fátima": "Sudeste",
               "Floresta": "Sul",
               "Glória": "Centro",
               "Guanabara": "Sudeste",
               "Iririú": "Nordeste",
               "Itaum": "Sul",
               "Itinga": "Sul",
               "Jardim Iririú": "Leste",
               "Jardim Paraíso": "Nordeste",
               "Jarivatuba": "Sudeste",
               "João Costa": "Sudeste",
               "Morro do Meio": "Oeste",
               "Nova Brasília": "Sudoeste",
               "Paranaguamirim": "Sudeste",
               "Petrópolis": "Sul",
               "Rio Bonito": "Norte",
               "Saguaçu": "Centro",
               "Santa Catarina": "Sul",
               "Santo Antônio": "Norte",
               "São Marcos": "Sudoeste",
               "Ulysses Guimarães": "Sudeste",
               "Vila Nova": "Oeste"}

        if self.bairro in MAP:
            self.regiao = MAP[self.bairro]

def main(args):

    if len(args) != 3:
        print("Use: __file__ <input.csv> <output.csv>")
        sys.exit(1)

    input_f = args[1]
    output_f = args[2]

    data = open(input_f, "r").readlines()
    data = data[1:]

    d = csv.reader(data)

    out = open(output_f, "w")
    csv_out = csv.writer(out, dialect=csv.unix_dialect())

    for line in d:

        a = Answer(line)
        a.norm()
        a.calc_faixa_etaria()
        a.calc_notas()
        a.def_regiao()
        csv_out.writerow(a.as_list())

    out.close()

if __name__ == "__main__":
    main(sys.argv)
