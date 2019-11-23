"""Manipular parametros de linha de comando."""
from argumentos import argument_manipulator
import argparse

# Criando root
cript_manager = argparse.ArgumentParser(
    description="Criptografias desenvolvidas pelo grupo da APS.",
)


required_args = cript_manager.add_argument_group("Parametros Obrigatorios")

# Argumentos para entrada de texto
# Apenas o texto ou arquivo serao selecionados.
input_arg = required_args.add_mutually_exclusive_group(required=True)
input_arg.add_argument(
    "-txt",
    help="Texto a ser criptografado/descriptografado.",
    type=str,
    dest="input"
)
input_arg.add_argument(
    "-iF",
    help="Arquivo a ser criptografado/descriptografado.",
    type=argparse.FileType('r', encoding='utf-8'),
    dest="input"
)

cript_manager.add_argument(
    "-oF",
    help="Arquivo de saida.",
    type=argparse.FileType('w', encoding="utf-8"),
    dest="output"
    )


# Acoes para a criptografia
action_crip = required_args.add_mutually_exclusive_group(required=True)
action_crip.add_argument(
    "--encript", "-e",
    help="Encriptar a mensagem.",
    action="store_true",
    dest='action'
    )

action_crip.add_argument(
    "--decript", "-d",
    help="Desencriptar a mensagem.",
    action="store_false",
    dest='action'
    )


# # 
# # CRIPTOGRAFIAS
# # 
cripts = cript_manager.add_subparsers(
    dest='cript', 
    title="Criptografias da APS",
    required=True)

# Cifra de cesar
caesar = cripts.add_parser(
    "caesar", 
    help="Cifra de cesar."
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
rsa_keys = cripts.add_parser(
    "rsaGK",
    help="Gerador de chaves RSA."
    )

# Criptografia RSA
rsa = cripts.add_parser(
    "rsa", 
    help="Criptografia RSA."
    )

rsa.add_argument(
    "key1",
    help="Chave publica 1 ou Chave privada 1",
    type=int
    )

rsa.add_argument(
    "key2",
    help='Chave publica 2 ou Chave privada 2',
    type=int
    )

# Vigenere
vigenere = cripts.add_parser(
    "vigenere", 
    help="Cifra de Vigenere com alfabeto padrao."
    )

vigenere.add_argument(
    "key",
    help="""
        Chave para criptografar/descriptografar 
        [digite $RANDOM$ para chaves aleatorias].
        """,
    type=str
    )

vigenere.add_argument(
    "-alphabet", 
    help="Alfabeto customizado.",
    type=str
    )

# OTP
otp = cripts.add_parser(
    "otp", 
    help="Criptografia One Time Pad."
    )

otp.add_argument(
    "key",
    help="""
        Chave para criptografar/descriptografar 
        [digite $RANDOM$ para chaves aleatorias].
        """,
    type=str
    )


if __name__ == "__main__":
    args = cript_manager.parse_args()
    argument_manipulator(**args.__dict__)
