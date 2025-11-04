# Autenticação com JWT

- Token gerado a partir das credencias do usuário logado

- Quando o usuário loga a API envia o token pelo payload para frontend

- Quando o usuário se cadastra o token é gerado e enviado para o frontend

- O token expira com o tempo

## Configuração

- Baixar biblioteca: ```pip install djangorestframework_simplejwt```

- Settings.py: 
```
INSTALLED_APPS = [
    "rest_framework",
    "rest_framework.authtoken"
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

## Imports

- ```from rest_framework.decorators import action, authentication_classes, permission_classes```
- ```from rest_framework.authentication import TokenAuthentication, SessionAuthentication```
- ```from rest_framework.permissions import IsAuthenticated```
- ```from rest_framework.authtoken.models import Token```

- Observação: o authtoken precisa ser adicionado aos installed apps e migrado

## Token

- ```token = Token.objects.create(user=user)`` Criar o token no signup

- ```token, created = Token.objects.get_or_create(user=user)``` Pegar ou criar (em caso de expirar) o token no login

- ```authentication_classes = [TokenAuthentication]```-> Define que o token deve ser passado no header(Authorization: Token <token>)
    
- ```permission_classes = [IsAuthenticated]``` -> Define que é necessário estar autenticado para função ser chamada

## Insights

- Não utilizar o **get_objects_or_404**, pois não retorna None e sim um exception 404, logo, para validações de username ou email já existentes o ideal é utilizar ```User.objects.filter(username=username).exists()```

- ```User.objects.filter(username=username).first()``` retorna o objeto com o arg de comparação, para validar senha, por exemplo, porque assim retorna None ao invés de 404

- Ao devolver os dados do usuário, não fazer serializer.data, pois só está retornando os próprios dados de envio no processo de signup e não o objeto criado. O correto é pegar o objeto e serializar ```UserSerializer(user).data```

- Utilizar serializers diferentes para o signup e login, pois o signup usa model serializer que valida constraints únicas ao automaticamente(como o username, mesmo que o intuito seja apenas validar, não criar, o que gera um erro de user duplicado), então o ideal é não utilizar model serializer no serializer de login e sim um serializer simples