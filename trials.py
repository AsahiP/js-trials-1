"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    
    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")

        i += 1


def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)


def censor_vowels(word):
    chars = []

    for letter in word:
        if 'aeiou' in letter:
            chars.append('*')
        else:
            chars.append(letter)

    return chars.join("")
        

def snake_to_camel(string):
    camel_case = []
    new_strg = string.split('_')

    for word in new_strg:
        camel_case.append(f"{word[0].upper()}{word[1:]}")
    
    return camel_case.join("")



def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest

def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result - 1)]:
            result.append(char)

    return result.join('')


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
            # if parens < 0:
            if parens != 0:
                return False

    

def compress(string):
    compress = []

    current_char = ""
    char_count = 0

    for char in string:
        if char != current_char:
            compress.append(current_char)

            if char_count > 1:
                compress.append(str(char_count))

            
            current_char = char
            char_count = 0

        char_count +=1

    compress.append(current_char):
    if char_count > 1:
        compress.append(str(char_count))

    return compress.join("")
