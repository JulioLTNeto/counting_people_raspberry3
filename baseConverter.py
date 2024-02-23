import base64

def converter():
    # Caminho para o arquivo de imagem que você deseja converter
    caminho_imagem = 'imagens/entrada.jpg'

    # Abra o arquivo de imagem em modo binário
    with open(caminho_imagem, 'rb') as arquivo_imagem:
        # Leia o conteúdo do arquivo
        imagem_binaria = arquivo_imagem.read()

    # Converta a imagem binária em base64
    imagem_base64 = base64.b64encode(imagem_binaria).decode('utf-8')

    # Imprima a representação em base64 da imagem
    # print(imagem_base64)
    return imagem_base64
