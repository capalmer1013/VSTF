import os
import unittest
import yaml
import sys
import importlib


class TestClass(unittest.TestCase):
    def runTest(self):
        pass

    def test_pretest(self):
        self.assertEqual('foo'.upper(), 'FOO')


def generateTestFunctions(testInput, testOutput, importModule, message=None):
    def tempMethod(self):
        self.assertEqual(importModule.__dict__[testInput](), testOutput, msg=message)

    setattr(TestClass, 'test_'+testInput, tempMethod)


def runTests(yamlFile, cwd=''):
    """
    :param yamlFile: a file defining tests to be performed
    :param cwd: current working dir if giving a relative path name
    :return: None
    """
    testConfig = yaml.load(open(cwd+'/'+yamlFile))
    sys.path.append(testConfig['importDir'])
    importModule = importlib.import_module(testConfig['moduleName'])

    for testFunc in testConfig['tests']:
        generateTestFunctions(testFunc, testConfig['tests'][testFunc], importModule)

    unittest.main()



if __name__ == "__main__":
    unittest.main()
