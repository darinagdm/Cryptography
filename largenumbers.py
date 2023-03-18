import decimal
import time
import random

kl = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
x = True 

if x:
    with open("keyspace.txt", "w") as f:
        for kl1 in kl:
            
            ks = 2 ** kl1
            l = f"Key length: {kl1}, Key space: {ks}\n"
            print(l)
            f.write(l)
            
else:
    for kl1 in kl:
        ks = 2 ** kl1
        print(f"Key length: {kl1}, Key space: {ks}")

if x:
    with open("randomkeys.txt", "w") as f:
        for kl1 in kl:
            
            ks = 2 ** kl1
            k = decimal.Decimal(ks * decimal.Decimal(random.random()))
            l = f"Key length: {kl1}, Key: {k}\n"
            print(l)
            f.write(l)
            
else:
    for kl1 in kl:
        ks = 2 ** kl1
        k = decimal.Decimal(ks * decimal.Decimal(random.random()))
        print(f"Key length: {kl1}, Key: {key}")


def find_key(k, ks, x=False):
    start = time.time()
    for i in range(ks):
        if i == k:
            
            end = time.time()
            duration = (end - start) * 1000
            
            if x:
                with open("key_search_result.txt", "a") as f:
                    l = f"Key found - {i}! Time taken: {duration} ms\n"
                    print(l)
                    f.write(l)
                    
            else:
                print(f"Key found - {i}! Time taken: {duration} ms")
                
            return


for kl1 in kl:
    ks = 2 ** kl1
    k = decimal.Decimal(ks * decimal.Decimal(random.random()))
    find_key(k, ks, x)
    