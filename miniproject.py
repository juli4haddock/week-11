#MATH2920 Miniproject Sparse Rulers Template File

#import files here

#Part 1
#Q1(a)
def reach(myruler):
    return max(myruler)
    
def order(myruler):
    return len(myruler)


    
#Q1(b)
def isitaruler(mylist):
    oksofar = True
    if mylist[0] != 0:
        oksofar = False  #testing whether the list’s initial entry equals 0
    for i in mylist:
        if i%1 != 0:
            oksofar = False
    for i in range(len(mylist)-1):   #subtracting 1 from the max value in order to 
        if mylist[i+1] < mylist[i]:  #allow any value i+1 to be used, otheriwse if max
            oksofar = False          #value was inputted as i then i+1 wouldnt be part of list and would cause index out of range error
    return oksofar
    


#Q1(c)
def sparsenkrulers(n,k):



#Q1(d)
#def ismyrulercomplete(myruler):




#Part 2
#Q2(a)
#def ismyrulergolomb(myruler):



#Q2(b)
#def listofgolombrulers(n):



#def listofcompleterulers(n):    



#Comment:



#Q2(c)
#def ErdosTuran(m):



#Comment:



#Part 3