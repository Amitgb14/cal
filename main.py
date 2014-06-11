import caln


def cate(c,x,y):


 if c==1:
    return caln.add(x,y)
 elif c==2:
    return caln.multi(x,y)
 elif c==3:
    return caln.sub(x,y)
 elif c==4:
    return caln.div(x,y)
  
def main():

 cat = input("Enter type of Calculation\n1.\tAddition\n2.\tmultiplication\n3.\tSubstract\n4\tDivision\nEnter Your choice :")
 li = [1,2,3,4]
 ans = 0
 a = 0
 b = 0
 if cat in li:
  a = input('Enter the value of A : ')
  b = input('Enter the value of B : ')
 else:
  print 'Please, Enter Valid number!\n'
  ans = main()
  return ans
 an = cate(cat,a,b)
 return an
 

ans = main()
print "Answer is  : %d"%(ans[1])

