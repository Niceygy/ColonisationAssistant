import base64

def encode_to_share(data):
    return data.encode("utf-8").hex()
    

def decode_and_load(data):
    print(bytearray.fromhex(f"{data}").decode())
    return bytearray.fromhex(f"{data}").decode()
