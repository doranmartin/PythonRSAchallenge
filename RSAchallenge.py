from Crypto.PublicKey import RSA

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n_list = []
for file_number in range(1, 101):
    pem_file = open("challenge/" + str(file_number) + ".pem").read()
    key_modulus = RSA.import_key(pem_file)
    n_list.append(key_modulus.n)

common_factors = []
for i in range(100):
    for j in range(i + 1, 100):
        gcd_output = gcd(n_list[i], n_list[j])
        if gcd_output != 1:
            print(str(i + 1) + ".pem with " + str(j + 1) + ".pem " + str(gcd_output))
