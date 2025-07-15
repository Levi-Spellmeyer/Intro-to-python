def conversion(strSomeString):
    listCharacters = []
    for letter in range(len(strSomeString)):
        listCharacters += strSomeString[letter]
    return listCharacters

print(conversion("Levi"))



# this can actually be done using `Characters += "Levi"`