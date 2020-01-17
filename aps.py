"""Manipular parametros de linha de comando."""
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