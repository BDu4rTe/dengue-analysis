import geopandas as gpd
import matplotlib.pyplot as plt
import csv

BAIRRO = {
    "ADHEMAR GARCIA": [],
    "AMÉRICA": [],
    "ANITA GARIBALDI": [],
    "ATIRADORES": [],
    "AVENTUREIRO": [],
    "BOA VISTA": [],
    "BOEHMERWALD": [],
    "BOM RETIRO": [],
    "BUCAREIN": [],
    "CENTRO": [],
    "COMASA": [],
    "COSTA E SILVA": [],
    "DONA FRANCISCA": [],
    "ESPINHEIROS": [],
    "FÁTIMA": [],
    "FLORESTA": [],
    "GLÓRIA": [],
    "GUANABARA": [],
    "IRIRIÚ": [],
    "ITAUM": [],
    "ITINGA": [],
    "JARDIM IRIRIÚ": [],
    "JARDIM PARAÍSO": [],
    "JARDIM SOFIA": [],
    "JARIVATUBA": [],
    "JOÃO COSTA": [],
    "MORRO DO MEIO": [],
    "NOVA BRASILIA": [],
    "NOVA BRASÍLIA": [],
    "PARANAGUAMIRIM": [],
    "PARQUE GUARANI": [],
    "PETRÓPOLIS": [],
    "PIRABEIRABA": [],
    "PROFIPO": [],
    "RIO BONITO": [],
    "SAGUAÇU": [],
    "SANTA CATARINA": [],
    "SANTO ANTÔNIO": [],
    "SAO MARCOS": [],
    "SÃO MARCOS": [],
    "ULYSSES GUIMARAES": [],
    "ULYSSES GUIMARÃES": [],
    "VILA CUBATÃO": [],
    "VILA NOVA": [],
    "ZONA INDUSTRIAL NORTE": [],
    "ZONA INDUSTRIAL TUPY": [],
}

REGIAO = {
    "CENTRO": [],
    "LESTE": [],
    "NORDESTE": [],
    "NORTE": [],
    "OESTE": [],
    "SUDESTE": [],
    "SUL": [],
}

BAIRRO_REGIAO = {
    "ADHEMAR GARCIA": "SUDESTE",
    "AMÉRICA": "CENTRO",
    "ANITA GARIBALDI": "CENTRO",
    "ATIRADORES": "CENTRO",
    "AVENTUREIRO": "NORDESTE",
    "BOA VISTA": "LESTE",
    "BOEHMERWALD": "SUL",
    "BOM RETIRO": "NORTE",
    "BUCAREIN": "CENTRO",
    "CENTRO": "CENTRO",
    "COMASA": "LESTE",
    "COSTA E SILVA": "NORTE",
    "DONA FRANCISCA": "NORTE",
    "ESPINHEIROS": "LESTE",
    "FÁTIMA": "SUDESTE",
    "FLORESTA": "SUL",
    "GLÓRIA": "CENTRO",
    "GUANABARA": "SUDESTE",
    "IRIRIÚ": "LESTE",
    "ITAUM": "SUL",
    "ITINGA": "SUL",
    "JARDIM IRIRIÚ": "LESTE",
    "JARDIM PARAÍSO": "NORDESTE",
    "JARDIM SOFIA": "NORTE",
    "JARIVATUBA": "SUDESTE",
    "JOÃO COSTA": "SUDESTE",
    "MORRO DO MEIO": "OESTE",
    "NOVA BRASILIA": "OESTE",
    "NOVA BRASÍLIA": "OESTE",
    "PARANAGUAMIRIM": "SUDESTE",
    "PARQUE GUARANI": "SUL",
    "PETRÓPOLIS": "SUL",
    "PIRABEIRABA": "NORTE",
    "PROFIPO": "SUL",
    "RIO BONITO": "NORTE",
    "SAGUAÇU": "CENTRO",
    "SANTA CATARINA": "SUL",
    "SANTO ANTÔNIO": "NORTE",
    "SAO MARCOS": "OESTE",
    "SÃO MARCOS": "OESTE",
    "ULYSSES GUIMARAES": "SUDESTE",
    "ULYSSES GUIMARÃES": "SUDESTE",
    "VILA CUBATÃO": "NORDESTE",
    "VILA NOVA": "OESTE",
    "ZONA INDUSTRIAL NORTE": "NORTE",
    "ZONA INDUSTRIAL TUPY": "LESTE",
}

# dados externos
# powerbi painel dengue joinville
# 12/05/2024

POPULACAO = {
    "ADHEMAR GARCIA": 11200,
    "AMÉRICA": 12300,
    "ANITA GARIBALDI": 12300,
    "ATIRADORES": 6500,
    "AVENTUREIRO": 42700,
    "BOA VISTA": 17600,
    "BOEHMERWALD": 17600,
    "BOM RETIRO": 14400,
    "BUCAREIN": 7100,
    "CENTRO": 6400,
    "COMASA": 20800,
    "COSTA E SILVA": 33800,
    "DONA FRANCISCA": 600,
    "ESPINHEIROS": 10700,
    "FÁTIMA": 14300,
    "FLORESTA": 22300,
    "GLÓRIA": 12500,
    "GUANABARA": 11400,
    "IRIRIÚ": 25400,
    "ITAUM": 14600,
    "ITINGA": 8400,
    "JARDIM IRIRIÚ": 26700,
    "JARDIM PARAÍSO": 23200,
    "JARDIM SOFIA": 5800,
    "JARIVATUBA": 13900,
    "JOÃO COSTA": 14600,
    "MORRO DO MEIO": 12100,
    "NOVA BRASILIA": 14100,
    "NOVA BRASÍLIA": 14100,
    "PARANAGUAMIRIM": 33700,
    "PARQUE GUARANI": 13600,
    "PETRÓPOLIS": 14600,
    "PIRABEIRABA": 4900,
    "PROFIPO": 4700,
    "RIO BONITO": 6600,
    "SAGUAÇU": 14300,
    "SANTA CATARINA": 7500,
    "SANTO ANTÔNIO": 10700,
    "SAO MARCOS": 3200,
    "SÃO MARCOS": 3200,
    "ULYSSES GUIMARAES": 11900,
    "ULYSSES GUIMARÃES": 11900,
    "VILA CUBATÃO": 1300,
    "VILA NOVA": 32300,
    "ZONA INDUSTRIAL NORTE": 3100,
    "ZONA INDUSTRIAL TUPY": 54,
}

# fonte: https://www.joinville.sc.gov.br/wp-content/uploads/2017/01/Joinville-Bairro-a-Bairro-2017.pdf
# em km2
AREA = {
    "ADHEMAR GARCIA": 1.96,
    "AMÉRICA": 4.54,
    "ANITA GARIBALDI": 3.04,
    "ATIRADORES": 2.81,
    "AVENTUREIRO": 9.43,
    "BOA VISTA": 5.37,
    "BOEHMERWALD": 3.14,
    "BOM RETIRO": 3.91,
    "BUCAREIN": 2.04,
    "CENTRO": 1.31,
    "COMASA": 2.71,
    "COSTA E SILVA": 6.58,
    "DONA FRANCISCA": 1.10,
    "ESPINHEIROS": 2.74,
    "FÁTIMA": 2.21,
    "FLORESTA": 4.99,
    "GLÓRIA": 5.37,
    "GUANABARA": 2.55,
    "IRIRIÚ": 6.22,
    "ITAUM": 3.18,
    "ITINGA": 7.73,
    "JARDIM IRIRIÚ": 3.30,
    "JARDIM PARAÍSO": 3.22,
    "JARDIM SOFIA": 2.13,
    "JARIVATUBA": 2.09,
    "JOÃO COSTA": 3.41,
    "MORRO DO MEIO": 5.44,
    "NOVA BRASILIA": 7.85,
    "NOVA BRASÍLIA": 7.85,
    "PARANAGUAMIRIM": 11.51,
    "PARQUE GUARANI": 4.41,
    "PETRÓPOLIS": 3.04,
    "PIRABEIRABA": 6.09,
    "PROFIPO": 1.66,
    "RIO BONITO": 5.73,
    "SAGUAÇU": 4.89,
    "SANTA CATARINA": 5.42,
    "SANTO ANTÔNIO": 2.20,
    "SAO MARCOS": 5.46,
    "SÃO MARCOS": 5.46,
    "ULYSSES GUIMARAES": 3.23,
    "ULYSSES GUIMARÃES": 3.23,
    "VILA CUBATÃO": 0.36,
    "VILA NOVA": 14.43,
    "ZONA INDUSTRIAL NORTE": 30.70,
    "ZONA INDUSTRIAL TUPY": 1.47
}

FOCOS = {
    "ADHEMAR GARCIA": 36,
    "AMÉRICA": 211,
    "ANITA GARIBALDI": 296,
    "ATIRADORES": 90,
    "AVENTUREIRO": 757,
    "BOA VISTA": 346,
    "BOEHMERWALD": 202,
    "BOM RETIRO": 181,
    "BUCAREIN": 181,
    "CENTRO": 109,
    "COMASA": 272,
    "COSTA E SILVA": 348,
    "DONA FRANCISCA": 30,
    "ESPINHEIROS": 178,
    "FÁTIMA": 139,
    "FLORESTA": 417,
    "GLÓRIA": 183,
    "GUANABARA": 137,
    "IRIRIÚ": 239,
    "ITAUM": 290,
    "ITINGA": 69,
    "JARDIM IRIRIÚ": 266,
    "JARDIM PARAÍSO": 297,
    "JARDIM SOFIA": 30,
    "JARIVATUBA": 60,
    "JOÃO COSTA": 236,
    "MORRO DO MEIO": 229,
    "NOVA BRASILIA": 204,
    "NOVA BRASÍLIA": 204,
    "PARANAGUAMIRIM": 347,
    "PARQUE GUARANI": 91,
    "PETRÓPOLIS": 69,
    "PIRABEIRABA": 103,
    "PROFIPO": 20,
    "RIO BONITO": 108,
    "SAGUAÇU": 180,
    "SANTA CATARINA": 52,
    "SANTO ANTÔNIO": 124,
    "SAO MARCOS": 117,
    "SÃO MARCOS": 117,
    "ULYSSES GUIMARAES": 63,
    "ULYSSES GUIMARÃES": 63,
    "VILA CUBATÃO": 80,
    "VILA NOVA": 298,
    "ZONA INDUSTRIAL NORTE": 222,
    "ZONA INDUSTRIAL TUPY": 23,
}

CASOS = {
    "ADHEMAR GARCIA": 379,
    "AMÉRICA": 369,
    "ANITA GARIBALDI": 382,
    "ATIRADORES": 205,
    "AVENTUREIRO": 4113,
    "BOA VISTA": 1443,
    "BOEHMERWALD": 1121,
    "BOM RETIRO": 574,
    "BUCAREIN": 209,
    "CENTRO": 187,
    "COMASA": 840,
    "COSTA E SILVA": 1612,
    "DONA FRANCISCA": 18,
    "ESPINHEIROS": 376,
    "FÁTIMA": 474,
    "FLORESTA": 972,
    "GLÓRIA": 358,
    "GUANABARA": 427,
    "IRIRIÚ": 1306,
    "ITAUM": 445,
    "ITINGA": 708,
    "JARDIM IRIRIÚ": 935,
    "JARDIM PARAÍSO": 1233,
    "JARDIM SOFIA": 264,
    "JARIVATUBA": 474,
    "JOÃO COSTA": 610,
    "MORRO DO MEIO": 494,
    "NOVA BRASILIA": 453,
    "NOVA BRASÍLIA": 453,
    "PARANAGUAMIRIM": 997,
    "PARQUE GUARANI": 460,
    "PETRÓPOLIS": 500,
    "PIRABEIRABA": 661,
    "PROFIPO": 132,
    "RIO BONITO": 179,
    "SAGUAÇU": 1199,
    "SANTA CATARINA": 407,
    "SANTO ANTÔNIO": 529,
    "SAO MARCOS": 82,
    "SÃO MARCOS": 82,
    "ULYSSES GUIMARAES": 469,
    "ULYSSES GUIMARÃES": 469,
    "VILA CUBATÃO": 401,
    "VILA NOVA": 1278,
    "ZONA INDUSTRIAL NORTE": 243,
    "ZONA INDUSTRIAL TUPY": 0,
}

# importa dados exclusivos de Joinville, gerados por etl.py
data = open("out-joi.csv", "r").readlines()
data = data[1:]

# nota de cada bairro
notas = BAIRRO
# nota de cada regiao
notas_regiao = REGIAO

for line in csv.reader(data):

    bairro = line[11].upper()
    regiao = line[12].upper()
    nota = float(line[-7])

    # todas as notas do bairro
    notas[bairro].append(nota)

    # todas as notas dos bairros que pertecem a regiao
    rb = BAIRRO_REGIAO[bairro]
    notas_regiao[rb].append(nota)

# calcula a média de cada regiao
for k, v in notas_regiao.items():
    notas_regiao[k] = round(sum(v) / len(v), 2)

# substitui a nota de cada bairro pela nota de sua regiao
for k, v in notas.items():
    rb = BAIRRO_REGIAO[k]
    notas[k] = notas_regiao[rb]

gdf = gpd.read_file("Limites/bairros.shp")

fig, ax = plt.subplots(1, figsize=(18.5*3,10.5*3))

# inicializa coluna "nota_final" no dataframe do geopandas
if "nota_final" not in gdf.columns:
    gdf["nota_final"] = None
    gdf["nota_final"] = gdf["nota_final"].astype("float64")
    gdf["nota_final"] = gdf["nota_final"].round(decimals=4)

# inicializa coluna "focos_mosquito" no dataframe do geopandas
if "focos_mosquito" not in gdf.columns:
    gdf["focos_mosquito"] = 0
    gdf["focos_mosquito"] = gdf["focos_mosquito"].astype("float64")
    gdf["focos_mosquito"] = gdf["focos_mosquito"].round(decimals=4)

# inicializa coluna "casos_confirmados" no dataframe do geopandas
if "casos_confirmados" not in gdf.columns:
    gdf["casos_confirmados"] = 0
    gdf["casos_confirmados"] = gdf["casos_confirmados"].astype("float64")
    gdf["casos_confirmados"] = gdf["casos_confirmados"].round(decimals=4)

for index, row in gdf.iterrows():
    if row.nome_bairr in notas:
        gdf.at[index, "nota_final"] = notas[row.nome_bairr]
        gdf.at[index, "focos_mosquito"] = round(FOCOS[row.nome_bairr] / AREA[row.nome_bairr], 4)
        gdf.at[index, "casos_confirmados"] = round(CASOS[row.nome_bairr] / POPULACAO[row.nome_bairr], 4)
    else:
        gdf.at[index, "nota_final"] = 0
        gdf.at[index, "focos_mosquito"] = 0
        gdf.at[index, "casos_confirmados"] = 0

gdf.plot(column="nota_final", ax=ax, cmap="Purples", categorical=True, legend=True)
gdf.apply(lambda x: ax.annotate(text=x.nome_bairr, xy=x.geometry.centroid.coords[0], ha='center', color='black'), axis=1)
ax.axis('off')
plt.savefig("bairros.png", bbox_inches='tight', pad_inches=0)

gdf.plot(column="focos_mosquito", ax=ax, cmap="Reds", categorical=True, legend=True)
gdf.apply(lambda x: ax.annotate(text=x.nome_bairr, xy=x.geometry.centroid.coords[0], ha='center', color='black'), axis=1)
ax.axis('off')
plt.savefig("focos.png", bbox_inches='tight', pad_inches=0)

gdf.plot(column="casos_confirmados", ax=ax, cmap="Greens", categorical=True, legend=True)
gdf.apply(lambda x: ax.annotate(text=x.nome_bairr, xy=x.geometry.centroid.coords[0], ha='center', color='black'), axis=1)
ax.axis('off')
plt.savefig("casos.png", bbox_inches='tight', pad_inches=0)
