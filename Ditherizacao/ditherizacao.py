import numpy as np

#ditherizacao dos canais 
def ditherizacao(canal): 
    canal = canal.astype(np.float32)
    altura, largura = canal.shape

    for i in range(altura):
        for j in range(largura):

            old_pixel = canal[i, j]
            new_pixel = 0 if old_pixel < 128 else 255
            canal[i, j] = new_pixel
            error = old_pixel - new_pixel

            # Distribui o erro para os pixels vizinhos
            if j + 1 < largura:
                canal[i, j + 1] += error * 7 / 16
            if i + 1 < altura:
                canal[i + 1, j] += error * 5 / 16
                if j > 0:
                    canal[i + 1, j - 1] += error * 3 / 16
                if j + 1 < largura:
                    canal[i + 1, j + 1] += error * 1 / 16

    return np.clip(canal, 0, 255).astype(np.uint8)        
