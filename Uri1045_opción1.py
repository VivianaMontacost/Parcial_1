ladoa,ladob,ladoc=list(map(float,input().split()))
if(ladoa < ladob):
    temp = ladoa
    ladoa = ladob
    ladob = temp
if(ladob < ladoc):
    temp = ladob
    ladob = ladoc
    ladoc = temp
if(ladoa < ladob):
    temp = ladoa
    ladoa = ladob
    ladob = temp
if(ladoa>=(ladob+ladoc)):
    print("NAO FORMA TRIANGULO")
elif(ladoa*ladoa == (ladob*ladob+ladoc*ladoc)):
     print("TRIANGULO RETANGULO")
elif(ladoa*ladoa > (ladob*ladob + ladoc*ladoc)):
    print("TRIANGULO OBTUSANGULO")
elif(ladoa*ladoa<(ladob*ladob + ladoc*ladoc)):
    print("TRIANGULO ACUTANGULO")
if(ladoa == ladob and ladob == ladoc):
        print("TRIANGULO EQUILATERO")
elif(ladoa == ladob or ladob == ladoc):
        print("TRIANGULO ISOSCELES")