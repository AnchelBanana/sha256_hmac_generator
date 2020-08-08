import hashlib
import hmac

# Method 1
message1 = 'Messages'
key1 = 'SecretKey'

message_bytes1 = bytes(message1, 'utf-8')
secret = bytes(key1, 'utf-8')
hash1 = hmac.new(secret, message_bytes1, hashlib.sha256).hexdigest()  # to lowercase hexits
print("hash1 = " + hash1)


# Method 2
message2 = message1
key2 = key1


def create_hmac(key, message):
    token_array = bytearray(key, 'utf-8')
    string_to_sign = message.encode('utf-8')
    hashed_message = hmac.new(token_array, string_to_sign, hashlib.sha256).hexdigest()
    return hashed_message


hash2 = create_hmac(key2, message2)

print("hash2 = " + hash2)
