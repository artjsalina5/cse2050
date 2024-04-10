import string

def letter_count(file):
    '''Counts the instances of each ascii character from a file and returns an alphabetized dictionary'''
    with open(file) as f:
        count = {}
        data = f.read()
        data = data.lower()
        for char in data:
            if char in string.ascii_lowercase:
                count[char] = count.get(char, 0) + 1 #check a-z frequency with default value of 0
    sorted_count = {}
    for key in sorted(count):
        sorted_count[key] = count[key]
    return sorted_count

def letter_frequency(dict_letters):
    '''Given a dictionary of letters and their values, returns the ratio or frequency of each character in relation to the others in an alphabetized dictionary'''
    total = sum(dict_letters.values())
    freqs = {}
    for letter, count in dict_letters.items():
        freqs[letter] = count / total
    return freqs

if __name__ == '__main__':
   #first test
    frostdict = {'a': 13, 'b': 2, 'c': 6, 'd': 10, 'e': 23, 'f': 12, 'g': 2, 'h': 12, 'i': 23, 'k': 2, 'l': 6, 'm': 3, 'n': 9, 'o': 20, 'p': 1, 'r': 14, 's': 14, 't': 20, 'u': 5, 'v': 2, 'w': 8, 'y': 3}
    assert(letter_count('frost.txt')) == frostdict
   #second test
    frostfreq = {'a': 0.06190476190476191, 'b': 0.009523809523809525, 'c': 0.02857142857142857, 'd': 0.047619047619047616, 'e': 0.10952380952380952, 'f': 0.05714285714285714, 'g': 0.009523809523809525, 'h': 0.05714285714285714, 'i': 0.10952380952380952, 'k': 0.009523809523809525, 'l': 0.02857142857142857, 'm': 0.014285714285714285, 'n': 0.04285714285714286, 'o': 0.09523809523809523, 'p': 0.004761904761904762, 'r': 0.06666666666666667, 's': 0.06666666666666667, 't': 0.09523809523809523, 'u': 0.023809523809523808, 'v': 0.009523809523809525, 'w': 0.0380952380952381, 'y': 0.014285714285714285}
    assert(letter_frequency(letter_count('frost.txt'))) == frostfreq