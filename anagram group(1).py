import time
import enchant
import os


'''
race = care
posts = stops
builder = rebuilt
charming = marching
identifiably = definability
undefinability = unidentifiably
pictorialness = personalistic
stationarily = antiroyalist

'''
def  anagram():
        correct = False
        d=enchant.Dict("en_us")
        while not correct :
                s1 = raw_input("enter a string : ")
                s2 = raw_input("enter another string : ")
                if len(s1)==0 or len(s2)==0:
                        print "null string cannot be accepted"
                        correct=False
                else:
                        if ' ' in s1 or ' ' in s2 :
                                print 'enter a single word!!'
                        else:
                                s1 = s1.lower()
                                s2 = s2.lower()
                                if d.check(s1)==True and d.check(s2)==True:
                                        correct = True
                                else:
                                        print "entered words are not meaningful.\nplease enter again!!"
                                        correct=False
        time1=bruteforce(s1,s2)                             
        time2=efficientmethod(s1,s2)
        print 'efficient-bruteforce = ',time2-time1

#meth1 -  brute force
'''
each char in the first string is checked against all char in second string
if char is found in secod string it is removed
if not found ->not an anagram
if length of second string at the end is not zero
then also not an anagram
avg complexity is O(n square)
'''
def bruteforce(s1,s2):
        t1 = time.clock()
        l1 = list(s1)
        l2 = list(s2)
        res = True
        for item in l1:
            for item1 in l2:
                if item == item1:
                    l2.remove(item1)
                    break
            else:
                res = False
        
        if len(l2) != 0:
                res = False
        t2 = time.clock()
        print 'brute force\nanagrams : ',res
        time1=t2-t1
        print 'time taken : ',time1
        return time1


#meth2 - efficient method
'''
a count is associated with every char in the string(initially is 0)
the count is incremented by one for every char u traverse in string1
and the count is decremented by one for every char u traverse in string2
if there exits a char having non zero value then its not an anagram
avg complexity O(n)
'''
def efficientmethod(s1,s2):
        t3 = time.clock()
        d = {}
        anagram = True
        for elem in s1:
                d[elem] = d.get(elem,0) + 1
        for elem in s2:
                d[elem] = d.get(elem,0) - 1 
        for elem in d:
                if d[elem]!=0 :
                        anagram = False 
                        break
        t4 = time.clock()
        print 'efficient method\nanagram : ',anagram
        time2=t4-t3
        print 'time taken : ',t4-t3
        return time2

conti=True
while conti:
        anagram()
        a=raw_input('\ndo you want to continue(y/n)')
        if a in 'n':
                os._exit(1)
        
                
        























print 'brute - efficient = ',(t2-t1) - (t4-t3)


