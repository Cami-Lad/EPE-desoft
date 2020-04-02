from random import randint

fichas = 100
rodada= 'Come out'
while (fichas!=0):
    point= 0
    dado1=(randint(1,6))
    dado2=(randint(1,6))
    dados= dado1 + dado2
    print (fichas)
    jogar= input('Você deseja apostar ou sair do jogo ? ')
    if jogar == 'sair':
       fichas -= fichas  
    elif jogar == 'apostar':
        tipo_aposta=input('Escolha uma aposta: Pass_line_bet, Field, Anycraps, ou Twelve ')
        
        if tipo_aposta == 'Pass_line_bet' :
            aposta= int(input('Quanto você deseja apostar?'))
            if dados == 7 or dados ==  11:
                fichas += aposta 
            if dados == 2 or dados == 3 or dados == 12:
                fichas -= aposta
            if dados == 4 or dados == 5 or dados == 6 or dados == 8 or dados == 10:
                point == dados 
                rodada= 'point'
                
                while (rodada == 'point'):
                    d1=(randint(1,6))
                    d2=(randint(1,6))
                    dt= d1+ d2
                    print (dt)
                    if dt == 7:
                        fichas -= aposta
                        print ("Você perdeu a aposta") 
                    if dt != point:
                        print ('Tente novamente')
                    elif dt == point:
                        rodada= 'Come Out'
                     


        if tipo_aposta == 'Field':
            aposta= int(input('Quanto você deseja apostar?'))
            if dados == 5 or 6 or 7 or 8 :
                fichas -= aposta
                print ("Você perdeu a aposta")
            if dados == 3 or 4 or 9 or 10 or 11:
                fichas = fichas 
                print ("Acabou a rodada")
    
            elif dados == 2:
                fichas += aposta*2 
                print ("Você ganhou 2X a aposta")
    
            else:
                fichas += aposta*3
                print("Você ganhou 3X a aposta")

        if tipo_aposta == 'Anycraps':
            aposta= int(input('Quanto você deseja apostar?'))
            if dados == 2 or 3 or 12:
                fichas += aposta*7
                print ("Ganhou a aposta")
    
            else: 
                fichas -= aposta
                print ("Você perdeu a aposta") 

        if tipo_aposta == 'Twelve':
            aposta= int(input('Quanto você deseja apostar?'))
            if dados == 12:
                fichas += aposta*30
                print("ganhou a aposta")
    
            else:
                fichas -= aposta

print ("Até a próxima!")


