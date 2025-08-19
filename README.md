# Validador de CPF em Python

Este projeto é um script em **Python** que valida **CPFs (Cadastro de Pessoas Físicas)** de acordo com as regras oficiais da Receita Federal.  
O programa realiza verificações passo a passo, garantindo maior confiabilidade na checagem de CPFs digitados pelo usuário.

---

## Funcionalidades

- Verifica se o CPF contém **apenas números**  
- Confere se o CPF possui **exatamente 11 dígitos**  
- Impede CPFs compostos por **todos os dígitos iguais** (ex: `11111111111`)  
- Calcula e valida os **dígitos verificadores** (10º e 11º dígitos)  
- Exibe mensagens claras de erro e sucesso  
- Permite múltiplas tentativas até o usuário digitar `sair`  

---

## Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.  
2. Clone este repositório ou baixe os arquivos manualmente.  
3. No terminal, execute:

```bash
python cpf_validator.py
```

---

## Exemplo de Uso

```bash
$ python cpf_validator.py

Informe o seu CPF (ou digite 'sair' para finalizar): 12345678909

CPF INVÁLIDO! ❌
```

```bash
$ python cpf_validator.py

Informe o seu CPF (ou digite 'sair' para finalizar): 52998224725

CPF VÁLIDO! ✅
```

---

## Tecnologias Utilizadas

- **Python 3** - Linguagem de programação

- **Sys** - Manipulação de saída e finalização do programa

---

## Lógica do Programa

O script é dividido em funções independentes, facilitando manutenção e leitura do código:

- `validar_cpf(cpf)` - Verifica se o CPF contém apenas números.

- `tamanho_cpf(cpf)` - Confere se possui exatamente 11 dígitos.

- `sequencia(cpf)` - Bloqueia CPFs com todos os números iguais.

- `digito_dez(cpf)` - Calcula o 10º dígito verificador.

- `digito_onze(cpf)` - Calcula o 11º dígito verificador.

---

## Contribuição

Contribuições são bem-vindas! 
Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar o projeto.

---

## Licença

Este programa está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Autor

**Kauã Santos**
Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**

**Contato:**

- GitHub: [kauasantos-dev](https://github.com/kauasantos-dev)
- E-mail: [kavillykaua@gmail.com](kavillykaua@gmail.com)