from Bio import SeqIO

#setando caminho do arquivo

caminhoDoArquivo = 'data/gene.fna'

#realizando leitura do arquivo fna
nucleotideo = []
with open(caminhoDoArquivo, 'r') as arquivo:
    for sequencia in SeqIO.parse(arquivo, 'fasta'):
        nucleotideo.append(str(sequencia.seq))

# Método responsável pela transcrição
def transcricao(nucleotideo):
    genomaTranscrito = []
    transcricaoSeq = []
    for seq in nucleotideo: # Inteirando sobre o arquivo fasta
        for nucleotideo in seq:# Inteirando no método transcrição # n²
            if nucleotideo == 'T':
                transcricaoSeq.append('A')
            elif nucleotideo == 'A':
                transcricaoSeq.append('U')
            elif nucleotideo == 'G':
                transcricaoSeq.append('C')
            elif nucleotideo == 'C':
                transcricaoSeq.append('G')
    genomaTranscrito.append(''.join(transcricaoSeq)) # Cocatena os nucleotídeos em uma única string.
        
    print(genomaTranscrito)
    
                    

transcricao(nucleotideo)
