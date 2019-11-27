#S&A Passwordgenerator
==================
S&A were my first newbie projects in Python and something I did use a lot before migrating to "real" password managers.

The simple generator generates a 40-characters strong password with letters from 'a-z' 'A-Z', digits from '1-9' and all
special characters.
I simply reformat the code from time to time to make the code more 'efficient' and applying new stuff I've learned
e.g. list comprehension, interpolating methods, import statements and return statements

The advanced generator generates a password based on the user inputs such as length and what characters it should contain.
This code will als be reformatted in the future to apply new stuff e.g better user input controlling.

# Installation

1) `git clone https://github.com/N0W3N/PW-Gen.git`

or

1) download and unzip the package to your preferred path

2) change `[50] fileout = (os.path.expanduser("~") + "\Desktop\pw.txt")` in passwordgen adv.py to your own path if needed

# Usage

simply run `python passwordgen simple.py` or `python password adv.py` and follow the instructions