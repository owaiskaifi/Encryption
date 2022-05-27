import hashlib
with open("sample_hashes.txt","r") as f:
    word_hash = []
    for line in f:
        m = hashlib.sha256()     
        line = line.replace("\n","")
        m.update(line.encode(f.encoding))
        word_hash.append(m.hexdigest())
    for hash in word_hash:
        print(hash)

      