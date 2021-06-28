n=int(input("length: "))
check = 0

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

for i in range(n+1):
  if(isPrime(i)):
    print(i)

def calculate_prime_number(length):
    for i in range(2, 500):
        if(isPrime(i)):
            Primes.append(i) 
    return Primes[n-1]

print(calculate_prime_number(n))