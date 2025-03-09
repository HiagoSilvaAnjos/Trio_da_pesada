# Sistema de Processamento de Linguagem Natural (PLN)

Este repositório documenta um sistema de **Processamento de Linguagem Natural (PLN)** que realiza a segmentação de textos em subtópicos com base em sentenças similares e palavras-chave.

## Estrutura do Sistema

O sistema é dividido em três fases principais:

### 1. Entrada
- O sistema recebe um **arquivo de texto** contendo o conteúdo original a ser processado.
- O texto será carregado e preparado para o processamento.

### 2. Processamento
O sistema segue as seguintes etapas para segmentação do texto:

#### a) Preparação do Texto
- **abrir_arquivo**: Carrega o arquivo de entrada.
- **processar_texto**: Limpa o texto removendo caracteres indesejados.
- **tokenizar_texto**: Separa o texto original em listas tokenizadas de palavras.
- **remover_stopwords_pontuacao**: Remove stopwords e pontuações.

#### b) Cálculo de Similaridade
- **pegar_representacao_vetorial**: Obtém a representação vetorial de cada sentença.
- **soma_quadradaProduto escalar**: Encontra o denominador necessário para a similaridade.
- **cosseno_similary**: Calcula a similaridade entre vetores.
- **Limite de Similaridade**: Um valor de 0.52 é usado para determinar se sentenças devem ser agrupadas.

#### c) Definição de Tópicos
- **pegar_topicos**: Para cada sentença, retorna suas palavras-chave como tópicos.
  - Se houver palavras com frequência maior que 1, elas são consideradas relevantes.
  - Caso contrário, substantivos, verbos, adjetivos e nomes próprios são usados.
  - Se nenhuma dessas opções for encontrada, a primeira palavra da sentença é usada como tópico.

#### d) Geração do Arquivo Final
- **criar_novo_arquivo**: Cria um novo arquivo organizando as sentenças em subtópicos e seus respectivos parágrafos.

### 3. Saída
- O resultado final é um **novo arquivo de texto** contendo o conteúdo segmentado em subtópicos.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para implementação.
- **SpaCy**: Biblioteca para processamento de linguagem natural.
- **Expressões regulares**: Para identificação de padrões textuais.

## Níveis de Implementação
O sistema pode ser implementado em diferentes níveis de dificuldade:

- **Nível 1**: Processamento básico do texto e separação em sentenças.
- **Nível 2**: Implementação da similaridade entre sentenças.
- **Nível 3**: Segmentação avançada utilizando tópicos relevantes.

## Como Utilizar
1. Forneça um arquivo de texto como entrada.
2. O sistema processará o arquivo e segmentará o conteúdo em subtópicos.
3. Um novo arquivo de texto será gerado com o conteúdo organizado.

## Melhorias Futuras
- Uso de **Machine Learning** para aprimorar a segmentação.
- Integração com uma **interface web**.
- Suporte a diferentes formatos de entrada (PDF, DOCX, etc.).

## Contribuição
Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, abra uma **issue** ou envie um **pull request**.

## Contribuidores Iniciais
- [pittpinheiro](https://github.com/pittpinheiro)
- [HiagoSilvaAnjos](https://github.com/HiagoSilvaAnjos)
- [AndreySlv](https://github.com/AndreySlv)

