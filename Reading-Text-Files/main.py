# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from asyncore import read
from itertools import count


def read_file_content():
    # [assignment] Add your code here 
    f = open("story.txt", "r")
    file_info=f.read()
    f.close()
    return file_info

print(read_file_content())



def count_words():
    text = read_file_content()
    # [assignment] Add your code here
    text_words=text.split()
    count= {}
    for word in text_words:
        if word in count:
            count[word] +=1
        else:
            count[word] =1
    return count#{"as": 10, "would": 20}

print(count_words())