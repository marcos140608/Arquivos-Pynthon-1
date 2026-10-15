import os

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''


def criar_pasta():
    pasta = '/tmp/exercicios'
    os.makedirs(pasta, exist_ok=True)
    os.chmod(pasta, 0o744)


def med(n1: float, n2: float, n3: float, n4: float) -> float:
    media: float = (n1 + n2 + n3 + n4) / 4
    return media


def escreveArq(caminho: str, arquivo: str, linha_arq: str):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    file = caminho + '/' + arquivo

    if os.path.exists(caminho) and os.path.isdir(caminho):
        tipo = 'w'
        enc = 'utf-8'
        if os.path.exists(file):
            tipo = 'a'
        with open(file, tipo, encoding=enc) as f:
            f.write(linha_arq)
    else:
        print("Diretório inválido")


def cadastro(nm: str, nt1: float, nt2: float, nt3: float, nt4: float, vlr_med: float):
    global dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex21.txt'

    linha: str = ''
    linha = (nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';'
             + str(nt4) + ';' + str(vlr_med) + '\n')

    escreveArq(dir, arq, linha)


def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    valor_media = med(nota1, nota2, nota3, nota4)
    print(f"Média de {nome}: {valor_media}")

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def main():
    contador: int = 0
    criar_pasta()
    while contador < 5:
        entrada()
        contador += 1


if __name__ == "__main__":
    main()
