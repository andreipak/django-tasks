from django.test import TestCase
from django.core.management import get_commands, call_command

COMMAND = 'listmodels'

class ListModelsCommandTest(TestCase):
    def test_command_call(self):
        commands_dict = get_commands()
        self.assertTrue(COMMAND in commands_dict)
        has_errors = False
        try:
            call_command(COMMAND)
        except:
            has_errors = True

        self.assertEqual(has_errors, False)
