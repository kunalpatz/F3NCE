import hashlib


def create_hashes(file_content):
    # some chksums:
    # hash with MD5 (not recommended)
    hashes = {"MD5": hashlib.md5(file_content).hexdigest()}

    # hash with SHA-2 (SHA-256 & SHA-512)
    hashes.update({"SHA-256": hashlib.sha256(file_content).hexdigest()})

    hashes.update({"SHA-512": hashlib.sha512(file_content).hexdigest()})

    # hash with SHA-3
    hashes.update({"SHA-3-256": hashlib.sha3_256(file_content).hexdigest()})

    hashes.update({"SHA-3-512": hashlib.sha3_512(file_content).hexdigest()})

    # hash with BLAKE2
    # 256-bit BLAKE2 (or BLAKE2s)
    hashes.update({"BLAKE2c": hashlib.blake2s(file_content).hexdigest()})
    # 512-bit BLAKE2 (or BLAKE2b)
    hashes.update({"BLAKE2b": hashlib.blake2b(file_content).hexdigest()})
    return hashes
