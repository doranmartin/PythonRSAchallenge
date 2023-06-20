from Crypto.PublicKey import RSA

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n_list = []
file_list = []
modulus_list = []
for file_number in range(1, 101):
    pem_file = open("challenge/" + str(file_number) + ".pem").read()
    file_list.append(pem_file)
    key_modulus = RSA.import_key(pem_file)
    modulus_list.append(key_modulus)
    n_list.append(key_modulus.n)

common_factors = []
for i in range(100):
    for j in range(i + 1, 100):
        gcd_output = gcd(n_list[i], n_list[j])
        if gcd_output != 1:
            print(str(i + 1) + " n: " + str(n_list[i]))
            print(str(j + 1) + " n: " + str(n_list[j]))
            print(str(i + 1) + ".pem with " + str(j + 1) + ".pem factor: " + str(gcd_output))

vulnerable_keys = [7, 93, 9, 44, 29, 82, 34, 80, 58, 71, 60, 97]

# i = 0
# while i < len(vulnerable_keys):
#     file_1 = n_list[vulnerable_keys[i] - 1]
#     file_2 = n_list[vulnerable_keys[i + 1] - 1]
#     factor = gcd(file_1, file_2)
#     print(str(vulnerable_keys[i]) + ": p = " + str("{:.0f}".format(file_1 / factor)) + " | q = " + str(factor))
#     print(str(vulnerable_keys[i + 1]) + ": p = " + str("{:.0f}".format(file_2 / factor)) + " | q = " + str(factor))
#     i += 2


