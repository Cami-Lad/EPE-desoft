from random import randint

def Field(dados):
    if dados == 5 or dados == 6 or dados == 7 or dados == 8 :
        return -1
    elif dados == 3 or dados == 4 or dados == 9 or dados == 10 or dados == 11:
        return 1
    elif dados == 2:
        return 2
    elif dados == 12:
        return 3

def Anycraps(dados):
    if dados == 2 or dados == 3 or dados == 12:
        return 7
    else: 
        return -1
        
def Twelve(dados):
    if dados == 12:
        return 30
    else:
        return -1

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
        tipo_aposta=input('Escolha uma aposta (Pass_line_bet/Field/Anycraps/Twelve): ')

        if 'Field' in tipo_aposta:
            aposta_Field = int(input('Quanto você deseja apostar em Field?'))
            resultadoF = Field(dados)
            if aposta_Field > fichas:
                print('você não tem essa quantidade de fichas.')
            else:
               if resultadoF > 0:
                   print('Você ganhou a aposta Field!')
               else:
                   print('você perdeu a aposta Field...')

                   fichas += aposta_Field*resultadoF
    
        if 'Anycraps' in tipo_aposta:
            aposta_Anycaps = int(input('Quanto você deseja apostar em Anycraps?'))
            resultadoA = Anycraps(dados)
            if aposta_Anycaps > fichas:
                print('você não tem essa quantidade de fichas.')
            else:
                if resultadoA > 0:
                   print('Você ganhou a aposta Anycraps!')
                else:
                 print('você perdeu a aposta Anycraps...')

                 fichas += aposta_Anycaps*resultadoA

        if 'Twelve' in tipo_aposta:
            aposta_Twelve = int(input('Quanto você deseja apostar em Twelve?'))
            resultadoT = Twelve(dados)
            if aposta_Twelve > fichas:
                print('você não tem essa quantidade de fichas.')
            else:
                if resultadoT > 0:
                    print('Você ganhou a aposta Twelve!')
                else:
                    print('você perdeu a aposta Twelve...')

                    fichas += aposta_Twelve*resultadoT

        if 'Pass_line_bet' in tipo_aposta:
            aposta_Pass_line_bet= int(input('Quanto você deseja apostar em Pass_line_bet?'))
            if aposta_Pass_line_bet > fichas:
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
        
        if fichas <= 0:
            print('Você ficou sem fichas.')   

        elif 'Pass_line_bet' not in tipo_aposta and 'Field' not in tipo_aposta and 'Anycraps' not in tipo_aposta and 'Twelve' not in tipo_aposta: 
            print('Por favor, entre uma aposta válida') 

    else:
        print('Por favor, entre uma resposta válida')  

print ("Por hoje é só, pessoal!")
