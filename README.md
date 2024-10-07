# Sobre o Projeto

Este é o projeto de um pacote Python capaz de treinar um classificador Haar Cascade de imagens se baseando no artigo [Creating a Cascade of Haar-Like Classifiers: Step by Step](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf).

# Obtenção de Imagens

Sites como o [Kaggle](https://www.kaggle.com/) e [images.cv](https://images.cv/) podem ser usados para obter a base de dados das imagens. Note que pode ser interessante remover ou filtrar algumas imagens obtidas destes sites por não serem ideais para certas aplicações de ML.

# Configuração de Parâmetros

É possível configurar os parâmetros de pré-processamento e treino pelo arquivo `params.py`. Segue abaixo um exemplo desse arquivo.

```python
img_size = 256
obj_size = 32
num_stages = 15

scaleFactor = 1.1
minNeighbors = 3
```

* `img_size`: Valor para o qual as imagens serão redimensionadas
* `obj_size`: Medida dos objetos
* `num_stages`: Quantidade de estágios de treinamento
* `scale_factor`: O quanto do tamanho da imagem é reduzido. Ver mais [aqui](https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html)
* `minNeighbors`: Quantos vizinhos cada retângulo canditato deve ter para ser mantido. Ver mais [aqui](https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html)

# Executando o Código

## Instalando Depedências

`poetry install`

## Realizando Pré-processamento

`poetry run preprocess`

Este comando irá gerar a pasta `tmp` contendo as imagens pré-processadas. Este comando também irá colar o executável `objectmaker.exe` em `tmp/positive`.

## Marcando Imagens Positivas

Execute o arquivo `tmp/positive/objectmaker.exe` para marcar as imagens positivas. Use o mouse para fazer o retângulo, a tecla `space` para adicionar o retângulo (mais de um retângulo pode ser marcado na mesma imagem) e a tecla `Enter` para passar para a próxima imagem. No fim, será gerado o arquivo `tmp/positive/info.txt`.

## Realizando Treinamento

`poetry run train`

## Gerando Arquivo XML

`poetry run generate_xml`

O arquivo XML será exportado para `result.xml`.

## Testando Classificador

`poetry run test`

Este comando irá testar o classificador exportado para `result.xml` no passo anterior nas imagens contidas na pasta `test_imgs`.
