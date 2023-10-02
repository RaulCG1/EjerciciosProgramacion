
def funcion(lista:list,num: int):

    def back(start:int,combinacion:list,objetivo:int):
        #encontrar solucion

        if objetivo ==0:  
            devolver.append(combinacion[:])
            return
        
        #no solucion
        if objetivo < 0 or start == len(lista):
            return []
        #backtrack
        for index in range(start,len(lista)):

            if index > start and lista[index] == lista[index - 1]:
                continue
            combinacion.append(lista[index])
            back(index + 1 ,combinacion, objetivo - lista[index])
            combinacion.pop()
    
    lista.sort()
    devolver= []
    back(0,[],num)

    return devolver

lista=[1,5,3,2]

print(funcion(lista,7))

    