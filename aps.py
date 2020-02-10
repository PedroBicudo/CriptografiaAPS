"""Manipular parametros de linha de comando."""
from criptografiaAps import argument_manipulator
import argparse

cript_manager = argparse.ArgumentParser(
    description="Criptografias desenvolvidas pelo grupo da APS.",
)

required_args = cript_manager.add_argument_group("Parametros Obrigatorios")

# Argumentos para entrada de texto
input_arg = required_args.add_mutually_exclusive_group(required=True)
input_arg.add_argument(
    "-txt",
    help="Texto a ser criptografado/descriptografado.",
    type=str,
    dest="inpt"
)
input_arg.add_argument(
    "-iF",
    help="Arquivo a ser criptografado/descriptografado.",
    type=argparse.FileType('r', encoding='utf-8'),
    dest="inpt"
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

# César
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
    type=str,
    dest='custom_alphabet'
    )

if __name__ == "__main__":
    args = cript_manager.parse_args()
    argument_manipulator(**args.__dict__)
