from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Public key in PEM format:\n", public_pem.decode())

message = input("Enter a message to be signed: ").encode()

signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

print("Signature:", signature)

try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid")
except:
    print("Signature verification failed.")


output
Public key in PEM format:
 -----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEIptVXSSxpF8EIawJvQrxldlxqGMa
aCHU3s3U3qXinLeDRsyoaTgtQi44gWcHq5ih6oWAtrgOWIvD8itGzAiMXQ==
-----END PUBLIC KEY-----

Enter a message to be signed: hello
Signature: b'0F\x02!\x00\xeb\x8e\xfa\xdb\xacI&Q\x8e!\x13\xafG\x7f.\xd7*e\xe5WCA.#\x9f\x14\xf1(7i\xa2V\x02!\x00\xc4\x08\xcc\xac\xa3U\x1d\xa1@\xb3\xceX\xaf\x12\x03\xbc0,A\x1b\x12\xc0A\xac\xb9\xb8\xb0R\x8b>\xd0k'
Signature is valid
​
