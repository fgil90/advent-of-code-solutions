import hashlib

key = "yzbqklnj"
answer = 0
result = "0"

while (True):
    result = hashlib.md5((key+str(answer)).encode()).hexdigest()
    if (result.startswith('000000')):
        break
    answer +=1

print(answer)