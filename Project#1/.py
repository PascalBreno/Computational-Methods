# encoding = utf-8
def testfuncion(a, b):
    if (function(a) < 0 and function(b) < 0):
        print('valores invalidos')
        return 0
    if (function(a) > 0 and function(b) > 0):
        print('valores invalidos')
        return 0

def false_position(a, b):
    if(testfuncion(a, b)==0):
        return 0
    x = newx_falseposition(a, b)
    f_a = function(a)
    f_b = function(b)
    while (abs(function(x)) > 0.001):
        if ((function(x) > 0 and function(a) > 0) or (function(x) < 0 and function(a) < 0)):
            a = x
        else:
            b = x
        x = newx_falseposition(a, b)

    print '     -----------METODO DA POSICAO FALSA----------'
    print('          valor de x = %.4f' % x)
    print('          false position = %.4f' % function(newx_falseposition(a, b)))
    print '     --------------------------------------------'


def newton(a):
    f_x = function(a)
    fd_x = functiondev(a)
    x_ant = a
    x = a
    while (abs(function(x)) > 0.001):
        x_ant = x
        x = x_ant - (f_x / fd_x)
        f_x = function(x)
        fd_x = functiondev(x)
    print '     -----------METODO DE NEWTON-----------------'
    print('          valor de x = %.4f' % x)
    print('          false position = %.4f' % function(x))
    print '     --------------------------------------------'


def functionsecante(x1, x2):
    return ((x1 * function(x2)) - (x2 * function(x1))) / (function(x2) - function(x1))


def secante(a, b):
    x1 = a
    x2 = b
    x = functionsecante(x1, x2)
    while (abs(function(x)) > 0.001):
        x1 = x2
        x2 = x
        x = functionsecante(x1, x2)
    print '     -----------METODO DA SECANTE----------------'
    print('          valor de x = %.4f' % x)
    print('          false position = %.4f' % function(x))
    print '     --------------------------------------------'


def newx_falseposition(a, b):
    x = ((a * function(b)) - (b * function(a))) / (function(b) - function(a))

    return x


def novox(x, y):
    a = (x + y) / 2
    return a


def Error_Method(larger, smaller):
    if (testfuncion(a, b)==0):
        return 0
    x = novox(larger, smaller) / 1.0
    while (abs(function(x)) > 0.001):
        if (function(x) > 0):
            larger = x
        else:
            smaller = x
        x = novox(larger, smaller) / 1.0
    print '     -----------METODO DO ERRO---------------'
    print('          valor de x = %.4f' % x)
    print('          false position = %.4f' % (function(x)))
    print '     -----------------------------------------'



'''
    Here it's where begin this program, first read another file with functions separated by ' ; ' (normal function; derived function and interval)
'''

import os.path


if (os.path.exists('function.txt')):
    arquivo = open('function.txt', 'r')
    string = arquivo.read()
    string = string.split(';')
    functiond = string[0]
    functionderivada2 = string[1]
    valores = string[2].split(',')
    a = float(valores[0])
    b = float(valores[1])

    '''
    The name file is "Function.txt", now the programing read and separate the functions in differents Strings then convert the string with interval for 'float' to use in function
    '''

else:
    print('arquivo nao existe')
    exit()
'''
    Here it's when the functions (Function normal and Function Derived) are stored in function for to used before.
    1- Stored the functions in new file with extends .py.
    2 - To use the new files with the functions (Normal and derived).
'''
# add in file 'normalfuncion.py' the function (function normal).

functionnormal = open('normalfunction.py', 'w')
functionnormal.write('def function(x):')
functionnormal.write('\n')
functionnormal.write('  return ' + functiond)
functionnormal.close()

# add in file 'normalderived.py' the function (function derived).

functionderived = open('functionderived.py', 'w')
functionderived.write('def functiondev(x):')
functionderived.write('\n')
functionderived.write('  return ' + functionderivada2)
functionderived.close()

#now imported the new file 'funcioderived' and 'functionnormal'

from functionderived import functiondev
from functionormal import function

# ---Here coming the calculus.---

#First needed to identify the largest value in interval for use in function.---
if (function(a) > 0):
    larger = a
    smaller = b
else:
    larger = b
    smaller = a
#---------------------------------------------------------------------------
#Now use this methods for find your answer
Error_Method(larger, smaller)
false_position(a, b)
newton(a)
secante(a, b)
arquivo.close()


