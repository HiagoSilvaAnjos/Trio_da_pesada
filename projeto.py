#INSTALE AS DEPENDENCIAS 
# pip install spacy
# python -m spacy download pt_core_news_lg

import spacy
nlp = spacy.load("pt_core_news_lg")

caminho_relativo_entrada = "/workspaces/Trio_da_pesada/texto_entrada.txt"
caminho_relativo_saida = "/workspaces/Trio_da_pesada/texto_saida.txt"

#HELPER FUNCTIONS
def remover_stopwords_pontuacao(sentenca_tokenizada):  
       return [token.text for token in nlp(sentenca_tokenizada) if not token.is_punct and not token.is_stop]

#MAIN FUNCTIONS
def abrir_arquivo(caminho_relativo):
    try:
        with open(caminho_relativo, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    
def processar_texto(texto):
    doc = nlp(texto)
    sentencas_tokenizadas = [sent.text.strip() for sent in doc.sents]

    sentencas_limpas = []
    for sentenca in sentencas_tokenizadas:
        sentenca_limpa = remover_stopwords_pontuacao(sentenca)
        sentencas_limpas.append(sentenca_limpa)

    return (sentencas_limpas,sentencas_tokenizadas)

def pegar_topicos(texto):
    tokens_do_texto = remover_stopwords_pontuacao(texto)

    chaves = Counter(tokens_do_texto)

    chaves_frequentes =  []
    for chave in chaves:
        if chaves[chave] > 1:
            chaves_frequentes.append(chave)
    
    if chaves_frequentes:
        topicos = f"<Tópicos: {', '.join(chaves_frequentes)}>"
        return (texto, topicos)

    else:
        palavras_relevantes = []

        for token in nlp(" ".join(tokens_do_texto)):
            if token.pos_ in ["VERB","ADJ","PROPN","NOUN"]:
                palavras_relevantes.append(token.text)
        
        if palavras_relevantes and len(palavras_relevantes) > 1:
            topicos = []
            topicos.append(str(palavras_relevantes[0]))
            topicos.append(str(palavras_relevantes[1]))
            topicos_gerados = f"<Tópicos: {', '.join(topicos)}>"

            return (texto,topicos_gerados)
        else:
            topico = texto[0]
            topicos_restantes = f"<Tópicos: {', '.join(topico)}>"

            return (texto, topicos_restantes)
        
def criar_aquivos(lista_sentencas):
    with open(caminho_relativo_saida, "w", encoding="utf-8") as paragrafos:
        for paragrafo in lista_sentencas:
            paragrafos.write(f"{paragrafo[0]} \n")
            paragrafos.write(f"{paragrafo[1]} \n")
            paragrafos.write(f"\n")


def start(): 
    try:
        # Nível 1
        texto = abrir_arquivo(caminho_relativo_entrada)
        texto_processado = processar_texto(texto) # Vai retornar uma tupla com dois valores => (sentenças_tokenizadas, sentenças_originais)
        print(texto_processado[0])
        print(texto_processado[1])

        # Nível 2

        #Nível 3
        sentencas_completas = []
        # Essas sentenças concatenadas vão se tornar o texto dado pelo nível dois, só está esse exemplo pra fazer o código funcionar, depois eu altero.
        sentencas_concatenadas = ['Python é uma linguagem de programação popular para ciência de dados.', 'Muitas pessoas utilizam Python para análise de dados e machine learning. Ciência de dados e machine learning são áreas que se beneficiam das bibliotecas do Python.', 'Com suas bibliotecas poderosas, Python tornou-se essencial para inteligência artificial.', 'JavaScript é essencial para desenvolvimento web moderno. No desenvolvimento web, JavaScript permite criar interfaces dinâmicas. Frameworks baseados em JavaScript, como React e Next.js, facilitam o desenvolvimento web.', 'JavaScript e React são amplamente usados para aplicações interativas.']
        for senteca in sentencas_concatenadas:
            texto_topico = pegar_topicos(senteca)
            sentencas_completas.append(texto_topico)

        criar_aquivos(sentencas_completas)
        print("Arquivo de texto processado com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")

start()