from setuptools import setup, find_packages
import sys

sys.path.append('./storybuilder/builder')
sys.path.append('./src')
sys.path.append('./tests')

setup(
        name = 'EveryStar short novel',
        version = '0.0.2',
        description = "This is novels that upload to the EveryStar",
        packages = find_packages(),
        test_suite = 'test_all.suite'
)
