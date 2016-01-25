#   Universidad Nacional Autonoma de Mexico

#       Julio Cesar Guzman Villanueva

#        Reconocimiento de Patrones

#               Perceptron

def producto_interno(vectorA, vectorB):
    resultado = 0
    if len(vectorA) == len(vectorB):
        leng = len(vectorA)
        for i in range(leng):
            resultado = resultado + vectorA[i] * vectorB[i]
    else:
        print('error 1')
    return resultado

def suma(vectorA, vectorB):
    vectorC = []
    if len(vectorA) == len(vectorB):
        leng = len(vectorA)
        for i in range(leng):
            vectorC.append(vectorA[i] + vectorB[i])
    else:
        print('error 2')
    return vectorC

def resta(vectorA, vectorB):
    vectorC = []
    if len(vectorA) == len(vectorB):
        leng = len(vectorA)
        for i in range(leng):
            vectorC.append(vectorA[i] - vectorB[i])
    else:
        print('error 3')
    return vectorC

def multiplicacion_escalar(vectorA, escalar):
    resultado = []
    for i in range(len(vectorA)):
        resultado.append( vectorA[i] * escalar )
    return resultado

clases = {}

#Ejercicio del libro

w1 = clases['w1'] = [ [0,1,1], [0,2,1], [1,2,1] ]
w2 = clases['w2'] = [ [1,0,1], [2,0,1], [2,1,1] ]

w = [ 0, 1, 1 ]

#Ejercicio visto en clase

#w1 = clases['w1'] = [ [0,0,1], [0,1,1] ]
#w2 = clases['w2'] = [ [1,0,1], [1,1,1] ]
#w = [ 0, 0, 1 ]

iteraciones = 10

for i in range(iteraciones):
    for clase in clases:
        elementos_de_clase = clases[clase]
        for elemento in elementos_de_clase:
            x = elemento
            p = producto_interno(w,x)
            if x in w1 and p <= 0 :
                w = suma( w , x )
            if x not in w1 and p >= 0:
                w = resta( w , x )
            else:
                w = w
print(w)
