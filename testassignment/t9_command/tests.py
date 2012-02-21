from django.test import TestCase
from django.core.management import get_commands, call_command

COMMAND = 'listmodels'
class ListModelsCommandTest(TestCase):
    def test_command_call(self):
        commands_dict = get_commands()
        self.assertTrue(COMMAND in commands_dict)
        call_command(COMMAND)
