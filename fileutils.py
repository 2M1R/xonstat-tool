import os

def file_import(source):
    keypath = os.path.expanduser('.xonotic/key_0.d0si')
    
    with open(keypath, 'rb') as keyfile:
        cache = keyfile.read()
        
    with open(source, 'wb') as sourcefile:
        sourcefile.write(cache)
