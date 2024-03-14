from Bio import SeqIO

#setando caminho do arquivo

caminhoDoArquivo = 'data/gene.fna'

#realizando leitura do arquivo fna

with open(caminhoDoArquivo, 'r') as arquivo:
    for sequencia in SeqIO.parse(arquivo, 'fasta'):
        
