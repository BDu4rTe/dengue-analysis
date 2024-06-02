## Microorganismo causador

# por fonte de informacao
SELECT fi.nome, AVG(re.nota_microorganismo) AS nota
    FROM en_resposta re, en_fonte_informacao fi
    WHERE fi.id_fonte_informacao = re.id_fonte_informacao
    GROUP BY re.id_fonte_informacao
    ORDER BY nota;

# por escolaridade
SELECT es.nome, AVG(re.nota_microorganismo) AS nota
    FROM en_resposta re, en_escolaridade es
    WHERE es.id_escolaridade = es.id_escolaridade
    GROUP BY re.id_escolaridade
    ORDER BY nota;

## Conhecimento sobre os sintomas

# por fonte de informacao
SELECT fi.nome, AVG(re.nota_sintomas) AS nota
    FROM en_resposta re, en_fonte_informacao fi
    WHERE re.id_fonte_informacao = fi.id_fonte_informacao
    GROUP BY re.id_fonte_informacao
    ORDER BY nota;

# por escolaridade
SELECT es.nome, AVG(re.nota_sintomas) AS nota
    FROM en_resposta re, en_escolaridade es
    WHERE re.id_escolaridade = es.id_escolaridade
    GROUP BY re.id_escolaridade
    ORDER BY nota;

## Nota final por bairro

SELECT ba.nome AS bairro, AVG(re.nota_final) AS nota
    FROM en_bairro ba, en_resposta re
    WHERE re.id_bairro = ba.id_bairro
    GROUP BY ba.nome
    ORDER BY nota;

## Nota final por regiao

SELECT reg.nome AS regiao, AVG(re.nota_final) AS nota
    FROM en_resposta re, en_bairro ba, en_regiao reg
    WHERE re.id_bairro = ba.id_bairro AND
          reg.id_regiao = ba.id_regiao
    GROUP BY ba.id_regiao
    ORDER BY nota;
