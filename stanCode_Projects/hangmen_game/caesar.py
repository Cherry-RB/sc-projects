"""
File: caesar.py
Name:Cherry
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    step:
        1.according to the secret_number, make the new_alphabet
        2.make the new string(the deciphered string)
    """
    secret_number = int(input('Secret number:'))  # how much the ciphered move(平移多少？)
    ciphered = input('What\'s the ciphered string?')  # the ciphered string(需要解密的字串)
    ciphered = ciphered.upper()  # make sure the ciphered string is capital letter(把需要解密的字串變成大寫)
    deciphered = caesar(secret_number, ciphered)  # decipher function
    print('The deciphered string is: '+deciphered)  # get the deciphered string(得到解密完後的字串)


def caesar(secret_number, ciphered):
    """
    decipher the ciphered string
    :param secret_number:int
    :param ciphered:string
    :return:deciphered string
    """
    # step1.according to the secret_number, make the new_alphabet
    new_alphabet = ALPHABET[len(ALPHABET)-secret_number:]+ALPHABET[:len(ALPHABET)-secret_number]
    # step2.make the new string(the deciphered string)
    deciphered = ''
    for i in range(len(ciphered)):
        if ciphered[i].isalpha():  # make sure that we are operating the alphabet
            j = new_alphabet.find(ciphered[i])
            deciphered += ALPHABET[j]
        else:  # if the ciphered string have other word, let it keep
            deciphered += ciphered[i]
    return deciphered


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
