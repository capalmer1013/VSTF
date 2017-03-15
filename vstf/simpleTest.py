import os
import unittest
import yaml
import sys
import importlib


class testClass(unittest.TestCase):
    def runTest(self):
        # only for testing the test script
        pass


def generateTestFunctions(testInput, testOutput, message=None):
    def tempMethod(self):
        self.assertEqual(testInput(), testOutput, msg=message)

    setattr(testClass, 'test_'+testInput, tempMethod)

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
        generateTestFunctions(testFunc, testConfig['tests'][testFunc])

    unittest.main()

