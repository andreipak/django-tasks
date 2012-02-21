from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import make_option
from django.db import models

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--tee-stderr',
            action='store_true',
            dest='tee',
            default=False,
            help='duplicate output to stderr'),

        make_option('--stderr-prefix',
            action="store",
            type="string",
            dest='prefix',
            default='error:',
            help='prefix for stderr output'),
    )

    help = 'Print all project models and the count of objects in every model'

    def handle(self, *args, **kwargs):
         for m in models.get_models():
            row = "%s.%s\t%2d" % (m.__module__, m.__name__,
                        m._default_manager.count())

            self.stdout.write('%s\n' % row)

            if kwargs.get('tee'):
                prefix = kwargs.get('prefix')
                if prefix:
                    self.stderr.write('%s %s\n' % (prefix, row))
                else:
                    self.stderr.write('%s\n' % row)
