def to_find(word: str):
    word = word.lower()
    amount_ = "_" * len(word)
    amount_ = "".join(amount_)
    result = list(word)
    print(f"Let's plat\nThere is word with {amount_} -> {len(word)} letters\n Try to guess!")
    while True:
        letter = str(input("Pls enter a letter : "))
        if letter in word:
            index = word.find(letter)
            amount_ = list(amount_)
            index_of = [index for index, l in enumerate(word) if l == letter]
            for index in index_of:
                amount_[index] = letter
                if amount_ == result:
                    return f"This word was {word}, you won!"
            print(*amount_)
        else:
            amount_ = "".join(amount_)
            print(f"There is no this letter\nYour word is ~{amount_}~")


a_word = "Milica"
print(to_find(a_word))