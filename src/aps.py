"""Manipular parametros de linha de comando."""
from argumentos import manipularArgumentos
import argparse

# Criando root
criptmng = argparse.ArgumentParser(
    description="Criptografias desenvolvidas pelo grupo da APS.",
)

# Argumentos para entrada de texto
# Apenas o texto ou arquivo serao selecionados.
input_arg = criptmng.add_mutually_exclusive_group(required=True)
input_arg.add_argument(
    "-txt",
    help="Texto a ser criptografado.",
    type=str
)
input_arg.add_argument(
    "-file",
    help="Arquivo a ser criptografado.",
    type=argparse.FileType('r', encoding='utf-8')
)

# Acoes para a criptografia
action_crip = criptmng.add_mutually_exclusive_group(required=True)
action_crip.add_argument(
    "--encript", "-e",
    help="Encriptar a mensagem.",
    action="store_true",
    default="store_false"
    )

action_crip.add_argument(
    "--decript", "-d",
    help="Desencriptar a mensagem.",
    action="store_true",
    default="store_false"
    )


# # 
# # CRIPTOGRAFIAS
# # 
cripts = criptmng.add_subparsers(
    dest='cript', 
    title="Criptografias da APS",
    required=True)

# Cifra de cesar
caesar = cripts.add_parser(
    "caesar", 
    help="Cifra de cesar"
    )

caesar.add_argument(
    "rot", 
    help="Rotacao para o alfabeto.",
    type=int
    )

caesar.add_argument(
    "-alphabet",
    help="Alfabeto customizado.",
    type=str
    )


# Gerador de chaves RSA
rsaKeys = cripts.add_parser(
    "rsaGK",
    help="Gerador de chaves RSA."
    )

rsaKeys.add_argument(
    "generateKeys",
    help="Gerar randomicamente chaves necessarias para a criptografia",
    action='store_true'
    )


# Criptografia RSA
rsa = cripts.add_parser(
    "rsa", 
    help="Criptografia RSA."
    )

rsa.add_argument(
    "publickey",
    help="Chave publica 1",
    type=int
    )

rsa.add_argument(
    "key",
    help='Chave privada para desencriptar e chave publica para encriptar.',
    type=int
    )

# Custom OTP
custom_otp = cripts.add_parser(
    "otp", 
    help="Criptografia One Time Pad com alfabeto padrao."
    )

custom_otp.add_argument(
    "key",
    help="""
        Chave para criptografar/descriptografar 
        [digite $RANDOM$ para chaves aleatorias].
        """,
    type=str
    )

custom_otp.add_argument(
    "-alphabet", 
    help="Alfabeto customizado.",
    type=str
    )

# ASCII OTP
ascii_otp = cripts.add_parser(
    "asciiotp", 
    help="Criptografia One Time Pad via tabela ascii."
    )

ascii_otp.add_argument(
    "key",
    help="""
        Chave para criptografar/descriptografar 
        [digite $RANDOM$ para chaves aleatorias].
        """,
    type=str
    )


if __name__ == "__main__":
    args = criptmng.parse_args()
    manipularArgumentos(**args.__dict__)
