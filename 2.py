import os

nome: str = ''
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0 
valor_media: float = 0
dir: str = '/tmp/exercicios/'
arq: str = 'ex21.txt'

def escreveArq(caminho, arquivo, linha_arq):
    file:str = ''
    tipo:str = ''
    enc:str = ''

    if os.path.exists(dir) and os.path.isdir(dir):
        arquivo = dir + arq
        if os.path.exists(arquivo):
            tipo = 'a'
        else:
            tipo = 'w'

    with open(arquivo, tipo) as file:
        file.write(linha_arq)

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global arq, dir
    linha:str = ''
    linha = nm + '\n' + str(nt1) + '\n' + str(nt2) + '\n' + str(nt3) + '\n' + str(nt4) + '\n' + str(vlr_med) + '\n'
    escreveArq(dir, arq, linha)

def med(n1, n2, n3, n4):
    media: float = 0
    media = (n1 + n2 + n3 + n4) / 4
    return media

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    nome = str(input("Digite o nome:"))
    nota1 = float(input("Digite a nota1:"))
    nota2 = float(input("Digite a nota2:"))
    nota3 = float(input("Digite a nota3:"))
    nota4 = float(input("Digite a nota4:"))
    valor_media = med(nota1, nota2, nota3, nota4)
    
    print(valor_media)
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    pasta ='/tmp/exercicios/'
    os.makedirs(pasta, exist_ok=True)
    os.chmod(pasta, 0o744)

    for contador in range(1, 6):
        entrada()

if __name__ == '__main__':
    main()