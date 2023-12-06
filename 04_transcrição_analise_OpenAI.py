import openai
from whispers.whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel()
    result = model.transcribe(audio_path)
    return result['text']

def analyse_transcription(transcription):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Você é uma IA altamente habilidosa treinada em compreensão e sumarização de linguagem. Gostaria que você lesse o texto a seguir e o resumisse em um parágrafo conciso. Mantenha os pontos mais importantes, fornecendo um resumo coeso e legível que ajude alguém a entender os principais pontos da discussão sem precisar ler o texto completo. Evite detalhes desnecessários ou pontos tangenciais. Após isso, com base no texto, identifique e liste os principais pontos discutidos. Essas devem ser as ideias, descobertas ou tópicos mais importantes que são cruciais para a essência da discussão. Seu objetivo é fornecer uma lista que permita a alguém entender rapidamente sobre o que foi falado. Em seguida, revise o texto e identifique as tarefas, atribuições ou ações acordadas ou mencionadas como necessárias. Essas podem ser tarefas atribuídas a indivíduos específicos ou ações gerais que o grupo decidiu tomar. Liste esses itens de ação de forma clara e concisa. Finalmente, como uma IA com expertise em análise de linguagem e emoção, sua tarefa é analisar o sentimento do seguinte texto. Considere o tom geral da discussão, a emoção transmitida pela linguagem utilizada e o contexto no qual palavras e frases são empregadas. Indique se o sentimento é geralmente positivo, negativo ou neutro, fornecendo breves explicações para sua análise, quando possível. O texto em questão é o seguinte::\n\n{transcription}",
        temperature=0.7,
        max_tokens=150,
    )
    return response.choices[0].text
