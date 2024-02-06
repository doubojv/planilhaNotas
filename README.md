# planilhaNotas

## Desafio Tunts-Rocks

A princípio, o desafio trata-se de um preenchimento de colunas de uma classe escolar com a seguinte planilha no excel:




Preferi usar Python pela facilidade que tive no entendimento da documentação do Google Sheets.

O print abaixo representa a planilha após o preenchimento:

Minha planilha atualizada:
https://docs.google.com/spreadsheets/d/1aBNO50SgbE35h7OgvyH0x7NqepqwdsRSK2PGl9z5fZc/edit#gid=0


## Tecnologias utilizadas

**Linguagem:** Python

**Outros:** Google Sheets 



## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar algumas bibliotecas na sua máquina

`pip install gspread pandas
`

`pip install openpyxl
`



## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/doubojv/planilhaNotas.git
```

Entre no diretório do projeto

```bash
  cd planilhaNotas
```

Instale as dependências citadas anteriormente


Faça uma cópia pública e editável da seguinte planilha:
```bash
  https://docs.google.com/spreadsheets/d/1XvWJcRLj2WAeXO3ULQ_GxGm9---3SZkjMbGcXMJtt70/edit#gid=0
```

Substitua a linha 16 pelo ID da sua nova planilha

```bash
spreadsheet = client.open_by_key("SEU_ID")
```
