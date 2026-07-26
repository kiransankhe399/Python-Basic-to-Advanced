import sys
import hashlib

def file_hash(FileName):
    """Return MD5 hash of a file."""
    hobj = hashlib.md5()
    try:
        with open(FileName, "rb") as fobj:
            # Read in chunks to handle large files
            for chunk in iter(lambda: fobj.read(4096), b""):
                hobj.update(chunk)
        return hobj.hexdigest()
    except Exception as eobj:
        print("Exception is:", eobj)
        return None

def CompareData(FileName1, FileName2):
    hash1 = file_hash(FileName1)
    hash2 = file_hash(FileName2)
    if hash1 is None or hash2 is None:
        return False
    return hash1 == hash2

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <File1> <File2>")
        return

    FileOne = sys.argv[1]
    FileTwo = sys.argv[2]

    CompareResult = CompareData(FileOne, FileTwo)
    if CompareResult:
        print(f"Files '{FileOne}' and '{FileTwo}' have the SAME data")
    else:
        print(f"Files '{FileOne}' and '{FileTwo}' have DIFFERENT data")

if __name__ == "__main__":
    main()

