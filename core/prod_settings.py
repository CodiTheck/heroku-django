import dj_database_url
from core.settings import *
from stdlib import get_env_var


DEBUG = False;
TEMPLATE_DEBUG = False;

# To force HTTPs communication to server
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https');
SECURE_SSL_REDIRECT     = True;

# You can go to https://djecrety.ir/
# to generate a new key
# SECRET_KEY = get_env_var("SECRET_KEY", "");

DATABASES['default'].update(dj_database_url.config());

ALLOWED_HOSTS = ['heroku-dj.herokuapp.com'];

# CONFIGURATION DE WHITENOISE
# ================================================================
# WhiteNoise permet à votre application Web de servir ses
# propres fichiers statiques, ce qui en fait une unité autonome
# qui peut être déployée n'importe où sans dépendre de nginx,
# d'Amazon S3 ou de tout autre service externe. (Particulièrement
# utile sur Heroku, OpenShift et autres fournisseurs PaaS.).
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware'];
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage';
