# Haddock

The method curse() of this package returns random curses from [Captain Haddock](https://en.wikipedia.org/wiki/Captain_Haddock). At the moment it supports curses in english (default), german and french. 

The sources for the curses are
- en: http://www3.sympatico.ca/brooksdr/haddock/main.htm
- de: https://weltenwandel.wordpress.com/2011/04/22/
die-1w100-fluche-des-kapitan-haddock/
- fr: https://fr.wikipedia.org/wiki/Vocabulaire_du_capitaine_Haddock

Pull requests for other languages are welcome.

## Installation
Clone the git repository and execute the following command in the repository folder:

    python setup.py install

## Usage

    import haddock
    >>> print haddock.curse()
    anthropophagus!
    >>> print haddock.curse(title=True)
    Brontosaurus!
    >>> print haddock.curse(lang="de", title=True)
    Sie Logarithmus!
    >>> print(haddock.curse(lang="fr", title=True))
    Bande D'Ectoplasmes De Tonnerre De Brest 
