def count_words(setences):
    setences = setences.split()
    return len(setences)


setences = input(" Enter a sentence: ")
print(f"They are exactly {count_words(setences)} words ")
# count_words("ont adore ca a ahhhh") 