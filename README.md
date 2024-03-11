# Haddock

Aren't you bored of reading and writing the same error messages over and over again
like "Wrong argument!", "End date must be after start date!" , "Division by zero!" etc. . With the haddock package you will be able to spice them up a bit:

- "Wrong argument, dipsomaniac!"
- "End date must be after start date, whipper-snapper!"
- "Division by zero, interplanetary goat!"

To do this, the method curse() of this package returns random curses from [Captain Haddock](https://en.wikipedia.org/wiki/Captain_Haddock). At the moment it supports curses in english (default), german and french. 

The sources for the curses are
- en: http://www3.sympatico.ca/brooksdr/haddock/main.htm
- de: https://weltenwandel.wordpress.com/2011/04/22/
die-1w100-fluche-des-kapitan-haddock/
- fr: https://fr.wikipedia.org/wiki/Vocabulaire_du_capitaine_Haddock

Pull requests for other languages are welcome.

## Installation

    pip install haddock-curses

## Usage

    import haddock
    >>> print(haddock.curse())
    anthropophagus!

You can use the [title() method](https://docs.python.org/3/library/stdtypes.html#str.title) from Python standard library to capitalize your swears.

    >>> print(haddock.curse().title())
    Brontosaurus!
    >>> print(haddock.curse(lang="de").title())
    Sie Logarithmus!
    >>> print(haddock.curse(lang="fr").title())
    Bande D'Ectoplasmes De Tonnerre De Brest 

You can decorate existing exception message with curses.

    >>> try: 0/0
    ... except Exception as e: print(str(e) + ", " + haddock.curse() + "!")
    ...
    division by zero, confounded rattletrap!!

## Upload to PyPi

The project needs poetry for package management. To install on e.g. Mac OS X do

    $ brew install poetry

Before you can upload packages to PyPi you need to create an account at PyPi, activate 2FA (e.g. use Google Authenticator)
and create an API-Token. Then you can configure poetry to use the API-Token like

    $ poetry config pypi-token.pypi <your-api-token>

You can then build and upload the package to PyPi simply by

    $ poetry build    # will build both sdist and wheel 
    $ poetry publish  # by default publishes to PyPi
