<h2>README do Script de Redimensionamento de Imagens</h2>

>Status do Projeto: Em desenvolvimento

<p>Este script permite redimensionar todas as imagens em uma pasta especificada para uma largura máxima de 1000 pixels,
    mantendo a proporção. Se uma imagem for maior que 1 MB, ela será redimensionada e salva com o prefixo
    "redimensionada_" na mesma pasta. A imagem original será excluída para economizar espaço.</p>

<h3>Pré-requisitos</h3>

<ul>
    <li>Python 3.5 ou posterior</li>
    <li>Módulo PIL (Python Imaging Library)</li>
</ul>

<h3>Instalação</h3>

<ol>
    <li>Instale o Python 3.5 ou posterior no site oficial: https://www.python.org/downloads/</li>
    <li>Instale o módulo PIL executando o comando pip install pillow no terminal.</li>
</ol>

<h3>Uso</h3>
<ol>
    <li>Salve o script em uma localização desejada.</li>
    <li>Abra uma janela de terminal e navegue até a pasta contendo o script.</li>
    <li>Execute o script digitando o comando python image_resizing_script.py no terminal.</li>
    <li>Informe o caminho para a pasta contendo as imagens que você deseja redimensionar quando solicitado.</li>
    <li>O script redimensionará todas as imagens elegíveis na pasta e as salvará com o prefixo "redimensionada_"
        na mesma pasta.</li>
    <li>As imagens originais serão excluídas.</li>
</ol>

<h3>Observações</h3>

<ul>
    <li>O script apenas redimensiona imagens com as extensões ".jpg", ".jpeg" ou ".png".</li>
    <li>Se uma imagem já for menor ou igual a 1 MB, ela não será redimensionada.</li>
    <li>Se um arquivo com o mesmo nome da imagem redimensionada já existir, ele será sobrescrito.</li>
    <li>Se o módulo PIL não estiver instalado, o script será encerrado e solicitará a instalação.</li>
</ul>
