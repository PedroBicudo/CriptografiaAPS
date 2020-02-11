from criptografiaAps import AbstractCriptModel

class Vigenere(AbstractCriptModel):
    
    def _get_letter(self, letter_pos, key_pos, operator, alphabet):
        """Obter a nova letra apos a encriptacao/desencriptacao.

        Parameters
        ----------
        letter_pos: int
            Posicao da letra.

        key_pos: int
            Posicao da chave.

        operator: function
            Operacao a ser realizada.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Letra do alfabeto.

        """
        return alphabet[operator(letter_pos, key_pos) % len(alphabet)]

    def _get_word(self, msg, key, operator, alphabet):
        """Obter a palavra criptografada/descriptografada.

        Parameters
        ----------
        msg: str
            Mensagem qualquer.

        key: str
            Chave para encriptacao/decriptacao.

        operator: function
            Operacao a ser realizada.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Texto encriptado/decriptado.
        """
        new_msg = ""
        for index, letter in enumerate(msg):
            letter_pos = alphabet.index(letter)
            key_pos = alphabet.index(key[index])
            new_msg += self._get_letter(
                letter_pos, key_pos,
                operator, alphabet
                )
        return new_msg
