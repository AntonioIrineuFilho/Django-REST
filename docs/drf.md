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

### Serializer x Service

- Uma classe serializer e uma classe de serviço devem compartilhar responsabilidades

- Por exemplo, quando não há regras de negócio complexas os métodos podem ficar no serializer

- No entanto, quando houver o tratamento de regras de negócio mais complexas, o serializer ficaria responsável apenas pela validação dos dados, enquanto o service lidaria com a regra de negócio e a manipulação do banco de dados

### Serializer simples

- ```serializers.Serializer```

- Apenas serialização, sem as validações do ModelSerializer

- Os campos são instanciados como nos models

```Python
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField
    password = serializers.CharField(write_only=True)
```

### Métodos nativos

- O Model Serializer possui diversos métodos nativos

- ```is_valid()``` -> Valida os dados recebidos da requisição

-  ```validated_data``` -> Retorna os dados validados em dict

- ```create() / update()`` -> Cria(POST) ou atualiza(PUT) objetos seguindo um fluxo padrão(podem ser reescritos no serializer se necessário)

- ```metodo = serializers.SerializerMethodField()```-> Cria a expectativa da existência de um método com o padrão *get_<variavel>*, nesse caso, um método chamado get_metodo(), sendo que a variável será um campo do fields e possuirá um valor que pode ser manipulado com a chamada de obj no método: ```def get_metodo(self, obj)```

- ```model_id = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all(), source="model")``` -> Pega um campo do fields que seja um ID para uma FK, recupera o objeto(ou objetos, em caso de many=True) e valida retornando uma mensagem de erro se o ID foi inválido

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

## Viewsets

- Classes que abstraem e unificam os métodos de requisição, de modo que em um único viewset há os métodos para GET, POST, PUT, DELETE, RETRIEVE, etc.

- O roteamento das viewsets são feitas também de forma abstraída e automática por meio de routers

- No final, um viewset funciona como um apiview, só que com todos os métodos unificados por meio de ações(list, retrieve, create, update, partial_update, destroy) e com o roteamento sendo feito de forma abstraida e automática pelo router

```Python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_or_404
from .models import Modelo
from .serializers import ModeloSerializer

class ModeloViewSet(viewsets.ViewSet):

    def list(self, request):
        query_set = Modelo.objects.all()
        serializer = ModeloSerializer(queryset, many=true)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        modelo_objeto = get_or_404(Modelo, pk=pk)
        serializer = ModeloSerializer(modelo_objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        modelo_objeto = get_or_404(Modelo, pk=pk)
        serializer = ModeloSerializer(instance=modelo_objeto, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Model Viewsets

- Realiza tudo que o viewset faz mas de forma automática, apenas definindo o query set e o serializer

- Ou seja, todas as ações das requisições HTTP o model viewset realiza sozinho

```Python
from rest_framework import viewsets
from .models import Modelo
from .serializers import ModeloSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    query_set = Modelo.objects.all()
    serializer_class = ModeloSerializer
```

### Routers

- Gerador de endpoints automático do DRF, define as rotas por meio de uma palavra-chave definida e por meio de uma lógica de endpoints

- Se a requisição for para um objeto individual, gera um endpoint individual (/palavra-chave/pk)

- Se for uma requisição que não dependa de um objeto específico (create/list), ele gera um endpoint coleção (/palvra-chave/)

```Python
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"endpoint-coleção", MinhaViewSet, basename="endpoint-coleção")
urlpatterns = router.urls
```

### Actions

- Decoradores para métodos personalizados dentro do ModelViewSet

- ```@action(detail=Bool, methods=['METHOD'])```

- o detail recebe um booleano para indicar se deve passar o PK no endpoint e o methods indica com quais métodos HTTP esse método pode ser invocado

- o action gera um endpoint personalizado para o endpoint principal da classe ao qual esse método pertence:

```Python
class Produtos(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

    @action(detail=True, methods=["GET"])
    def ver_produto(self, request):
    ...

# endpoint final = produtos/pk/ver_produto
```

