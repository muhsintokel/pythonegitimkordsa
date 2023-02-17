
var1 = '41,5,59,N'
a,b,c,d = var1.split(",") # => [41,5,59,N]
#                               0  1  2  3
# print(b)
print(var1.split(",")[1])


print("Metin değiştirme programına hoş geldiniz!")
text = input("Metni girin: ")
text = text.replace('a', '@')
text = text.replace('i', '!')
text = text.replace('o', '#')

print("Değiştirilmiş metin: ", text)
