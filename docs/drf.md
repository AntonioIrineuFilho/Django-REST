# Django REST Framework

- Atua dentro do Django tradicional

## Dependências

- Django -> ```pip install Django```

- Django REST Framework -> ```pip install djangorestframework markdown```

## Configuração

- No settings.py, adicionar "rest_framework" no INSTALLED_APPS

- No gerenciador de rotas globais, adicionar um include para o DRF

```Python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1", include("main_app.urls")),
    path("auth/", include("rest_framework.urls"))
]
```

## Model Serializers

- Arquivo serializers.py que será responsável por receber JSON, validar e converter em objeto (desserialização) ou o oposto, converter um objeto em JSON como response

- Importe o módulo de serializers -> ```from rest_framework import serializers```

- Cada classe de serializers herda serializers.ModelSerializers

### extra_kwargs

- Argumentos extras importantes principalmente para finalidades de segurança

- Argumentos do tipo "write_only" -> Permite apenas métodos de escrita como POST ou PUT para dados sensíveis como senhas, ou seja, apenas podem ser consumidos pela API mas não enviados como resposta ao frontend (basicamente ao mandar pro front ignora o que for write only)

- Argumentos do tipo "read_only" -> Apenas método GET, ou seja, não podem ser alterados via requisição, apenas entregues para visualização, como por exemplo uma chave estrangeira (basicamente ao modificar no back ignora o que for read only)

### Fields

- Os campos a serem mapeados pelo serializer são identificados por meio do atributo name no frontend, semelhante ao Django tradicional 

### Métodos nativos

- O Model Serializer possui diversos métodos nativos

- ```is_valid()``` -> Valida os dados recebidos da requisição

-  ```validated_data``` -> Retorna os dados validados em dict

- ```create() / update()`` -> Cria(POST) ou atualiza(PUT) objetos seguindo um fluxo padrão(podem ser reescritos no serializer se necessário)

### Serializer x Service

- Uma classe serializer e uma classe de serviço devem compartilhar responsabilidades

- Por exemplo, quando não há regras de negócio complexas os métodos podem ficar no serializer

- No entanto, quando houver o tratamento de regras de negócio mais complexas, o serializer ficaria responsável apenas pela validação dos dados, enquanto o service lidaria com a regra de negócio e a manipulação do banco de dados

## APIViews

- As views, semelhantes às views do Django tradicional, atuarão como APIViews, herdando do DRF

```Python
from rest_framework.views import APIView // para construção das APIs
from rest_framework.response import Response // para retorno dos JSONs ao frontend
from rest_framework import status // para retorno dos status code
// importação dos serializers
```

- Cada classe de APIViews devem herdar de APIView

## Generic views

- Conceito importante: para o CRUD, é importante entender o conceito de endpoints de coleção (endpoints gerais como quando algo é escrito ou lido) e endpoints individuais (específicas para instâncias, como por exemplo endpoints com o id de um objeto, para atualizar ou deletar)

- Há generic views para ambos os tipos de endpoints



