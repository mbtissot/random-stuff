'''
'Look and say' sequences are sequences where the next term comes from reading the last term out loud.
The next number is, as you read the last number: (how many)(which number)
So, with a seed of 1, one would read: one one -> 11
So now our sequence is 1, 11.
Now, doing it again we have: two ones -> 21
Our sequence now is 1, 11, 21

The first 5 terms, starting with 1, are
1 (seed), 11 (one one), 21 (two ones), 1211 (one two, one one), 111221 (one one, one two, two ones)
'''

sequence = [1] # list defining the sequence. put your seed as the first element
n = 10 # how many terms do you want in your sequence?
while len(sequence)<n: # to generate n terms in the sequence
    valor = sequence[-1] # to generate the next term, we need to look at the last one
    v = str(valor) # converting to string
    string = '' # generating empty string
    index = 0 # index = counter of how many digits we've visited on the 'v'-string
    for c in v: # loops the characters of v
        contador = 0 # sets up counter
        for k in v[index:]: # loops on the characters of v again, but this time, as index goes up, visit fewer characters
            if c==k: # checks if the current character 'c' is equal to 'k' (current character of second loop)
                contador = contador + 1 # if so, adds 1 to the counter
            else:
                break # else, break and leave the for loop
            index = index+1 # increases index so that we don't loop around the entire string again
        if contador!=0: # if counter is not zero, adds to the string 'counter''number'
            string = string + str(contador) + str(c)
    sequence.append(string) # appends 'string' to the sequence. checks the while condition again.
print(sequence) # prints sequence :D