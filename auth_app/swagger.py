from drf_yasg import openapi

login_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
    },
    required=['email', 'password']
)
