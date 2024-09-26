from llama_cpp import Llama

# llm = Llama.from_pretrained(
# 	repo_id="hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF",
# 	filename="llama-3.2-1b-instruct-q4_k_m.gguf",
# 	verbose=False  # Desativa os logs de desempenho
# )

llm = Llama.from_pretrained(
	repo_id="hugging-quants/Llama-3.2-3B-Instruct-Q8_0-GGUF",
	filename="llama-3.2-3b-instruct-q8_0.gguf",
    verbose=False  # Desativa os logs de desempenho
)

def conversa():
    historico = [
        {"role": "system", "content": "Você é um assistente útil e amigável. Responda de forma clara e concisa."}
    ]
    print("Bem-vindo ao sistema conversacional. Digite 'sair' para encerrar.")
    
    while True:
        entrada = input("Você: ")
        if entrada.lower() == 'sair':
            print("Encerrando a conversa. Até logo!")
            break
        
        historico.append({"role": "user", "content": entrada})
        
        stream = llm.create_chat_completion(messages=historico, stream=True)
        print("Assistente: ", end="", flush=True)
        resposta_assistente = ""
        for chunk in stream:
            if chunk['choices'][0]['delta'].get('content'):
                conteudo = chunk['choices'][0]['delta']['content']
                print(conteudo, end="", flush=True)
                resposta_assistente += conteudo
        print()  # Nova linha após a resposta completa
        
        historico.append({"role": "assistant", "content": resposta_assistente})

if __name__ == "__main__":
    conversa()