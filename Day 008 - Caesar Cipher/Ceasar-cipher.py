import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(word,shift,type):
    end = ""
    shift=int(shift)
    shift = shift %26
    if type == "de":
        shift *= -1
    for i in word.lower():
        if i in alphabet:
            end += alphabet[alphabet.index(i)+shift]
        else: end += i

    print(end)
    result = input("Do you wanna go again ")
    if result == "Yes":
        return ceasar(input("type a word "), input("shift number "),input("type"))
    else:
        print("Suckers ")
        return


ceasar(input("type a word "), input("shift number "),input("type"))
    
    
    
