Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #4. A partir del código anterior, realiza una versión para números con decimales
>>> Var1=3.5
>>> Var2=3
>>> sum(Var1+Var2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sum(Var1+Var2)
TypeError: 'float' object is not iterable
>>> sum=(Var1+Var2)
>>> print(sum)
6.5
>>> print("Introduce una variable con valor 3.2 y otra con valor 3.1")
Introduce una variable con valor 3.2 y otra con valor 3.1
>>> Var3=3.2
>>> Var4=3.1
>>> sum=(Var3+Var4)
>>> print(sum)
6.300000000000001
