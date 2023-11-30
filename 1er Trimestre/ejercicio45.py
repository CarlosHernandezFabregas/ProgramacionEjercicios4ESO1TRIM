#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
var1=str(input("introduce una palabra,:"))
Pi=""
low=""
for cont in var1:
    if cont=="a" or cont=="e" or cont=="i" or cont=="o" or cont=="u":
        Pi=Pi + cont
    else:low=low + cont
print("Vocales son:",Pi)
print("Consonantes son:",low)