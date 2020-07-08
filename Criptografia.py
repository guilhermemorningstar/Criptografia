import string
alfabeto = list(string.ascii_lowercase)

for l in range(17):
    palavra = input( "Digite uma palavra: ")
    key = int(input("digite a chave: "))
    for i in range(len(palavra)):
        for x in range(len(alfabeto)):
            if(alfabeto[x] == palavra[i]):
                print(palavra[i], '' + alfabeto[x - key])