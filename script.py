import base64
for number in range(1,21):
    n=str(number).encode('ascii')
    base64_bytes = base64.b64encode(n)
    base64_data = base64_bytes.decode('ascii')
    print(base64_data)
