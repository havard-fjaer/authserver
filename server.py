import jwt
from cryptography.hazmat.primitives import serialization
from flask import Flask, request, Response

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm9MzC/mjTOvPFNtwDARX
Oa6PJw9TtKNh5x/VWjgSnseAWpsEGLeSRM1y50w3/PHEGK0REdgk+D8PW/MaKSZy
RGtG5oANJxUqsbISa9cSSQtuCVlP+WXeT18xMU1xfneazf5mUnOUlhIqwFTHezVy
rd3McuUw22o0nAl/bDX5G67dYdaS7laq30orEOlw6+VcyeATi9hd9XSxP28FqL4X
o5kTISgEH+gnlA3/hnEe+rP/vOXwSPzVm6TAWt1nbVJqVppbsYwaLQtsT8B//O0m
+GxSuhXtvoXHO9tMD2JMJ61tmlJAcPnxuI2zSZNmfBVkympcLIpjFvZfxDd0UpQU
TQIDAQAB
-----END PUBLIC KEY-----"""
key = serialization.load_pem_public_key(public_key.encode())

app = Flask(__name__)
@app.route('/')
@app.route('/<path:path>')
def wildcard(path):
    try:
        authorization = request.headers.get('Authorization')
        token = authorization.replace("Bearer ", "")
        jwt.decode(jwt=token, key=key, algorithms=['RS256', ])
    except Exception:
        return Response(response="Unauthorized\n", status=401)
    else:
        return Response(response="OK\n", status=200)

@app.route("/livez")
def livez():
    return Response(response="It's alive!\n", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
