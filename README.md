# Musical Lock

From [ScavHunt 2011](http://scavhunt.uchicago.edu/lists/2011.pdf):

> A lock that opens to a unique combination of musical inputs. The key may be either a series of tones that could be replicated by anyone or the direct mechanical operation of a customized instrument.

## Usage

Basic command line structure:

````python
python musical_lock.py infile precision freqs [freqs ...]
````

Working example:

````python
python musical_lock.py test.wav 3 293.63 440.00 293.66 392.00
````
