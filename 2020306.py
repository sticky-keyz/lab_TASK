def Caesar_Cipher_Encrypition(Text, shifts):
    D = Text
    for i in range(shifts):
        Encription = []
        for i in range(len(D)):
            a = ord(D[i])
            if a >= 65 and a <= 90:
                a = (a + 1)
                a -= 65
                a %= 26
                a += 65
            elif a >= 97 and a <= 122:
                a = (a + 1)
                a -= 97
                a %= 26
                a += 97
            Encription.append(chr(a))
        D = Encription[0]
        for i in range(1,len(Text)):
            D += Encription[i]
    return D

def function(Text, shifts):
    Data = Text
    for i in range(shifts):
        Dencription = []
        for i in range(len(Data)):
            a = ord(Data[i])
            if a >= 65 and a <= 90:
                a = (a - 1)
                a -= 65
                a %= 26
                a += 65
            elif a >= 97 and a <= 122:
                a = (a - 1)
                a -= 97
                a %= 26
                a += 97
            Dencription.append(chr(a))
        Data = Dencription[0]
        for i in range(1,len(Text)):
            Data += Dencription[i]
    return Data

Plain_Text = "Hassan and Umer are the Best"
En_Data = Caesar_Cipher_Encrypition(Plain_Text, 0)
input("Encripition: ", En_Data)

Data = function(En_Data, 0)
input("Decripition: ", Data)
