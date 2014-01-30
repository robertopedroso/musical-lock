# Musical Lock

From [ScavHunt 2011](http://scavhunt.uchicago.edu/lists/2011.pdf):

> A lock that opens to a unique combination of musical inputs. The key may be either a series of tones that could be replicated by anyone or the direct mechanical operation of a customized instrument.

This item was never completed by Max Scav in 2011 but I pursued it on a whim in January 2014.

Back in 2011, most teams completed the item using a MIDI keyboard or something of that sort. While that is a perfectly valid way to complete the item, it doesn't really use a 'musical input' to unlock a secret. In the case of the MIDI keyboard, the music merely serves as audible feedback for an ordinary button-operated digital combination lock.

Instead, this musical lock takes a wave file as input and determines whether the encoded tune matches a preset list of frequencies. This way, any sound source can be used so long as the resulting wave file contains a well-formed sequence of tones.

## Usage

Basic command line structure:

````python
python musical_lock.py infile precision freqs [freqs ...]
````

Working example:

````python
python musical_lock.py test.wav 3 293.63 440.00 293.66 392.00
````
