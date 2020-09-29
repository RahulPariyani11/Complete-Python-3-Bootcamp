#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[ ]:


NAME = "Rahul Pariyani"
COLLABORATORS = ""


# ---

# This problem set has two parts. The first part allows you to practice thinking about problems in a recursive fashion, taking advantage of the idea that one can reduce the problem to a simpler version of the same problem. 
# 
# First, you will write a recursive function that takes as input a string and figures out all the possible
# reorderings of the characters in the string.
# 
# The second part will give you experience in thinking about problems in terms of classes, each instance of which contains specific attributes as well as methods for manipulating them. You will use object-oriented programming to write a Caesar/shift cipher. 
# 
# I would like you to look at the [Google Style Guide](http://google.github.io/styleguide/pyguide.html). You don't need to follow everything in this style guide but I will deduct points for non-descriptive variable names and uncommented code (particularly, class and function signatures)
# 

# ### Part A (10 points) - Permutations of a String
# 
# A permutation is simply a name for a reordering. So the permutations of the string‘abc’ are ‘abc’, ‘acb’, ‘bac’, ‘bca’, ‘cab’, and ‘cba’. Note that a sequence is a permutation of itself (the trivial permutation). For this part of the pset you’ll need to write a **recursive** function get_permutations that takes a string and returns a
# list of all its permutations. You will find this function helpful later in the pset
# 
# A couple of notes on the requirements: Recursion MUST be used, global variables may NOT be used. Additionally, it is okay to use loops to code the solution. The order of the returned permutations does not matter. Please also avoid returning duplicates in your final list.

# In[ ]:


import string
def get_permutations(sequence):
    """Enumerate all permutations of a given string.

    Args:
        sequence (string): an arbitrary string to permute. Assume that it is a
        non-empty string.  
    
    Returns: 
        a list of all permutations of sequence.
    """
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


from nose.tools import assert_equal
assert_equal(set(get_permutations('abc')),set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))


# ### Part B (25 points) - Cipher like Caesar
# 
# Ever want to relive the glory days of your youth and pass secret messages to your friends? Well, here is your chance! But first, here is some vocabulary:
# 
# - Encryption - the process of obscuring or encoding messages to make them unreadable
# - Decryption - making encrypted messages readable again by decoding them
# - Cipher - algorithm for performing encryption and decryption
# - Plaintext - the original message
# - Ciphertext - the encrypted message. Note: a ciphertext still contains all of the original message information, even if it looks like gibberish. 
# 
# **Caesar Cipher**
# 
# The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is $k$. Then, all instances of the $i^{th}$ letter of the alphabet that appear in the plaintext should become the $(i + k)^{th}$ letter of the alphabet in the ciphertext. You will need to be careful with the case in which $i + k > 26$ (the length of the alphabet).
# 
# We will treat uppercase and lowercase letters individually, so that uppercase letters are always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. If an uppercase letter maps to “A”, then the same lowercase letter should map to “a”. Punctuation and spaces should be retained and not changed. For example, a plaintext message with a comma should have a corresponding ciphertext with a comma in the same position.
# 
# **Examples**:
# 
# |Plaintext|shift|Ciphertext|
# |---------|-----|----------|
# |'abcdef'|2|'cdefgh'|
# |'Hello World!'|4|'Lipps Asvph!'|
# |''|any value|''|
# 
# 
# **Classes and Inheritance**
# 
# This is your first experience coding with classes! Get excited! We will have a `Message` class with two subclasses `PlaintextMessage` and `CiphertextMessage`. `Message` contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action). `PlaintextMessage` has methods to encode a string using a specified shift value; our class will always create an encoded version of the message, and will have methods for changing the encoding. `CiphertextMessage` contains a method used to decode a string.
# 
# When you have completed your implementation, you can either create a `CiphertextMessage` instance using an encrypted string that someone provides you and try to decrypt it; or you can encrypt your own `PlaintextMessage` instance, then create a `CiphertextMessage` instance from the encrypted message within the `PlaintextMessage` instance, and try to decrypt it and see if it matches the original plaintext message.
# 
# **Your job will be to fill methods for all three of these classes according to the specifications given in the docstrings**. Please remember that you never want to directly access attributes outside a class - that’s why you have getter and setter methods. Don’t overthink this; a getter method should just return an attribute and a set method should just set an attribute equal to the argument passed in. Although they seem simple, we need these methods in order to make sure that we are not manipulating attributes we shouldn’t be. Directly using class attributes outside of the class itself instead of using getters and setters will result in a point deduction – and more importantly can cause you headaches as you design and implement object class hierarchies. 
# 
# **Rules**
# 
# You do not have to use recursion in Part B, but you are welcome to. There are a couple of helper functions that we have implemented for you: `load_words` and `is_word`. You may use these in your solution and you do not need to understand them completely, but should read the associated comments. You should read and understand the helper code in the rest of the file and use it to guide your solution. 
# 
# 
# 

# In[2]:


### HELPER CODE ###

def load_words(file_name):
    """
    Args:
        file_name (string): the name of the file containing 
        the list of words to load.
        
    Returns: 
        a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    """ Determines if word is a valid word, ignoring capitalization 
        and punctuation.
        
    Args:
        word_list (list): list of words in the dictionary.
        word (string): a possible word.
    
    Returns: 
        True if word is in word_list, False otherwise.

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: 
        a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


# In[ ]:


import string
WORDLIST_FILENAME = 'words.txt'

class Message():
    
    def __init__(self, message_text, valid_words):
        """Initializes a Message object.
        
        Args:
            text (string): the message's text

            a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        # YOUR CODE HERE
        
        self.message_text=message_text
        self.valid_words=valid_words
        
        raise NotImplementedError()
        
    def get_message_text(self):
        """Used to safely access self.message_text outside of the class.
        
        Returns: 
            self.message_text
        """
        # YOUR CODE HERE
        
        self.message_text=input("Please enter secret message")
        return self.message_text
    
        raise NotImplementedError()


    def get_valid_words(self):
        """Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: 
            a COPY of self.valid_words.
        """
        # YOUR CODE HERE
        return self.message_text.split(" ")
    
        raise NotImplementedError()
        
    def build_shift_dict(self, shift):
        """Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        Args:
            shift (integer): the amount by which to shift every letter of the 
            alphabet. 0 <= shift < 26.

        Returns: 
            a dictionary mapping a letter (string) to another letter (string). 
        """
        ###Note: you may find the string  module’s ascii_lowercase constant helpful here.
        
        # YOUR CODE HERE
        
        d={}  #defined an empty dictionary
        
        d = { k: v for k, v in enumerate(string.ascii_lowercase) 
        
        for i in string.ascii_lowercase:
            
            
        raise NotImplementedError()


    def apply_shift(self, shift):
        """Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        .
        
        Args:
            shift (integer): the shift with which to encrypt the message.
            0 <= shift < 26.

        Returns: 
            the message text (string) in which every character is shifted
            down the alphabet by the input shift.
        """
###Hint: use build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.
        
        # YOUR CODE HERE
        raise NotImplementedError()
            

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """Initializes a PlaintextMessage object.
        
        Args:
            text (string): the message's text
            shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        # YOUR CODE HERE
        raise NotImplementedError()


    def get_shift(self):
        """Used to safely access self.shift outside of the class.
        
        Returns: 
            self.shift
        """
        # YOUR CODE HERE
        raise NotImplementedError()

    def get_encryption_dict(self):
        """Used to safely access a copy self.encryption_dict outside of the class.
        
        Returns: 
            a COPY of self.encryption_dict.
        """
        # YOUR CODE HERE
        raise NotImplementedError()

    def get_message_text_encrypted(self):
        """Used to safely access self.message_text_encrypted outside of the class.
        
        Returns: 
            self.message_text_encrypted.
        """
        # YOUR CODE HERE
        raise NotImplementedError()


    def change_shift(self, shift):
        """Changes self.shift of the PlaintextMessage and updates other 
            attributes determined by shift.        
        
        Args:
            shift (integer): the new shift that should be associated with this message.
            0 <= shift < 26.

        Returns: 
            nothing
        """
        # YOUR CODE HERE
        raise NotImplementedError()

    ###Hint: think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code


class CiphertextMessage(Message):
    def __init__(self, text):
            
        """Initializes a CiphertextMessage object.
        
        Args:
            text (string): the message's text.

            a CiphertextMessage object has two attributes:
                self.message_text (string, determined by input text)
                self.valid_words (list, determined using helper function load_words)
        """
###Hint: use the parent class constructor to make your code more concise.
        # YOUR CODE HERE
             
             def encrypt(string, shift):
                 cipher=''
                 for char in sef.message_text:
                     if char == ' ':
                         cipher=cipher+char
                    elif char.isupper():
                         cipher+=chr((ord(char) + shift - 65)%26 +65)
                    else:
                         cipher+=chr((ord(char) + shift - 97)%26 +97)
                return cipher
    

    print("Message after encryption: ", encrypt(self.message_text,s))
             
        raise NotImplementedError()


    def decrypt_message(self):
        """Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return.

        Returns: 
            a tuple of the best shift value used to decrypt the message
            and the decrypted message text using that shift value.
        """
        # YOUR CODE HERE
             
             
        raise NotImplementedError()
        
            
                    
###Hint: you may find the helper function is_word(wordlist, word) and the string method split useful (https://docs.python.org/3/library/stdtypes.html#str.split)

###Note: is_word will ignore punctuation and other special characters when considering whether a word is valid.


# In[ ]:


from nose.tools import assert_equal
plaintext = PlaintextMessage('hello', 2)
assert_equal(plaintext.get_message_text_encrypted(),'jgnnq')
ciphertext = CiphertextMessage('jgnnq')
assert_equal(ciphertext.decrypt_message(), (24, 'hello'))


# ### Part C (15 points): Substitution Cipher
# 
# A better way to hide your messages is to use a substitution cipher. In this approach, you create a hidden coding scheme, in which you substitute a randomly selected letter for each original letter. For the letter “a”, you could pick any of the other 26 letters (including keeping “a”), for the letter “b”, you could then pick any of the remaining 25 letters (other than what you selected for “a”) and so on. You can probably see that the number of possibilities to test if you wanted to decrypt a substitution ciphered message is much larger than for a Caesar cipher (26! compared to 26). So for this problem, we are going to just consider substitution ciphers in which the vowels are encrypted, with lowercase and uppercase versions of a letter being mapped to corresponding letters. (For example, ‘A’ -> ‘O’ then ‘a’->’o’).
# 
# **Classes and Inheritance**
# 
# Similar to the Caesar cipher, we are going to use classes to explore this idea. We will have a `SubMessage` class with general functions for handling Substitution Messages of this kind. We will also write a class with a more specific implementation and specification, `EncryptedSubMessage`, that inherits from the `SubMessage` class.
# 
# Your job will be to fill methods for both classes according to the specifications given in the docstrings. Please remember that you never want to directly access attributes outside a class - that’s why you have getter and setter methods. Again, don’t overthink this; a get method should just return a variable and a set method should just set an attribute equal to the parameter passed in. Although they are simple, we need these methods in order to make sure that we are not manipulating attributes we shouldn’t be. Directly using class attributes outside of the class itself instead of using getters and setters will result in a point deduction – and more importantly can cause you headaches as you design and implement object class hierarchies.
# 
# 

# In[ ]:


WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        """Initializes a SubMessage object.
        
        Args:
            text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        # YOUR CODE HERE
        raise NotImplementedError()
        
    def get_message_text(self):
        """Used to safely access self.message_text outside of the class.
        
        Returns: 
            self.message_text.
        """
        # YOUR CODE HERE
        raise NotImplementedError()
        
    def get_valid_words(self):
        """Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: 
            a COPY of self.valid_words
        """
        # YOUR CODE HERE
        raise NotImplementedError()
        
    def build_transpose_dict(self, vowels_permutation):
        """
        Args:
            vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: 
            a dictionary mapping a letter (string) to another letter (string). 
        """
        
        # YOUR CODE HERE
        raise NotImplementedError()

    def apply_transpose(self, transpose_dict):
        """
        Args:
            transpose_dict (dict): a transpose dictionary.
        
        Returns: 
            an encrypted version of the message text, based on the dictionary.
        """
        # YOUR CODE HERE
        raise NotImplementedError()

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        """Initializes an EncryptedSubMessage object

        Args:
            text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        # YOUR CODE HERE
        raise NotImplementedError()
        
    def decrypt_message(self):
        """Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: 
            the best decrypted message.
        
        """
###Hint: Use the Permutation function you wrote in Part A
        # YOUR CODE HERE
        raise NotImplementedError()


# In[ ]:


from nose.tools import assert_equal
message = SubMessage("Hello World!")
permutation = "eaiuo"
enc_dict = message.build_transpose_dict(permutation)
assert_equal(message.apply_transpose(enc_dict),"Hallu Wurld!")
enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
assert_equal(enc_message.decrypt_message(),"Hello World!")

