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