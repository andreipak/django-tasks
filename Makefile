APP = testassignment
SETTINGS = settings

PWD = $(shell pwd)
MANAGESCRIPT = django-admin.py
MANAGE = PYTHONPATH=$(PWD) DJANGO_SETTINGS_MODULE=$(APP).$(SETTINGS) $(MANAGESCRIPT)

test:
	$(MANAGE) test

run:
	$(MANAGE) runserver

#using werkzeug thru django-devserver
devserver:
	$(MANAGE) runserver --werkzeug

syncdb:
	$(MANAGE) syncdb --noinput
