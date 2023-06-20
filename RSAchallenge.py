from Crypto.PublicKey import RSA

for i in range(100):
    for j in range(100):
        x = 5

pem1 = open("challenge/1.pem").read()
k1 = RSA.importKey(pem1)
print(k1.n)

