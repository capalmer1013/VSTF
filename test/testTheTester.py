# Who watches the watchmen?
# also this does not seem to work in pycharms. excellent.
import sys
sys.path.append('../')
import vstf.simpleTest
import os

print __file__
print os.getcwd()

vstf.simpleTest.runTests('exampleTest.yaml', cwd=os.getcwd())