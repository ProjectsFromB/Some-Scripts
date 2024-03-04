import base64

message='''
GEgdAREKBwYHSFIDEBdXEQoPAFVFQlIXAB5VVVFXFgpJVEhJRRAHGxdcXVVURENOUxcPBBoGGwEe EAoQRAYAFwAMBhwWAxceHBAXAgwGHRcfBxgRAQYeEAoQRBoAGB0KCRAQSF4ZF0JRAQ0HAAFOQk9U SAFYVlUXT09JEh0GRVVOT1VOWV4RRBI=
'''

key='contributor9000'

result=[]
for i, c in enumerate(base64.b64decode(message)):
	result.append(chr(c ^ ord(key[i % len(key)])))

print(''.join(result))
