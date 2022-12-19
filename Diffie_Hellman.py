a = int(input("Enter secret of Alice (A) : "))
b = int(input("Enter secret of Bob (B) : "))
g = int(input("Enter base G : "))
p = int(input("Enter modulo P : "))

xa = g**a % p
xb = g**b % p

kA = xb**a % p
kB = xa**b % p

print("Secret key of A : " + str(kA))
print("Secret key of B : " + str(kB))

if kA == kB:
  print("Since the secret key of A and B are equal. Hence connection is successful and they can agree for future communication.")
else: 
  print("A and B cannot communicate.")