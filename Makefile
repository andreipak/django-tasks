APP = testassignment
SETTINGS = settings

PWD = $(shell pwd)
MANAGESCRIPT = django-admin.py
MANAGE = PYTHONPATH=$(PWD):$(PWD)/$(APP) DJANGO_SETTINGS_MODULE=$(APP).$(SETTINGS) $(MANAGESCRIPT)

test:
	$(MANAGE) test

run:
	$(MANAGE) runserver

#using werkzeug thru django-devserver
werkzeug:
	$(MANAGE) runserver --werkzeug

syncdb:
	$(MANAGE) syncdb --noinput
