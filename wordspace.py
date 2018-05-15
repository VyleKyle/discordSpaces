while True:
    print("Gimme a phrase to space out")
    phrase = input()
    newphrase = ""
    for x in phrase:
        newphrase = newphrase + x + " "
    print(newphrase)
    
