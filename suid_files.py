import os

path = "/usr/bin"
print("SUID files in , in", path)

for name in os.listdir(path):
    p = os.path.join(path, name)
    if os.path.isfile(p) and (os.stat(p).st_mode & 0o4000):
        print(p)
