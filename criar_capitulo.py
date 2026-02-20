import os
import sys

TEMPLATE_CAPITULO = r"""\chapter{{{titulo}}}

% ====================================================
% SEÇÃO 1.1
% ====================================================
\section{{Seção Exemplo}}

\begin{{resumocapitulo}}
Resumo introdutório desta seção.
\end{{resumocapitulo}}

% --- EXERCÍCIOS ---
\registrasolucao{{1.1}}{{1a}}{{%
\begin{{passo}}{{1: Descrição do passo}}
Escreva aqui a resolução detalhada.
\end{{passo}}
}}
"""

def formatar_nome_arquivo(titulo):
    nome = titulo.lower().replace(" ", "_")
    # remover acentos comuns
    for acento, sem_acento in zip("çãáéíóúâêô", "caaeiouaeeo"):
        nome = nome.replace(acento, sem_acento)
    return f"{nome}.tex"

def criar_capitulo(titulo):
    pasta = "capitulos"
    os.makedirs(pasta, exist_ok=True)
    arquivo = os.path.join(pasta, formatar_nome_arquivo(titulo))
    
    if os.path.exists(arquivo):
        print(f"⚠️  O capítulo '{titulo}' já existe!")
        return
    
    conteudo = TEMPLATE_CAPITULO.format(titulo=titulo)
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)
    
    print(f"✅ Capítulo '{titulo}' criado com sucesso em: {arquivo}")
    print(f"📌 Lembre-se de adicionar no main.tex com \\input{{capitulos/{formatar_nome_arquivo(titulo).replace('.tex','')}}}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python criar_capitulo.py 'Título do Capítulo'")
    else:
        criar_capitulo(sys.argv[1])