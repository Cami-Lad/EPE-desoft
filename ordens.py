from randint import random




while (fichas != 0) or (jogar == sair ) :

    dado1=(randint (1,6))
    dado2=(randint (1,6))
    dados= dado1 + dado2

    jogar= input('Você deseja apostar ou sair do jogo ?')
    if jogar == 'sair':
       fichas -= fichas  
    elif jogar == 'sim'
        aposta=insput('Escolha uma aposta: Pass_line_bet, Field, Anycraps, ou Twelve')
        
        if aposta == 'Pass_line_bet' :
            if dados= 7 or 11:
                fichas += aposta 
            if dados == 2 or 3 or 12:
                fichas -= aposta
            if dados == 4 or 5 or 6 or 8 or 10:
                dados = point
                
                while (dt != point):
                    d1=(randint (1,6))
                    d2=(randint (1,6))
                    dt= d1+ d2
                    print (dt)
                    if dt == 7:
                        fichas -= aposta
                        print ("Você perdeu a aposta") 
                    if dt != point:
                        print ('Tente novamente')
                     


        if aposta == 'Field':

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

        if aposta == 'Anyncraps':

            if dados == 2 or 3 or 12:
                fichas += aposta*7
            print ("Ganhou a aposta")
    
            else: 
                fichas -= aposta
                print ("Você perdeu a aposta") 

        if aposta == 'Twelve':

            if dados == 12:
                fichas += aposta*30
                print("ganhou a aposta")
    
            else:
                fichas -= aposta

print ("Até a próxima!")


