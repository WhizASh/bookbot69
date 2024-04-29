from collections import Counter
def all_containt(book):
    with open(book) as f:
        containt = f.read()
        return (containt)

def count_word(book):
    with open(book) as f:
        containt = f.read()
        words = containt.split()
        return(len(words))

def count_letter(book):
    letters = dict()
    with open(book) as f:
        letters = dict(Counter(f.read().lower()))
        # print(letters)
        # for letter in f.read().lower():
        #     if letter in letters:
        #         #increment the key with value +1
        #         letters[letter] += 1
        #     else:
        #         #add the letter as key in dictionary
        #         letters[letter]=1
        letters = {i:val for i,val in letters.items() if i.isalpha()}
        return(letters)

def main(book):
    print(f"---------------------Report for {book}------------------------")
    print(f"{count_word(book)} words found in the document ")

    letters = count_letter(book)
    letters =sorted(letters.items(),key=lambda x:x[1],reverse=True)

    for letter,count in letters:
        print(f"The '{letter}' character was found {count} times")
    

main('books/frankenstein.txt')
# print(count_letter('books/frankenstein.txt'))
