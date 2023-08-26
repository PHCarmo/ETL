# Projeto ETL

**ETL** - Pipeline de Extração, Transformação e Carregamento de dados.

## Descrição

O projeto **ETL** é um exemplo de um processo de Extração, Transformação e Carregamento implementado usando Python. Desenvolvido a partir do Bootcamp Santader 2023 lecionado na DIO.

## Funcionalidades

- Extract: baseado em um CSV de IPs públicos busca informações atuais sobre o clima na região do IP fornecido. (API usada: https://weatherstack.com/documentation)

- Transform: realiza buscas personalizadas através do Google sobre o que fazer na localidade do IP baseando no clima apresentado no dia (API usada: https://developers.google.com/custom-search/v1/overview?hl=pt-br)

- Load: Devolve as principais informações para um CSV final.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/PHCarmo/ETL.git
    cd ETL
    ```

2. Instale as bibliotecas necessárias:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o processo ETL:

    ```bash
    python main.py
    ```

4. Procure o arquivo "final_result.csv" dentro do subdiretório "data".

Este projeto foi criado por PHCarmo em @2023.
