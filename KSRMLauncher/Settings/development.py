from .base import *
import django_heroku
# override base.py here


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0']

INSTALLED_APPS +=[
    # 'debug_toolbar' ,
]

# MIDDLEWARE +=[
#     'debug_toolbar.middleware.DebugToolbarMiddleware'
# ]

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.Settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
# ]

# def show_toolbar(request):
#     return True
#
# DEBUG_TOOLBAR_CONFIG = {
#
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TOOLBAR_CALLBACK': show_toolbar,
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db' ,
        'USER': "root",
        'PASSWORD': "pass@123" ,
        'HOST': '127.0.0.1' ,
        'PORT': "3306" ,
'OPTIONS':{
        "init_command":"SET foreign_key_checks = 0;",
    }

    }
}



STRIPE_PUBLIC_KEY =''
STRIPE_SECRET_KEY =''
django_heroku.settings(locals())