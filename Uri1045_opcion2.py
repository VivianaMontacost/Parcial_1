medidas=input("")
(x,y,z)=medidas.split(" ")
x=float(x)
y=float(y)
z=float(z)
if (x==y==z):
    A=x
    B=y
    C=z
elif (x>=y and x>=z and y>=z):
    A=x
    B=y
    C=z
elif (x>=y and x>=z and z>=y):
    A=x
    B=z
    C=y
elif (y>=x and y>=z and z>=y):
    A=y
    B=x
    C=z
elif (y>=x and y>=z and z>=x):
    A=y
    B=z
    C=x
elif (y>=x and y>=z and z<=x):
    A=y
    B=x
    C=z
elif (z>=x and z>=y and x>=y):
    A=z
    B=x
    C=y
elif (z>=x and z>=y and y>=x):
    A=z
    B=y
    C=x
if(A>=B+C):
    print("NAO FORMA TRIANGULO")
else:
    if(A**2==B**2+C**2):
        print("TRIANGULO RETANGULO")
    if (A**2<B**2+C**2):
        print("TRIANGULO ACUTANGULO")
    if(A==B==C):
        print("TRIANGULO EQUILATERO")
    if (A**2>B**2+C**2):
      print("TRIANGULO OBTUSANGULO")
    if (A==B and C!=A or B==C and A!=B):
        print("TRIANGULO ISOCELES")
    
