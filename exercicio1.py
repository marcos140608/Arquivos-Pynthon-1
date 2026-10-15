import os

valor: int = 0
dir: str = ''
arq: str = ''


def criar_pasta():
    pasta = '/tmp/exercicios'
    os.makedirs(pasta, exist_ok=True)
    os.chmod(pasta, 0o744)


def mult(vlr: int, tab: int) -> int:
    res: int = vlr * tab
    return res


def grava(c: int, rslt: int):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    linha = str(rslt) + '\n'
    file = dir + '/' + arq

    if os.path.exists(dir) and os.path.isdir(dir):
        tipo = 'w'
        enc = 'utf-8'
        if os.path.exists(file):
            if c > 0:
                tipo = 'a'
        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha)
    else:
        print("Diretório inválido")


def main():
    global valor, dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'

    contador: int = 0
    result: int = 0

    criar_pasta()

    valor = int(input("Digite um valor entre 1 e 10: "))
    while valor < 1 or valor > 10:
        valor = int(input("Valor inválido. Digite um valor entre 1 e 10: "))

    while contador < 10:
        result = mult(valor, contador + 1)
        print(f"{valor} x {contador + 1} = {result}")
        grava(contador, result)
        contador += 1


if __name__ == "__main__":
    main()
