from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='haddock-curses',
	  version='0.1.3',
	  description='Random curses from Captain Haddock.',
	  long_description=readme(),
	  classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
      ],
	  url='https://github.com/asmaier/haddock',
	  author='asmaier',
	  author_email='asmaier@web.de',
	  license='MIT',
	  packages=find_packages(),
	  include_package_data=True,
	  zip_safe=False)
