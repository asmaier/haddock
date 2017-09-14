from setuptools import setup, find_packages

setup(name='haddock',
	  version='0.1',
	  description='Random curses from Captain Haddock.',
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
