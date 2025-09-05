DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'portaldb',
        'CLIENT': {
            'host': 'mongodb',
            'port': 27017,
        }
    }
}
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'corsheaders',
    'your_app',
]
MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    # ...
]
CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}