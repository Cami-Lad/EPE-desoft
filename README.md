# EPE-desoft
trabalho de despft, junção dos códigos. 


fichas = 100
fase = 
aposta= 
dados= 

#field

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



#anycraps 

if dados == 2 or 3 or 12:
    fichas += aposta*7
    print ("Ganhou a aposta")
    
else: 
    fichas -= aposta 
