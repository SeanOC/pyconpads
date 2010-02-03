import os, sys, site
sys.path.append('/srv/pyconpads')
sys.path.append('/srv/pyconpads/pyconpads')
site.addsitedir('/srv/pyconpads/env/lib/python2.5/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pyconpads.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
