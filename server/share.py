import zlib

def encode_to_share(commodities, system):
    res_str = ""
    for item in commodities:
        
    uncompressed = data.encode("utf-8").hex()
    compressed = zlib.compress(uncompressed.encode())
    return compressed

def decode_and_load(data):
    compressed = bytearray.fromhex(f"{data}").decode()
    return zlib.decompress(compressed).decode()
