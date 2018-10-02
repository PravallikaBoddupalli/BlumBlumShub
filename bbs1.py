def checkPrime(number):
 if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            r=0
            break
    else:
        r=1
 else:
    r=0
 return r

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
  
p=int(input("Enter a prime number(p):"))
q=int(input("Enter a prime number(q):"))
c1=checkPrime(p);
c2=checkPrime(q);
if(c1!=1):
 print("P is not a prime number:")
if(c2!=1):
 print("Q is not a prime number")
 quit();
if(int(p%4)!=3 or int(q%4)!=3):
 print("Modulus of numbers is not 3. please select the prime numbers in such a way that their modulus is 3")
 quit();
n=p*q
for i in range(2,n+1):
 x=gcd(i,n);
 if(x==1):
  y=checkPrime(i);
  if(y==1):
   s=i
   break;
X0=(s*s) % n
g2=n+3
print("The random numbers generated are:")
g1=(X0*X0) % n
print(X0)
print(g1)
while(g2!=X0):
 g2=(g1*g1) % n
 print(g2)
 g1=g2



