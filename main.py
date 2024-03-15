from Bio import SeqIO

#setando caminho do arquivo

caminhoDoArquivo = 'data/gene.fna'

#realizando leitura do arquivo fna
memoria = []
with open(caminhoDoArquivo, 'r') as arquivo:
    for sequencia in SeqIO.parse(arquivo, 'fasta'):
        memoria.append(str(sequencia.seq))
        print(memoria)

