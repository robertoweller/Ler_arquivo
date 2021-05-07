"""
Notas da disciplina

Faça um programa contendo uma função que como argumentos os nomes de dois 
arquivos. O primeiro arquivo armazena os nomes dos alunos e o segundo arquivo 
contém as respectivas notas dos alunos. O nome em uma linha do primeiro arquivo 
está associado às notas (uma ou mais) na linha correspondente do segundo arquivo.
Assuma que as notas estão separadas umas das outras por virgulas. A função deve 
ler os dois arquivos e imprimir como saída o nome do aluno e a respectiva média 
de suas notas. No programa princimpal deve ser chamado tal função.

Exemplo de arquivos de entrada:

-------------------------------
Joao                   |8,5,9            
Maria                  |9,5,5
Jose                   |8,9,3
-------------------------------


Exemplo de saída:

-------------------------------
Nome         Média

Joao         7.33
Maria        6.33
Jose         6.67
-------------------------------

"""

def leiaArquivos(nomes, notas):
    """ 
    Ler os dois arquivos e imprimir como saída o nome do aluno e a respectiva
    média de suas notas
    """
    nomes = open(nomes, 'r')
    notas = open(notas, 'r')
    listaNome = ''.join(nomes).split()
    listaNota = ''.join(notas).split()

    print(f'\n{"Nome":20}Média')

    for nm in enumerate(listaNome):
        # Convertendo cada item da lista em inteiros, pq são strings
        media = list(map(int, listaNota[nm[0]].split(',')))
        media = sum(media)/len(media)

        print(f'{nm[1]:20}{media:.2f}')
    
    nomes.close()
    notas.close()


if __name__ == "__main__":
    nomes_alunos = 'nomes_dos_alunos.txt'
    notas_alunos = 'notas_dos_alunos.txt'

    leiaArquivos(nomes_alunos, notas_alunos)

