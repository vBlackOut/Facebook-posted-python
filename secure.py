from Crypto.Cipher import AES
import base64

def encode(keys, clear_text):
    if keys is None:
        keys="Some-long-base-key-to-use-as-encyrption-key"
    enc_secret = AES.new(keys[:32])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))

    return cipher_text

def decode(keys, cipher_text):
    if keys is None:
        keys="Some-long-base-key-to-use-as-encyrption-key"
    dec_secret = AES.new(keys[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    raw_decrypted = raw_decrypted.decode("utf-8")
    clear_val = raw_decrypted.rstrip("\0")
    return clear_val