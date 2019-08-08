from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='haddock-curses',
	  version='0.1.4',
	  description='Random curses from Captain Haddock.',
	  long_description=readme(),
	  classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
	'Natural Language :: English',
	'Natural Language :: French',
	'Natural Language :: German',
        'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
        'Topic :: Utilities',
      ],
	  url='https://github.com/asmaier/haddock',
	  author='asmaier',
	  author_email='asmaier@web.de',
	  license='MIT',
	  packages=find_packages(),
	  include_package_data=True,
	  zip_safe=False)
