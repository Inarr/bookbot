def word_count(text):
    word = text.split()
    return (len(word))

def letter_count(text):
    lower_case = text.lower()
    words = lower_case.split()
    letters={"a":0,"b":0,"c":0,"d":0,"e":0,
    "f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,
    "m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter]+=1
    return letters

def sort_on(dict):
    return dict["num"]

def letter_sort(letters):
    letter_list=[]
    for i in letters:
        letter_list.append(dict(letter=i, num=letters[i]))
    letter_list.sort(reverse=True, key=sort_on)
    for i in letter_list:
        print(f"The letter '{i["letter"]}' appears {i["num"]} times")
    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        print("")
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count(file_contents)} words were found in the document")
        print("")
        letter_sort(letter_count(file_contents))
        print("")
        
main()   