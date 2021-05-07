words = []


def prompt(kind):
    ask = "Please enter " + kind + ":"
    word = input(ask)

    words.append(word)


prompt("an adjective")
prompt("a nationality")
prompt("a person")
prompt("a plural noun")
prompt("an adjective")
prompt("a plural noun")

print("Computers were invented by a", words[0], words[1],
"engineer named", words[2], ". To make a computer, you need to take a lot of", words[3], ", melt them down, and make",
words[4], words[5], ".")