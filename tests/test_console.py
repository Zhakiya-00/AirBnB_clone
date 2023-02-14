import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        # Test create command with missing class name
        self.cli.onecmd("create")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

        # Test create command with invalid class name
        self.cli.onecmd("create InvalidClass")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test create command with valid class name
        self.cli.onecmd("create BaseModel")
        self.assertNotEqual("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        # Test show command with missing class name
        self.cli.onecmd("show")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

        # Test show command with invalid class name
        self.cli.onecmd("show InvalidClass")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test show command with missing instance id
        self.cli.onecmd("show BaseModel")
        self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

        # Test show command with invalid instance id
        self.cli.onecmd("show BaseModel 123")
        self.assertEqual("** no instance found **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        # Test destroy command with missing class name
        self.cli.onecmd("destroy")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

        # Test destroy command with invalid class name
        self.cli.onecmd("destroy InvalidClass")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test destroy command with missing instance id
        self.cli.onecmd("destroy BaseModel")
        self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

        # Test destroy command with invalid instance id
        self.cli.onecmd("destroy BaseModel 123")
        self.assertEqual("** no instance found **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        # Test all command with invalid class name
        self.cli.onecmd("all InvalidClass")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test all command with valid class name
        self.cli.onecmd("all BaseModel")
        self.assertNotEqual("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        # Test update command with missing class name
        self.cli.onecmd("update")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

        # Test update command with invalid class name
        self.cli.onecmd("update InvalidClass")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test update command with missing instance id
        self.cli.onecmd("update BaseModel")
        self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

        # Test update command with invalid instance id
        self.cli.onecmd("
