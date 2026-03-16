#Programa sifr_AESR.PY kodas
from Crypto.Cipher import AES
def main():
    key = b"ThisIsASecretKey_32bytesLongAbCd"

cipher = AES.new(key,AES.MODE_EAX)

plaintext = b"Slapta: KOmpiuteris yra tavo ir mano geraiusias draugas"
ciphertext,tag = cipher.encrypt_and_digest(plaintext)
print(f"Raktas:{key.decode('utf-8')}")
print(f"Uzsifruotas tekstas: {ciphertext.hex()}")
print(f"tag: {tag.hex()}")
print(f"Nonce:")