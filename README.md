# 2026 - ILP - Atividade avaliativa no. 02 do 1o bimestre

## Informações gerais
- **Objetivo**: avaliar conhecimento dos alunos até notas de aula [for](https://github.com/infoweb-logica/11-notas_de_aula-09-python/).
- **Público alvo**: alunos da disciplina de [Introdução a lógica e programação](https://github.com/infoweb-logica/) do curso de [Infoweb](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN](https://portal.ifrn.edu.br/campus/natalcentral/).
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Aluno(a)(e)**: Analy Souza de Lima 

---

## Checklist

- [ ] 1. Fork desse repositório
- [ ] 2. Substitui neste arquivo (`README.md`) de `FIXME` pelo seu nome
- [ ] 3. Abrir o VS Code local ou o _codespaces_ para criar os arquivos respostas da avaliação. Preferível o _codespaces_.
- [ ] 4. Responder as questões abaixos.
- [ ] 5. Publicar no Github suas repostas.

> 💡 **Dica 01:** Preste atenção nos nomes dos arquivos especificados no texto das questões.

> 💡 **Dica 02:** Lembre de publicar suas respostas no Github de votla, se não eu não consigo acessar suas respostas.

> 💡 **Dica 03:** Dúvidas, pergunte!!! Estamos todos aprendendo.

> 💡 **Dica 04:** Use a função abaixo para gerar números aleatórios. Importante ter a instrução `import random`.
[Informações sobre números aleatórios](/numeros_aleatorios.md).

```python
import random

# Inteiro entre 1 e 100
numero_aleatorio = random.randint(1, 100)
```
---

## Lista de questões

### Questão 1 (nível fácil)
Escreva um programa Python que exiba na tela uma sequência de 10 números inteiros aleatórios entre 1 e 100.

Exemplo de saída:
```
1o número aleatório 4
2o número aleatório 10
3o número aleatório 1
4o número aleatório 20
5o número aleatório 34
6o número aleatório 70
7o número aleatório 53
8o número aleatório 2
9o número aleatório 100
10o número aleatório 99

```


**Arquivo resposta**: `questao01.py`

---

### Questão 2 (nível fácil)

Escreva um programa Python que leia um número inteiro positivo e armazene na variável `repeticoes`; e exiba na tela uma sequência de `repeticoes` números inteiros aleatórios entre 1 e 100.

Exemplo de entrada:
```
Digite a quantidade de números aleatórios: 10
```

Exemplo de saída:
```
1o número aleatório 4
2o número aleatório 10
3o número aleatório 1
4o número aleatório 20
5o número aleatório 34
6o número aleatório 70
7o número aleatório 53
8o número aleatório 2
9o número aleatório 100
10o número aleatório 99

```

**Arquivo resposta**: `questao02.py`

---

### Questão 3 (nível médio)

Escreva um programa que recebe um inteiro positivo `numero` e determina se `numero` é um número perfeito (um número é perfeito se a soma de seus divisores próprios é igual a ele mesmo, ex: 6 = 1+2+3).

| Exemplo de entrada | Saída esperada |
| ------------------ | -------------- |
| 6 | 6 é perfeito |
| 28 | 28 é perfeito |
| 10 | 10 não é perfeito |

**Arquivo resposta**: `questao03.py`

---

### Questão 4 (nível médio)

Escreva um programa que leia um inteiro positivo `numero` e exibe o número de dígitos de `numero`.

| Exemplo de entrada | Saída esperada |
| ------------------ | -------------- |
| 1234 | 4 |
| 50 | 2 |

**Arquivo resposta**: `questao04.py`

---

### Questão 5 (nível difícil)

Escreva um programa que leia um número inteiro positivo `repeticoes`, depois leia `repeticoes` números inteiros e calcule:
- a soma total,
- a média,
- o maior valor,
- o menor valor,
- a quantidade de valores acima da média.

Exemplo de entrada:
```
Digite a quantidade de números: 3
Informe o valor 1: 5
Informe o valor 2: 1
Informe o valor 3: 3
```

Exemplo de saída:
```
a soma total é 9
a média é 3
o maior valor é 5
o menor valor é 1
a quantidade de valores acima da média é 1
```

**Arquivo resposta**: `questao05.py`

