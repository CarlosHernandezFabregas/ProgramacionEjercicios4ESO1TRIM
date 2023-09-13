Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#2. Programa que introduzca por teclado tres tipos de variables y se muestren por pantallaen el siguiente orden y formato: número entero, texto y número decimal.
>>> Var1=1
>>> print(Var1)
1
>>> Var2="a"
>>> print(Var2)
a
>>> Var3=6.8
>>> print(Var3)
6.8
>>> 1
1
>>> a
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> "a"
'a'
>>> 3.4
3.4
>>> B
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    B
NameError: name 'B' is not defined
>>> 5.4
5.4
>>> 3.4=error
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> "3.4"="error"
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> "3.4"=="error"
False
>>> "B"=="error"
False
>>> "5.4"=="error"
False
