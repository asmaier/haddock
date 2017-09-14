# Haddock

The method curse() of this package returns random curses from [Captain Haddock](https://en.wikipedia.org/wiki/Captain_Haddock). At the moment it supports curses in english (default)
and german. 

The sources for the curses are
- en: http://www3.sympatico.ca/brooksdr/haddock/main.htm
- de: https://weltenwandel.wordpress.com/2011/04/22/die-1w100-fluche-des-kapitan-haddock/

Pull requests for other languages are welcome.

## Installation
Clone the git repository and execute the following command in the repository folder:

    python setup.py install

## Usage

    import haddock
    >>> print haddock.curse()
    Anthropophagus!
    >>> print haddock.curse(lang="de")
    Sie Logarithmus! 