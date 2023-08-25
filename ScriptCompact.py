import sys
import os

# Check if PIL is installed
try:
    from PIL import Image
except ImportError:
    print('PIL module is not installed. Please install it and try again.')
    sys.exit()

def redimensionar_imagem(filename, pasta):
    # Check if file extension is valid
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return None
    
    with Image.open(filename) as img:
        # Define uma largura máxima de 1000 pixels
        largura_maxima = 1000
        # Redimensiona a imagem mantendo a proporção
        img.thumbnail((largura_maxima, largura_maxima), Image.ANTIALIAS)
        # Define o novo nome do arquivo
        novo_nome_arquivo = os.path.join(pasta, f"redimensionada_{os.path.basename(filename)}")
        try:
            img.save(novo_nome_arquivo, optimize=True, quality=80)
        except IOError:
            return None
        
        # Check if new file size is smaller than 1MB
        if os.path.getsize(novo_nome_arquivo) < 1000000:
            return novo_nome_arquivo
        else:
            os.remove(novo_nome_arquivo)
            return None

# Get folder containing the images to be resized from user input
pasta = input('Por favor, insira o caminho para a pasta contendo as imagens a serem redimensionadas: ')
if not os.path.exists(pasta):
    print('A pasta especificada não existe. Por favor, insira um caminho válido e tente novamente.')
    sys.exit()

# Percorre todas as imagens na pasta e as redimensiona, se necessário
for filename in os.scandir(pasta):
    if filename.is_file() and filename.stat().st_size > 1000000 and filename.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        caminho_imagem = filename.path
        novo_nome_arquivo = redimensionar_imagem(caminho_imagem, pasta)
        # Verifica se a imagem foi redimensionada com sucesso
        if novo_nome_arquivo is not None:
            # Renomeia o arquivo redimensionado para incluir o prefixo "redimensionada_"
            novo_caminho_imagem = os.path.join(pasta, f"redimensionada_{os.path.basename(filename)}")
            # Check if file with same name already exists
            if os.path.exists(novo_caminho_imagem):
                print(f'Warning: {novo_caminho_imagem} already exists and will be overwritten.')
            os.rename(novo_nome_arquivo, novo_caminho_imagem)
            print(f'{caminho_imagem} foi redimensionada e salva como {novo_caminho_imagem}.')
            # Exclui o arquivo original para economizar espaço
            os.remove(caminho_imagem)
        else:
            print(f'Error: {caminho_imagem} não pôde ser redimensionada ou já está abaixo do limite de tamanho.')
    elif filename.is_file() and filename.stat().st_size <= 1000000:
        print(f'{filename.path} já está abaixo do limite de tamanho.')
    elif filename.is_file() and not filename.name.lower().endswith(('.jpg', '.jpeg', '.png')):
        print(f'{filename.path} não é um arquivo de imagem válido.')

#teste