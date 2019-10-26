# CriptografiaAPS
Trabalho de conclusão de semestre da UNIP.

## Criptografias usadas
- Cifra de Cesar;
- RSA;
- One Time Pad ( Custom e ASCII ).

## Manipulando as criptografias via linha de comando:
### Sintaxe básica:
```
python aps.py (-e|-d) (-txt|-file) cript args
```

## Criptografando e descriptografando mensagens:
### Cifra de César:
```
# Sintaxe
python aps.py (-e|-d) (-txt|-file) cript rot

# Encriptando
python aps.py -e -txt foo caesar 12
python aps.py -e -file foo.txt caesar 12

# Desencriptando:
python aps.py -d -txt raa caesar 12
python aps.py -d -file raa.txt caesar 12
```

### RSA:
```
# Gerar chave
python aps.py -e -txt teste rsaGk

# Sintaxe
python aps.py (-e|-d) (-txt|-file) rsa keypublic1 key

# Encriptando:
python aps.py -e -txt foo rsa 1624391 110923
python aps.py -e -file foo.txt rsa 1624391 110923

# Desencriptando:
python aps.py -d -txt  0xf481b:0x9ccd9:0x9ccd9 rsa 1624391 68467
python aps.py -d -file foo.txt rsa 1624391 68467
```

### ASCII OTP:
```
Sintaxe:
python aps.py (-e|-d) (-txt|-file) asciiotp key

# Encriptando:
python aps.py -e -txt foo asciiotp $RANDOM$
python aps.py -e -file foo.txt asciiotp $RANDOM$

# Desencriptando:
python aps.py -d -txt 0x11:0x1f:0x1d asciiotp wpr
python aps.py -d -file foo.txt asciiotp wpr

$RANDOM$ Gera uma chave randomica do mesmo tamanho do texto
```

### CUSTOM OTP:
```
Sintaxe:
python aps.py [-h] (-txt TXT | -file FILE) (--encript | --decript) cript args

# Encriptando:
python aps.py -e -txt foo otp $RANDOM$
python aps.py -e -file foo.txt otp $RANDOM$

# Desencriptando:
python aps.py -d -txt X)t asciiotp SUf
python aps.py -d -file foo.txt asciiotp SUf

$RANDOM$ Gera uma chave randomica do mesmo tamanho do texto
```

## Por que ASCIIOTP e RSA retornam hexadecimal?
Ambas as criptografias manipulam valores que podem pertencer ou não a tabela,
isto é, valores decimais que ultrapassam os limites da tabela ASCII ou valores
pertencentes a tabela ASCII porém visiveis. Dito isto, por 
convencao, o grupo decidiu padronizar a saida das criptografias que manipulam 
a tabela ASCII, tornando seu resultado, após a encriptação, em hexadecimal.




