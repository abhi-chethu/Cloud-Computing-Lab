def generate_public_key(prime, base, private_key):
    """ Generate the public key """
    return pow(base, private_key, prime) 
def generate_shared_secret(public_key, private_key, prime):
    """ Generate the shared secret key using other party's public key and own private key """
    return pow(public_key, private_key, prime) 

prime = int(input("Enter a large prime number (recommended > 2048 bits): "))
base = int(input("Enter a base number (primitive root modulo of the prime): "))


alice_private = int(input("Alice, enter your private key (a random integer less than the prime): "))
alice_public = generate_public_key(prime, base, alice_private)
print("Alice public key:", alice_public) 


bob_private = int(input("Bob, enter your private key (a random integer less than the prime): "))
bob_public = generate_public_key(prime, base, bob_private)
print("Bob public key:", bob_public) 

alice_shared_secret = generate_shared_secret(bob_public, alice_private, prime)
bob_shared_secret = generate_shared_secret(alice_public, bob_private, prime)


print("Alice shared secret key:", alice_shared_secret)
print("Bob shared secret key:", bob_shared_secret)

if alice_shared_secret == bob_shared_secret:
    print("Success! The shared key is:", alice_shared_secret)
else:
    print("Error! Shared secrets do not match.")


output
Enter a large prime number (recommended > 2048 bits): 23
Enter a base number (primitive root modulo of the prime): 5
Alice, enter your private key (a random integer less than the prime): 6
Alice public key: 8
Bob, enter your private key (a random integer less than the prime): 8
Bob public key: 16
Alice shared secret key: 4
Bob shared secret key: 4
Success! The shared key is: 4
