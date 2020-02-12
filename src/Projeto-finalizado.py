import cv2
import matplotlib.pyplot as plt
from math import log
#Filtro da medianna
def faz_matriz(l,c, canal): #linhas, colunas e canal
    m = []
    for i in range(l):
        m.append([])
        for j in range(c):
            m[i].append(img.item(i,j, canal))
    return m

def calcula_mediana(m, l, c): #matriz, linhas e colunas
    lista = [m[l][c],m[l-1][c-1],m[l-1][c],m[l-1][c+1],m[l][c-1],m[l][c+1],m[l+1][c-1],m[l+1][c],m[l+1][c+1]]
    lista.sort()
    return lista[4]

def pixel_to_mediana(canal, matriz): #percorrer a lista mudando cada pixel por sua mediana(matriz e canal de cor)
    for i in range(1, linhas-1):
        for j in range(1, colunas-1):
            pixel = calcula_mediana(matriz, i, j)
            matriz[i][j] = pixel
            img.itemset(i,j,canal, pixel)

def calcula_media(m, l, c): #matriz, linhas e colunas
    lista = [m[l][c],m[l-1][c-1],m[l-1][c],m[l-1][c+1],m[l][c-1],m[l][c+1],m[l+1][c-1],m[l+1][c],m[l+1][c+1]]
    lista.sort()
    return sum(lista)/9

def pixel_to_media(canal, matriz): #percorrer a lista mudando cada pixel por sua mediana(matriz e canal de cor)
    for i in range(1, linhas-1):
        for j in range(1, colunas-1):
            pixel = calcula_media(matriz, i, j)
            matriz[i][j] = pixel
            img.itemset(i,j,canal, pixel)

def kuwahara(m, canal):
    somatorio1 = 0
    somatorio2 = 0
    somatorio3 = 0
    somatorio4 = 0
    for i in range(2, linhas-2):
        for j in range(2, colunas-2):
            listaA = [m[i-2][j-2] , m[i-2][j-1] , m[i-2][j] , m[i-1][j-2] , m[i-1][j-1] , m[i-1][j] , m[i][j-2] , m[i][j-1] , m[i][j]]
            listaB = [m[i-2][j], m[i-2][j+1] , m[i-2][j+2] , m[i-1][j] , m[i-1][j+1] , m[i-1][j+2], m[i][j+1] , m[i][j+2]]
            listaC = [m[i][j-2] , m[i][j-1], m[i][j] , m[i+1][j-2] , m[i-1][j-1], m[i+1][j], m[i+2][j-2], m[i+2][j-1], m[i+2][j]]
            listaD = [m[i][j], m[i][j+1], m[i][j+2], m[i+1][j], m[i+1][j+1], m[i+1][j+2], m[i+2][j], m[i+2][j+1], m[i+2][j+2]]

            mediaA = sum(listaA)/9
            mediaB = sum(listaB)/9
            mediaC = sum(listaC)/9
            mediaD = sum(listaD)/9

            for k in listaA:
                somatorio1 += (k - mediaA)**2

            for k in listaB:
                somatorio2 += (k - mediaB)**2

            for k in listaC:
                somatorio3 += (k - mediaC)**2

            for k in listaD:
                somatorio4 += (k - mediaD)**2

            DP1 = somatorio1**(1/2)
            DP2 = somatorio2**(1/2)
            DP3 = somatorio3**(1/2)
            DP4 = somatorio4**(1/2)

            desvios  = [DP1,DP2,DP3,DP4]
            medias = [mediaA,mediaB,mediaC,mediaD]
            comparador = 0

            for k in desvios:
                if comparador == 0:
                    comparador = k

                elif comparador > k:
                    comparador = k

            pixel = 0
            if comparador == DP1:
                    pixel = mediaA

            elif comparador == DP2:
                    pixel = mediaB

            elif comparador == DP3:
                    pixel = mediaC

            elif comparador == DP4:
                    pixel = mediaD
            img.itemset(i,j,canal, pixel)


def kuwahara_3x3(m, canal):
    somatorio1 = 0
    somatorio2 = 0
    somatorio3 = 0
    somatorio4 = 0
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            listaA = [m[i-1][j-1], m[i-1][j], m[i][j-1], m[i][j]]
            listaB = [m[i-1][j], m[i-1][j+1], m[i][j+1], m[i][j]]
            listaC = [m[i][j-1], m[i][j],m[i+1][j-1],m[i+1][j]]
            listaD = [m[i][j],m[i+1][j+1],m[i][j+1],m[i+1][j+1]]

            mediaA = sum(listaA) /4
            mediaB = sum(listaB) / 4
            mediaC = sum(listaC) / 4
            mediaD = sum(listaD) / 4

            for k in listaA:
                somatorio1 += (k - mediaA)**2

            for k in listaB:
                somatorio2 += (k - mediaB)**2




            for k in listaC:
                somatorio3 += (k - mediaC)**2

            for k in listaD:
                somatorio4 += (k - mediaD)**2

            DP1 = somatorio1 ** (1 / 2)
            DP2 = somatorio2 ** (1 / 2)
            DP3 = somatorio3 ** (1 / 2)
            DP4 = somatorio4 ** (1 / 2)

            desvios = [DP1, DP2, DP3, DP4]
            medias = [mediaA, mediaB, mediaC, mediaD]
            comparador = 0

            for k in desvios:
                if comparador == 0:
                    comparador = k

                elif comparador > k:
                    comparador = k

            pixel = 0
            if comparador == DP1:
                pixel = mediaA

            elif comparador == DP2:
                pixel = mediaB

            elif comparador == DP3:
                pixel = mediaC

            elif comparador == DP4:
                pixel = mediaD
            img.itemset(i, j, canal, pixel)


#E
#for c in range(img.shape[2]):
#  pixel_to_mediana(c)

#Histograma

def pixels_de_matriz(canal):
    m= [] #lista com todos os pixels de um determinado canal
    for i in range(linhas):
        for j in range(colunas):
            m.append(img.item(i,j,canal))
    return m

def PSNR (M,m):
    soma_mse=0
    calculo_mse =0
    for i in range(linhas):
        for j in range(colunas):
            soma_mse+=(M[i][j]-m[i][j])**2
    calculo_mse = soma_mse/(linhas*colunas)
    psnr =20*(log(255/(calculo_mse**(1/2)),10))
    return psnr


def histograma (pixelsR,pixelsG,pixelsB):
        plt.subplot(221),plt.hist(pixelsR, bins=range(256), color='r'), plt.title('R')
        plt.xticks(), plt.yticks()
        plt.subplot(222), plt.hist(pixelsG, bins=range(256),color='g'), plt.title('G')
        plt.xticks(), plt.yticks()
        plt.subplot(223), plt.hist(pixelsB, bins=range(256),color='b'), plt.title('B')
        plt.xticks(), plt.yticks()
        plt.subplot(224), plt.hist(pixelsB, bins=range(256),color='b'), plt.hist(pixelsG, bins=range(256),color='g'), plt.hist(pixelsR, bins=range(256), color='r'),plt.title('RGB')
        plt.xticks(), plt.yticks()
        plt.show()

def psnr_total(mB,mG,mR):
    p =(PSNR(mB,matrizBO)+PSNR(mG,matrizGO)+PSNR(mR,matrizRO))/3
    return p

#for i in range(img.shape[2]):
#  pixels_de_matriz(linhas,colunas,i)


while True:
    try:
        nome_img = input('Nome da imagem: ').lower()
        img = cv2.imread(nome_img)
        tamanho = img.shape
        break
    except AttributeError:
        print('Coloque uma imagem presente na pasta do programa!')

linhas = img.shape[0]
colunas = img.shape[1]

matrizBO = faz_matriz(linhas,colunas,0)
matrizGO = faz_matriz(linhas,colunas,1)
matrizRO = faz_matriz(linhas,colunas,2)

Pr = pixels_de_matriz(2)
Pg = pixels_de_matriz(1)
Pb = pixels_de_matriz(0)

histograma(Pr,Pg,Pb)

while True:
    funcao_programa = input('Digite o numero correspondente a operação: \n'
                            '1 - Filtro da mediana\n'
                            '2 - Filtro da media\n'
                            '3 - Filtro de Kuwahara (5x5)\n'
                            '4 - Filtro de Kuwahara(3x3)\n'
                            '5 - Sair\n').strip()


    img_original = cv2.imread(nome_img)
    img = cv2.imread(nome_img)

    matrizB = faz_matriz(linhas,colunas,0)
    matrizG = faz_matriz(linhas,colunas,1)
    matrizR = faz_matriz(linhas,colunas,2)

    if funcao_programa == '1':
        img = cv2.imread(nome_img)

        pixel_to_mediana(0, matrizB)
        pixel_to_mediana(1, matrizG)
        pixel_to_mediana(2, matrizR)

        cv2.imshow('Original', img_original)
        cv2.waitKey(1)

        print('PSNR Imagem pós filtro = {:.3f} dB'.format(psnr_total(matrizB,matrizR,matrizG)))
        cv2.imshow('Depois do filtro.jpg', img)
        cv2.waitKey(1)
        Pr = pixels_de_matriz(2)
        Pg = pixels_de_matriz(1)
        Pb = pixels_de_matriz(0)

        histograma(Pr,Pg,Pb)
        matrizB = matrizBO
        matrizG = matrizGO
        matrizR = matrizRO
        cv2.destroyAllWindows()

    elif funcao_programa == '2':
        img = cv2.imread(nome_img)

        pixel_to_media(0, matrizB)
        pixel_to_media(1, matrizG)
        pixel_to_media(2, matrizR)

        cv2.imshow('Original', img_original)
        cv2.waitKey(1)

        print('PSNR Imagem pós filtro = {:.3f} dB'.format(psnr_total(matrizB,matrizR,matrizG)))
        cv2.imshow('Depois do filtro.jpg', img)
        cv2.waitKey(1)
        Pr = pixels_de_matriz(2)
        Pg = pixels_de_matriz(1)
        Pb = pixels_de_matriz(0)

        histograma(Pr,Pg,Pb)
        matrizB = matrizBO
        matrizG = matrizGO
        matrizR = matrizRO
        cv2.destroyAllWindows()



    elif funcao_programa == '3':
        img = cv2.imread(nome_img)

        kuwahara(matrizB,0)
        kuwahara(matrizG,1)
        kuwahara(matrizR,2)


        matrizB = faz_matriz(linhas,colunas,0)
        matrizG = faz_matriz(linhas,colunas,1)
        matrizR = faz_matriz(linhas,colunas,2)

        print('PSNR Imagem pós filtro = {:.3f} dB'.format(psnr_total(matrizB,matrizR,matrizG)))
        cv2.imshow('Original', img_original)
        cv2.waitKey(1)

        cv2.imshow('Depois do filtro', img)
        cv2.waitKey(1)
        Pr = pixels_de_matriz(2)
        Pg = pixels_de_matriz(1)
        Pb = pixels_de_matriz(0)
        histograma(Pr,Pg,Pb)
        cv2.destroyAllWindows()

    elif funcao_programa == '4':
        img = cv2.imread(nome_img)

        kuwahara_3x3(matrizB, 0)
        kuwahara_3x3(matrizG, 1)
        kuwahara_3x3(matrizR, 2)

        matrizB = faz_matriz(linhas,colunas,0)
        matrizG = faz_matriz(linhas,colunas,1)
        matrizR = faz_matriz(linhas,colunas,2)

        print('PSNR Imagem pós filtro = {:.3f} dB'.format(psnr_total(matrizB,matrizR,matrizG)))

        cv2.imshow('Original', img_original)
        cv2.waitKey(1)

        cv2.imshow('Depois do filtro', img)
        cv2.waitKey(1)
        Pr = pixels_de_matriz(2)
        Pg = pixels_de_matriz(1)
        Pb = pixels_de_matriz(0)
        histograma(Pr,Pg,Pb)
        cv2.destroyAllWindows()

    elif funcao_programa == '5':
        print("FIM")
        break

    else:
        print('Digite um comando válido!')

