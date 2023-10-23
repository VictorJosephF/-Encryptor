import os


def criar_chave():
    chave = {}
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(len(alfabeto)):
        letra_original = alfabeto[i]
        letra_criptografada = alfabeto[(i + 3) % len(alfabeto)]
        chave[letra_original] = letra_criptografada
    return chave


def criptografar(frase, chave):
    tradutor = ""
    for letra in frase:
        if letra in chave:
            tradutor += chave[letra]
        else:
            tradutor += letra
    return tradutor


def descriptografar(frase, chave):
    chave_inversa = {v: k for k, v in chave.items()}
    tradutor = ""
    for letra in frase:
        if letra in chave_inversa:
            tradutor += chave_inversa[letra]
        else:
            tradutor += letra
    return tradutor


chave = criar_chave()

case = input("Digite C para Criptografar uma frase ou D para desencriptar uma frase: ")
if case == "C":

    frase_original = input("Digite sua frase: ")
    frase_encriptada = criptografar(frase_original, chave)
    print("Texto encriptado:", frase_encriptada)
elif case == "D":
    frase_encriptada = input("Digite o texto encriptado: ")
    frase_descriptada = descriptografar(frase_encriptada, chave)
    print("Texto descriptografado:", frase_descriptada)
