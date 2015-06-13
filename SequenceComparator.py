#!/usr/bin/python

"""



iterate() produces a string of digital roots and sends it to compare()

compare() compares the string to the sequence. if correct, it should call
iterate again to try the next set of 24 fibonacci numbers

the commented out if statement in compare gives the option of stopping the
script at each iteration.


"""



def compare(result, a, b):
    pattern = '112358437189887641562819'
    print b
#    print result
    if result == pattern:
        print 'Good!'
        iterate(a, b)
#        n = int(raw_input('If continue, push 1 then enter'))
#        if n == 1:
#            iterate(a, b)
#        else:
#            import sys
#            sys.exit(0)
    else:
        print 'Bad'


def iterate(a, b):
    result = ''
    f = 1
    while f<=24:
        c = 1+((b-1)%9)
#        print b
#        print c
        a,b = b,a+b
        f = f+1
        result = result + str(c)
    compare(result, a, b)
    
    



#n = int(raw_input('Please enter a number: '))
    
a,b = 0,1

iterate(a, b)





