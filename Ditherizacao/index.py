import cv2 as cv 
import numpy as np
import os
from ditherizacao import ditherizacao

# Verifica se o caminho da imagem existe
caminho_img = r"../Img/nicolas_cage.jpeg"
if not os.path.exists(caminho_img):
    print("Caminho da imagem não encontrado.")
    exit()

# Carrega a imagem 
img = cv.imread(caminho_img)
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# Exibe a imagem original
print("Imagem original, para continuar pressione qualquer tecla")
cv.imshow ('Imagem carregada', img)
cv.waitKey(4000)   
cv.destroyAllWindows()

# Captura a opção do usuário para ditherização
opcao = input("Escolha a opção de cores ('1' para Colorida , '2' para Cinza): ")

match opcao:
    case '1':  # Imagem colorida
        # # acessa a matriz de pixels da imagem
        matriz_pixels_blue = img[:, :, 0]
        # print("Matriz de pixels da imagem (blue):", matriz_pixels_blue)

        matriz_pixels_green = img[:, :, 1]
        # print("Matriz de pixels da imagem (green):", matriz_pixels_green)

        matriz_pixels_red = img[:, :, 2]
        # print("Matriz de pixels da imagem (red):", matriz_pixels_red)

        # Chama a função de ditherização para cada canal de cor
        print("ditherizando a imagem colorida")
        imagem_ditherizada__blue = ditherizacao(matriz_pixels_blue)
        imagem_ditherizada_green = ditherizacao(matriz_pixels_green)
        imagem_ditherizada_red = ditherizacao(matriz_pixels_red)

        #junta os canais ditherizados
        imagem_ditherizada_colorida = cv.merge((imagem_ditherizada__blue, imagem_ditherizada_green, imagem_ditherizada_red))

        print("Imagem ditherizada colorida")
        cv.imwrite('comp-aplicadaV/ImgDitherizada/imagem_ditherizada_colorida.png', imagem_ditherizada_colorida)
        cv.imshow ('Imagem ditherizada', imagem_ditherizada_colorida)
        cv.waitKey(4000)   
        cv.destroyAllWindows()  
        exit()


    case '2':  # Ditherização da imagem em escala de cinza
        #converte a imagem para escala de cinza
        img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Imagem em Cinza', img_cinza)
        cv.imwrite('comp-aplicadaV/Img/imagem_cinza.png', img_cinza)

        # Chama a função de ditherização para a imagem em escala de cinza
        print("ditherizando a imagem em cinza")
        imagem_ditherizada_cinza = ditherizacao(img_cinza)

        print("Imagem ditherizada em cinza")
        cv.imwrite('comp-aplicadaV/ImgDitherizada/imagem_ditherizada_cinza.png', imagem_ditherizada_cinza)
        cv.imshow ('Imagem ditherizada', imagem_ditherizada_cinza)
        cv.waitKey(4000)   
        cv.destroyAllWindows()  
        exit()

