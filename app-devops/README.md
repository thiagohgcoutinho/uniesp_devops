# **Projeto Multicamadas com Docker: Gerenciador de Eventos**

## **Descrição**
Este é um projeto web multicamadas que utiliza Docker para gerenciar os serviços. Ele inclui:
- **Front-end**: Interface web construída com HTML, CSS e JavaScript.
- **Back-end**: API REST desenvolvida em Python (Flask).
- **Banco de Dados**: Banco relacional PostgreSQL.
- Funcionalidades completas de **CRUD** (Create, Read, Update, Delete) para gerenciar eventos.

---

## **Tecnologias Utilizadas**
- **Docker e Docker Compose**
- **Flask** (Back-end)
- **PostgreSQL** (Banco de Dados)
- **HTML, CSS, JavaScript** (Front-end)

---

## **Como Executar o Projeto**

### **Pré-requisitos**
1. **Docker** e **Docker Compose** instalados.
2. Certifique-se de que as portas **8080**, **3000** e **5432** estão livres.

### **Passos**
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_PROJETO>
   
2. Configure o arquivo `.env` com os seguintes valores:
   ```env
   DB_HOST=db
   DB_NAME=product_db
   DB_USER=postgres
   DB_PASSWORD=postgres

3. Construa e inicie os contêineres:
   ```bash
   docker compose up --build

4. Acesse os serviços:
   - **Front-end**: [http://localhost:8080](http://localhost:8080)
   - **Back-end**: [http://localhost:3000](http://localhost:3000)

5. Para encerrar os contêineres, execute:
   ```bash
   docker compose down

## **Como Utilizar**

### **Front-end**
1. Preencha o nome e o preço de um evento no formulário e clique em **"Salvar"**.
2. Utilize o campo de busca para filtrar eventos existentes.
3. Exclua eventos clicando no botão de lixeira na tabela de eventos.

### **API REST**
Você pode interagir com as seguintes rotas via ferramentas como Postman ou Curl:
- **GET** `/products`: Lista todos os eventos.
- **POST** `/products`: Adiciona um novo evento.
  - Exemplo de corpo da requisição:
    ```json
    {
      "name": "Show de Rock",
      "price": 150.00
    }
    ```
- **DELETE** `/products/:id`: Exclui um evento existente.

---

## **Funcionalidades**
- Adicionar eventos com nome e preço.
- Listar todos os eventos.
- Filtrar eventos por nome no frontend.
- Excluir eventos existentes.

---

## **Estrutura do Banco de Dados**
O projeto utiliza uma tabela chamada `products` para armazenar os dados dos eventos:
- **id**: Identificador único do evento (chave primária).
- **name**: Nome do evento.
- **price**: Preço do ingresso do evento.

---

## **Como Encerrar os Serviços**
Para parar os containers, execute:
bash
docker compose down

---

## **Possíveis Melhorias Futuras**
- Adicionar autenticação para gerenciar permissões de acesso.
- Integrar uma API externa para informações adicionais dos eventos (como localização ou previsão do tempo).
- Implementar edição de eventos no frontend.
- Adicionar suporte a categorias de eventos para facilitar a organização.
- Implementar notificações para alertar sobre eventos próximos.
