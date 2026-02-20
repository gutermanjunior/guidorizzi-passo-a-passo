# 📚 Guia de Sobrevivência: Guidorizzi Passo a Passo

![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> Um material didático em LaTeX com resoluções detalhadas dos exercícios de **Um Curso de Cálculo**, de Hamilton Luiz Guidorizzi.

---

## 📖 Sobre o Projeto

Este repositório contém o código-fonte em LaTeX de um material complementar voltado à resolução **minuciosa e estruturada** dos exercícios do livro *Um Curso de Cálculo*.

O objetivo é apoiar estudantes na transição da matemática elementar para o Cálculo I, reduzindo lacunas conceituais e fortalecendo o rigor matemático.

Este guia prioriza:

- Clareza lógica
- Desenvolvimento passo a passo
- Justificativa formal de cada procedimento
- Identificação explícita de erros comuns

---

## 🚀 Diferenciais do Guia

- 🔎 **Passo a Passo Matemático**  
  Nenhuma etapa é omitida. Cada manipulação algébrica é explicitamente justificada.

- ⚠️ **Alertas de Atenção**  
  Destaques visuais para armadilhas frequentes (ex: multiplicação cruzada em inequações).

- 🧩 **Estrutura Modular**  
  Organização por capítulos e apêndices para facilitar consulta e expansão futura.

- 📚 **Foco Didático**  
  Linguagem acessível sem comprometer o rigor matemático.

---

## 📂 Estrutura do Projeto
```text
.
├── main.tex
├── configuracoes.tex
├── lista.tex
└── capitulos/
    ├── numeros_reais.tex
    ├── funcoes.tex
    └── limites.tex
```


### Arquivos principais:

- `main.tex` → Arquivo mestre que compila todo o material.
- `configuracoes.tex` → Configurações visuais e comandos personalizados.
- `lista.tex` → Lista organizada de exercícios com hyperlinks.
- `capitulos/` → Arquivos `.tex` individuais por tema.

---

## 🛠️ Como Compilar Localmente

### 1️⃣ Pré-requisitos

Instale uma distribuição LaTeX:

- TeX Live  
- MiKTeX  
- MacTeX  

### 2️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/sobrevivendo-ao-guidorizzi.git
cd sobrevivendo-ao-guidorizzi
```

### 3️⃣ Compile o projeto

Método recomendado:

```bash
latexmk -pdf main.tex
```

Ou manualmente:

```bash
pdflatex main.tex
```

---

---

## 🎯 Público-Alvo

Este material é especialmente indicado para:

- Estudantes de Engenharia
- Licenciaturas em Matemática
- Bacharelado em Matemática
- Estudantes de áreas exatas cursando Cálculo I
- Autodidatas interessados em fortalecer a base em Cálculo Diferencial

---

## 🤝 Contribuições

Contribuições são bem-vindas.

Se você encontrou:

- Erros matemáticos
- Melhorias de explicação
- Sugestões de organização
- Problemas de compilação

Sinta-se à vontade para:

1. Abrir uma **Issue**
2. Enviar um **Pull Request**

Toda colaboração contribui para tornar o aprendizado de Cálculo mais acessível.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.

Você pode utilizar, modificar e distribuir o material, respeitando os termos da licença.

---

## ⭐ Apoie o Projeto

Se este material ajudou você, considere:

- ⭐ Marcar o repositório com uma estrela
- 📢 Compartilhar com colegas
- 🤝 Contribuir com melhorias
- 🧠 Sugerir novos exercícios para resolução

Construindo conhecimento matemático, passo a passo.















<!--# 📚 Guia de Sobrevivência: Guidorizzi Passo a Passo

![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

[cite_start]Este repositório contém o código-fonte em LaTeX de um material didático focado na resolução detalhada dos exercícios do livro **"Um Curso de Cálculo" (Guidorizzi)**[cite: 66]. O objetivo é ajudar estudantes que enfrentam dificuldades com a transição da matemática básica para o Cálculo 1.

---

## 🚀 Por que este guia?

Aprender Cálculo pode ser assustador. Este material foi desenhado para ser um mapa de sobrevivência, focando em:
* [cite_start]**Passo a Passo Matemático:** Nenhuma etapa é "mágica" ou pulada[cite: 46, 57].
* [cite_start]**Alertas de Atenção:** Caixas visuais que destacam erros comuns (como multiplicar cruzado em inequações)[cite: 46].
* [cite_start]**Organização Modular:** Dividido por capítulos e apêndices para facilitar a consulta[cite: 44, 70].

---

## 📂 Estrutura do Projeto

O projeto está organizado de forma modular para facilitar a manutenção:
* [cite_start]`main.tex`: Arquivo mestre que une todos os módulos[cite: 29].
* [cite_start]`configuracoes.tex`: Toda a identidade visual e comandos personalizados.
* [cite_start]`lista.tex`: Compilado de exercícios sugeridos com hyperlinks[cite: 1].
* [cite_start]`capitulos/`: Pasta contendo os arquivos `.tex` de cada seção (ex: Números Reais, Funções)[cite: 30].

---

## 🛠️ Como Compilar Localmente

Se você deseja gerar o PDF no seu computador:

1. Tenha uma distribuição LaTeX instalada (TeX Live, MiKTeX ou MacTeX).
2. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/sobrevivendo-ao-guidorizzi.git](https://github.com/seu-usuario/sobrevivendo-ao-guidorizzi.git)
   ```
3. Compile o arquivo main.tex usando o compilador pdflatex ou latexmk.

---

📝 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar e estudar!

---

🤝 Contribuições
Encontrou um erro em alguma conta? Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request com a correção. Toda ajuda é bem-vinda para salvar mais um estudante do Cálculo! 🆘-->