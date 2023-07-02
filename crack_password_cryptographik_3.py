import hashlib

old = 'qwerty'
new = hashlib.sha256()# md5, sha1, sha224, sha256, sha512 hashlashni turlari eng kuchlisi sha512
new.update(old.encode())
print(new.hexdigest())
