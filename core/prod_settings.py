import dj_database_url
from core.settings import *


DEBUG = False;
TEMPLATE_DEBUG = False;



SECRET_KEY = '5ik@lvf!1e9y$ymk!goix36or^66bm9*tw@eeg#9i!@hd95sje';

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
