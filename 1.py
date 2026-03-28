import os

dir:str = "/tmp/exercicios/"
arq:str ="ex34.txt"

def mult(vlr, tab):
    res = (vlr * tab)
    return res

def grava(c, result):
    global dir
    global arq
    file:str =''
    tipo:str =''
    enc:str =''
    linha:str =''

    linha = str(result) + "\n"

    if os.path.exists(dir) and os.path.isdir(dir):
        arquivo = dir + arq
        if os.path.exists(arquivo):
            if c > 0:
                tipo = 'a'
            else:
                tipo = 'w'
        else:
            tipo = 'w'
    
    with open(arquivo, tipo) as file:
        file.write(linha)

def main():
    pasta = "/tmp/exercicios/"
    os.makedirs(pasta, exist_ok=True)
    os.chmod(pasta, 0o744)

    valor = int(input("Digite um valor de 1 a 10:"))
    for contador in range(1,11):
        result = mult(valor, contador)
        grava(contador, result)
    

if __name__ == "__main__":
    main()