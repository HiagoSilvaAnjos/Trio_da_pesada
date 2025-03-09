# Sistema de Processamento de Linguagem Natural (PLN)

Este repositório documenta um sistema de **Processamento de Linguagem Natural (PLN)** que executa a segmentação de textos em subtópicos com base em sentenças similares e suas palavras-chave.

## Estrutura do Sistema

O sistema está organizado em três principais fases:

### 1. Entrada
- O sistema recebe um **arquivo de texto** contendo o conteúdo original a ser processado.

### 2. Processamento
- O texto é quebrado em **subtópicos** a partir de sentenças similares e suas palavras-chave.
- O processamento pode utilizar bibliotecas de PLN, como **SpaCy**, para análise e segmentação do texto.
- A lógica de segmentação é organizada por meio de **funções** para modularização e melhor manutenção do código.

### 3. Saída
- Como resultado, um **novo arquivo de texto** é gerado com o texto original segmentado em subtópicos.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para implementação do sistema.
- **SpaCy**: Biblioteca para processamento de linguagem natural.
- **Expressões regulares**: Para identificação de padrões textuais.

## Como Utilizar
1. Forneça um arquivo de texto como entrada.
2. O sistema irá processar o arquivo e segmentá-lo em subtópicos.
3. Um novo arquivo de texto será gerado com o conteúdo segmentado.

## Possíveis Melhorias
- Integração com modelos de **Machine Learning** para melhorar a identificação de subtópicos.
- Implementação de uma interface web para facilitar o uso do sistema.
- Suporte a diferentes formatos de entrada (PDF, DOCX, etc.).
