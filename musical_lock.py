import wave
import numpy as np

def peak_freq(fftdata):
    maxfreq = fftdata[1:].argmax() + 1

    # use quadratic interpolation around the max
    if maxfreq != len(fftdata) - 1:
        y0, y1, y2 = np.log(fftdata[maxfreq-1:maxfreq+2:])
        x1 = (y2 - y0) * 0.5 / (2 * y1 * y2 - y0)

        return maxfreq + x1
    else:
        return maxfreq

def freq2hz(freq, rate, chunksize):
    return freq * rate / chunksize

def read_freqs(wfile, wfrate, swidth, chunksize):
    freqs = []

    data = wfile.readframes(chunksize)
    while len(data) == chunksize * swidth:
        # unpack the data and multiply by the Blackman window
        indata = np.array(wave.struct.unpack("%dh" % (len(data)/swidth), data))
        hdata = indata * np.blackman(chunksize)

        # take the fft and square each value
        fftdata = abs(np.fft.rfft(hdata)) ** 2

        # find the peak freq, convert to hz and add it to the list of freqs
        freq = freq2hz(peak_freq(fftdata), wfrate, chunksize)
        freqs.append(freq)

        # read a new chunk of data
        data = wfile.readframes(chunksize)

    return freqs

def clean_freqs(freqs):
    rfreqs = [round(f, 2) for f in freqs]

    seen = set()
    return [f for f in rfreqs if f not in seen and not seen.add(f)]

def compare_floats(f1, f2, eps):
    return abs(f1 - f2) < eps

def compare_freqs(infreqs, cfreqs, prec):
    if len(infreqs) != len(cfreqs):
        return False
    
    return all(compare_floats(a, b, prec) for a,b in zip(infreqs, cfreqs))

def check_file(wfile, cfreqs, prec, chunksize=2048):
    wf = wave.open(wfile, 'r')
    wfrate = wf.getframerate()
    swidth = wf.getsampwidth()

    freqs = read_freqs(wf, wfrate, swidth, chunksize)
    return compare_freqs(clean_freqs(freqs), cfreqs, prec)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Determines whether a given wave file matches a musical lock combination.')

    parser.add_argument('infile', help='input wav file')
    parser.add_argument('precision', type=int, help='maximum degree of error for comparing input and expected notes')
    parser.add_argument('freqs', nargs='+', type=float, help='list of note frequencies that open the lock')
    args = parser.parse_args()

    print check_file(args.infile, args.freqs, args.precision, 8192)
