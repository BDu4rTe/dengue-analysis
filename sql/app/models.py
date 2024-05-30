from . import db

class Escolaridade(db.Model):

    __tablename__ = "en_escolaridade"

    id_escolaridade = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Ocupacao(db.Model):

    __tablename__ = "en_ocupacao"

    id_ocupacao = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Renda(db.Model):

    __tablename__ = "en_renda"

    id_renda = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Contagio(db.Model):

    __tablename__ = "en_contagio"

    id_contagio = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    val = db.Column(db.Integer, nullable=False)

class TipoMoradia(db.Model):

    __tablename__ = "en_tipo_moradia"

    id_tipo_moradia = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Regiao(db.Model):

    __tablename__ = "en_regiao"

    id_regiao = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Estado(db.Model):

    __tablename__ = "en_estado"

    id_estado = db.Column(db.Integer, primary_key=True, nullable=False)
    sigla = db.Column(db.String, nullable=False, unique=True)
    nome = db.Column(db.String, nullable=False)

class Cidade(db.Model):

    __tablename__ = "en_cidade"

    id_cidade = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey("en_estado.id_estado"))
    estado = db.relationship("Estado")

class Bairro(db.Model):

    __tablename__ = "en_bairro"

    id_bairro = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    id_cidade = db.Column(db.Integer, db.ForeignKey("en_cidade.id_cidade"))
    cidade = db.relationship("Cidade")
    id_regiao = db.Column(db.Integer, db.ForeignKey("en_regiao.id_regiao"))
    regiao = db.relationship("Regiao")

class FonteInformacao(db.Model):

    __tablename__ = "en_fonte_informacao"

    id_fonte_informacao = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Tratamento(db.Model):

    __tablename__ = "en_tratamento"

    id_tratamento = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Acao(db.Model):

    __tablename__ = "en_acao"

    id_acao = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Preocupacao(db.Model):

    __tablename__ = "en_preocupacao"

    id_preocupacao = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Vacina(db.Model):

    __tablename__ = "en_vacina"

    id_vacina = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String, nullable=False)

class Resposta(db.Model):

    __tablename__ = "en_resposta"

    id_resposta = db.Column(db.Integer, primary_key=True, nullable=False)

    timestamp = db.Column(db.DateTime, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String, nullable=False)

    id_escolaridade = db.Column(db.Integer, db.ForeignKey("en_escolaridade.id_escolaridade"))
    escolaridade = db.relationship("Escolaridade")

    id_ocupacao = db.Column(db.Integer, db.ForeignKey("en_ocupacao.id_ocupacao"))
    ocupacao = db.relationship("Ocupacao")

    id_renda = db.Column(db.Integer, db.ForeignKey("en_renda.id_renda"))
    renda = db.relationship("Renda")

    id_contagio = db.Column(db.Integer, db.ForeignKey("en_contagio.id_contagio"))
    contagio = db.relationship("Contagio")

    contagio_familia = db.Column(db.String, nullable=False)

    id_estado = db.Column(db.Integer, db.ForeignKey("en_estado.id_estado"))
    estado = db.relationship("Estado")

    id_cidade = db.Column(db.Integer, db.ForeignKey("en_cidade.id_cidade"))
    cidade = db.relationship("Cidade")

    id_bairro = db.Column(db.Integer, db.ForeignKey("en_bairro.id_bairro"))
    bairro = db.relationship("Bairro")

    id_tipo_moradia = db.Column(db.Integer, db.ForeignKey("en_tipo_moradia.id_tipo_moradia"))
    tipo_moradia = db.relationship("TipoMoradia")

    coabitacao = db.Column(db.Integer)

    id_fonte_informacao = db.Column(db.Integer, db.ForeignKey("en_fonte_informacao.id_fonte_informacao"))
    fonte_informacao = db.relationship("FonteInformacao")

    microorganismo = db.Column(db.String)
    formas_contagio = db.Column(db.String)
    sintomas = db.Column(db.String)
    prevencao = db.Column(db.String)
    combate = db.Column(db.String)

    id_tratamento = db.Column(db.Integer, db.ForeignKey("en_tratamento.id_tratamento")) 
    tratamento = db.relationship("Tratamento")

    saneamento = db.Column(db.Integer)
    governo = db.Column(db.Integer)

    id_acao = db.Column(db.Integer, db.ForeignKey("en_acao.id_acao"))
    acao = db.relationship("Acao")

    id_preocupacao = db.Column(db.Integer, db.ForeignKey("en_preocupacao.id_preocupacao"))
    preocupacao = db.relationship("Preocupacao")

    id_vacina = db.Column(db.Integer, db.ForeignKey("en_vacina.id_vacina"))
    vacina = db.relationship("Vacina")

