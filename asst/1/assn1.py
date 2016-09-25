def swapchars(string):
    # Counting the letters
    letters = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            if (char in letters):
                letters[char] += 1
            else:
                letters[char] = 1

    # Returns the original string if there were no letters in it
    if len(letters) == 0:
        return string

    # Finding the most/least used char
    least = None
    most = None
    for letter, count in letters.iteritems():
        if least == None:
            least = (letter, count)
        elif (count < least[1]):
            least = (letter, count)

        if most == None:
            most = (letter, count)
        elif (count > most[1]):
            most = (letter, count)

    
    # Swapping the most used char with the least used char
    string_array = list(string)
    for i in xrange(len(string_array)):
        char = string[i]
        if char.lower() == least[0]:
            if char.isupper():
                string_array[i] = most[0].upper()
            else:
                string_array[i] = most[0]
        elif char.lower() == most[0]:
            if char.isupper():
                string_array[i] = least[0].upper()
            else:
                string_array[i] = least[0]

    return ''.join(string_array)
    


def sortcat(n, *args):
    # Using all strings if the first argument was -1
    if n == -1:
        n = len(args)

    # Sorting the args in order of length
    strings = sorted(args, key=len, reverse=True)

    # Concatenating the n longest strings together
    retval = ''
    for i in strings[0:n]:
        retval += i
    return retval



state_names = {}
def load_state_names(fileLoc):
    file = open(fileLoc, 'r')
    for line in file:
        a = line.split(',')
        state_names[a[1][0:2]] = a[0] # The substring of a[1] is to exclude the \n char from the key

def bluesclues(abbr):
    return state_names[abbr]

load_state_names('states.txt')
