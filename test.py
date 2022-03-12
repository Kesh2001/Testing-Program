# It is simply another python file
# if we have 100 fies of python then each module will have its own test module
# This file is never produced. It is only there to test that before released everything works in main
# pylint,pyflakes, pep8 are just basic tests, however testing is another level up
import unittest  # built-in module for testing
import main  # to test this file


class TestMain(unittest.TestCase):
    def setUp(self):  # sets-up before each call of a test
        print('About to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # if we put 10, we get a FAIL in command prompt

    def test_do_stuff2(self):
        test_param = 'sksihdiw'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))  # can also use assertIsInstance

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please Enter Number ')

    def test_do_stuff4(self):
        ''' Hiiiiiiii'''  # to add comments to ur test that will be displayed in details
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please Enter Number ')

    def tearDown(self):  # runs at end of every function
        print('Cleaning Up')


if __name__ == '__main__':
    unittest.main()  # this has nothing to do with the name of the file it simply tells to run the tests
# if we want to run all tests in unison we write in com prt"python -m unittest"
# write "touch test2.py" to make a new file in the current dir and paste the same code there
# and then run the same command we have twice the num of tests cause we wrote the if statement at last
# "python -m unittest -v" gives details about each test individually
