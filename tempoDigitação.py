
def cont_tempo():
    inicio = time.clock()
    input('Escreva seu nome:')
    fim = time.clock()
    tempo = fim - inicio
    print('Voce levou'+srt(tempo) +' segundos para escrever o seu nome')
    
