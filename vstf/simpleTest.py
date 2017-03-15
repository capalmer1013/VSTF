import unittest
import os
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

    setattr(testClass, 'test_'+testInput.__name__, tempMethod)

def runTests(yamlFile):
    """
    :param yamlFile: a file defining tests to be performed
    :return: None
    """
    testConfig = yaml.load(open(yamlFile))
    sys.path.append(testConfig['importDir'])
    importModule = importlib.import_module(testConfig['moduleName'])
    
    unittest.main()