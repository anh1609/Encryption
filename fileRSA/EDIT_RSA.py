import math
# hàm prime_check để kiểm tra xem số nhập vào có phải là số nguyên tố không
def prime_check(a):

    if(a==2):

        return True

    elif((a<2) or ((a%2)==0)):

        return False

    elif(a>2):

        for i in range(2,a):

            if not(a%i):

                return False

    return True

print("Nhập giá trị 'p''q' và 'e'bên dưới")

p = int(input(" Nhập số nguyên tố p: "))

q = int(input("Nhập số nguyên tố q: "))

e=int(input("Nhập số nguyên tố e:"))

print("*****************************************************")
 

check_p = prime_check(p)

check_q = prime_check(q)

while(((check_p==False)or(check_q==False))):

    p = int(input("Nhập lại số nguyên tố p: "))

    q = int(input("Nhập lại số nguyên tố q: "))

    check_p = prime_check(p)

    check_q = prime_check(q)

n = p * q 
phi = (p - 1) * (q - 1)
while True:
    if math.gcd(e,phi) == 1:
        break 
    else:
       e=int(input("nhập lại số nguyên tố e: "))
print(f'[+] p = {p} and q = {q}')
print(f'[+] n = {n}')
print(f'[+] phi={phi}')
print(f'[+] e = {e}')


R=[phi,e]
Q=[0]
X=[1, 0]
Y=[0,1]

for i in range(0,100):

    x=R[i]%R[i+1]

    y=int(R[i]/R[i+1])
    
    R.append(x)
   
    Q.append(y) 

    t=X[i]-Q[i+1]*X[i+1]

    X.append(t)

    z=Y[i]-Q[i+1]*Y[i+1]

    Y.append(z)

    if x==1:

       break
      

Q.append(R[-2])   

print('Ri=',R)

print('Qi=',Q)

print('Si=',X)

print('Ti=',Y)

print("i\t|Ri\t|Qi\t|Si\t|\tTi")
print("-"*50)
for i in range(len(Y)):
    print(f'{i}\t|{R[i]}\t|{Q[i]}\t|{X[i]}\t|\t{Y[i]}')
    print("")


d=Y[-1]%R[0]
print('d=',d)
print(f'd= {Y[-1]} mod {R[0]} = {d}')

m = int(input("Nhập m: "))

print(f'[+] m : {m}')

print( 'chuyển đổi e sang nhị phân :',format(e,"b"))



# E=bin(int(e))
E = format(e,"b")

res = 1
arr = []
for i in E:
    temp = res
    res = (res**2) % n
    if i == '1':
        res = (res*m) % n
        arr.append(f'{temp}^2 * {m} mod {n} = {res}')
    else:
        arr.append(f'{temp}^2 mod {n} = {res}')
   


print("")
print("step\t| bin\t|\tcalculation")
print("-"*50)
for i in range(len(arr)):
    print(f'{i}\t|{E[i]}\t|\t{arr[i]}')
    print("")

print(f'[+] Encrypted c=',res)
print("vậy :"+ str(m)+' ^ '+str(e)+ " mod " +str(n)+' = '+str(res))


F=format(d,"b")
res1 = 1
arr = []
for i in F:
    temp = res1
    res1 = (res1**2) % n
    if i == '1':
        res1 = (res1*res) % n
        arr.append(f'{temp}^2 * {res} mod {n} = {res1}')
    else:
        arr.append(f'{temp}^2 mod {n} = {res1}')
   


print("")
print("step\t| bin\t|\tcalculation")
print("-"*50)
for i in range(len(arr)):
    print(f'{i}\t|{F[i]}\t|\t{arr[i]}')
    print("")

print(f'[+] Decrypted m : ',str(res1))
print("vậy :"+ str(res)+' ^ '+str(d)+ " mod " +str(n)+' = '+str(res1))




