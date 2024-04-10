import letters
def highest_freq(file):
    '''Given a file name, calls functions from letters.py and returns the letter with the highest frequency and its ratio'''
    letter_count = letters.letter_count(file)
    letter_freq = letters.letter_frequency(letter_count)
    keymax = max(letter_freq, key=letter_freq.get)
    return keymax, letter_freq[keymax]

ltr, freq = highest_freq('frost.txt')
#third test
assert(ltr) == 'e'
assert(freq) == 0.10952380952380952