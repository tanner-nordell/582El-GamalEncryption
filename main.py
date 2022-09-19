# Press the green button in the gutter to run the script.
from elgamal import keygen, encrypt, decrypt

if __name__ == '__main__':
    keys = keygen()
    print(keys)
    m = 10000001
    c = encrypt(keys[0], m)
    print(c)
    print(decrypt(keys[1], c))
