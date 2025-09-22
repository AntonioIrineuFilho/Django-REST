# Conceitos Teóricos

## API

- Aplication Programming Interface tem função de intermediar a comunicação entre o frontend e o banco de dados 

- Utiliza o protocolo HTTP (XML/JSON) com requisição via URL

- URL: endereço estático

- URI / Endpoint: partiçção dinâmica da URL

## REST

- Representational State Transfer

- Arquitetura para desenvolvimento de serviços web

- Se um sistema segue corretamente a estrutura REST ele é considerado um serviço **RESTful**

- Utiliza mémoria em cache para armazenar temporariamente a resposta de uma requisição, dispensando acessar o servidor kkexcessivamente

### Verbos HTTP REST

- PUT: Create

- GET: Read

- POST: Update

- DELETE: Delete

## HTTP Request

- Requisição HTTP do dispositivo cliente ao servidor web

### Header da requisição

- Accept: Especifíca o formato de arquivo desejado
    - Accept: appliction/xml
    - Accept: application/json
    - Accept: application/pdf

- Accept-Language: Idioma do conteúdo

- Cache-Control: Controle de conteúdo cache (dados e tempo)

## HTTP Response

- Resposta do servidor à requisição

- Deve seguir o accept da requisição (se foi requisitado um JSON deve ser respondido um JSON)

- Deve ser retornado um status code

### Status Code

- 2XX: Sucess
    - 200: Consulta encontrada no server
    - 201/202: Criação de novo recurso com sucesso

- 3XX: Redirection
    - 300: Requisição HTTP foi entendida, mas o recurso encontra-se em outro endpoint

- 4XX: Cliente Error
    - 404: endpoint não encontrado
    - 403 e 405: Endpoint só pode ser requisitada com GET/POST

- 5XX: Server Error
    - 500: Requisição bem sucedida, mas com erro no lado do servidor

