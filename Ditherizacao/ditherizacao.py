import numpy as np

#ditherizacao: função que aplica o algoritmo de ditherização de Floyd-Steinberg
def ditherizacao(matriz_img): 
    matriz_img = matriz_img.astype(np.float32)
    altura, largura = matriz_img.shape

    for i in range(altura):
        for j in range(largura):

            # aplica quatização do pixel
            # Se o pixel for menor que 128, torna-o preto (0), caso contrário, branco (255)
            old_pixel = matriz_img[i, j]
            new_pixel = 0 if old_pixel < 128 else 255

            # Calculo o erro entre o pixel original e o pixel quantizado
            matriz_img[i, j] = new_pixel
            error = old_pixel - new_pixel

            # Distribui o erro para os pixels vizinhos
            if j + 1 < largura:
                matriz_img[i, j + 1] += error * 7 / 16
            if i + 1 < altura:
                matriz_img[i + 1, j] += error * 5 / 16
                if j > 0:
                    matriz_img[i + 1, j - 1] += error * 3 / 16
                if j + 1 < largura:
                    matriz_img[i + 1, j + 1] += error * 1 / 16

    return np.clip(matriz_img, 0, 255).astype(np.uint8)        
