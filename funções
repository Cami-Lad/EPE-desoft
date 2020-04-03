from random import randint

fichas = 100
rodada= 'Fase:Come out '
while (fichas>0):
    
    dado1=(randint(1,6))
    dado2=(randint(1,6))
    dados= dado1 + dado2
    
    print ("fichas:{}".format(fichas))
    print (rodada)
    
    jogar= input('Você deseja apostar ou sair do jogo? (apostar/sair) ')
    
    if jogar == 'sair':
       fichas -= fichas  
    elif jogar == 'apostar':
        tipo_aposta=input('Escolha uma aposta (Pass_line_bet, Field, Anycraps, ou Twelve): ')
        if tipo_aposta not in "Pass_line_bet, Field, Anycraps, ou Twelve":
            print ('Por favor, entre uma aposta válida')  
    
        if tipo_aposta == 'Pass_line_bet' :
            aposta= int(input('Quanto você deseja apostar?'))
            if aposta > fichas:
                print('você não tem essa quantidade de fichas.')
            elif dados == 7 or dados ==  11:
                print ('dados:{}'.format(dados))
                print ('Você ganhou a aposta!')
                fichas += aposta 
            elif dados == 2 or dados == 3 or dados == 12:
                print ('dados:{}'.format(dados))
                print ('Você perdeu a aposta...')
                fichas -= aposta
            elif dados == 4 or dados == 5 or dados == 6 or dados == 8 or dados == 9 or dados == 10:
                print('dados:{}'.format(dados))
                rodada= 'Fase: Point'
                
                while (rodada == 'Fase: Point'):
                    print (rodada)
                    d1=(randint(1,6))
                    d2=(randint(1,6))
                    dt= d1+ d2
                    print('dados:{}'.format(dt))
                    if dt == 7:
                        fichas -= aposta
                        print ("Você perdeu a aposta...")
                        rodada= 'Fase:Come out'
                    elif dt == dados:
                        rodada= 'Fase:Come out'
                        fichas += aposta
                        print ('Você ganhou a aposta!')
                    else:
                        print ('Tente novamente.')

        if tipo_aposta == 'Field':
            aposta= int(input('Quanto você deseja apostar?'))
            if aposta > fichas:
                print('você não tem essa quantidade de fichas.')
            elif dados == 5 or dados == 6 or dados == 7 or dados == 8 :
                print (dados)
                fichas -= aposta
                print ("Você perdeu a aposta...")
            elif dados == 3 or dados == 4 or dados == 9 or dados == 10 or dados == 11:
                print (dados)
                fichas += fichas 
                print ('Você ganhou a aposta!')
    
            elif dados == 2:
                print (dados)
                fichas += aposta*2 
                print ("Você ganhou 2X a aposta!")
    
            elif dados == 12:
                print (dados)
                fichas += aposta*3
                print("Você ganhou 3X a aposta!")

        if tipo_aposta == 'Anycraps':
            aposta= int(input('Quanto você deseja apostar?'))
            if aposta > fichas:
                print('você não tem essa quantidade de fichas.')
            elif dados == 2 or dados == 3 or dados == 12:
                print (dados)
                fichas += aposta*7
                print ("Ganhou a aposta!")
            else:
                print (dados) 
                fichas -= aposta
                print ("Você perdeu a aposta...") 

        if tipo_aposta == 'Twelve':
            aposta= int(input('Quanto você deseja apostar?'))
            if aposta > fichas:
                print('você não tem essa quantidade de fichas.')
            elif dados == 12:
                print (dados)
                fichas += aposta*30
                print("Ganhou a aposta!")
            else:
                print (dados)
                fichas -= aposta
                print ("Você perdeu a aposta...")
        if fichas <= 0:
            print('Você ficou sem fichas.')   
    else:
        print('Por favor, entre uma resposta válida')  

print ("Por hoje é só pessoal!")
