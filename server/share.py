import base64

def encode_to_share(data):
    return base64.b64encode(data.encode('ascii')).decode('ascii')
