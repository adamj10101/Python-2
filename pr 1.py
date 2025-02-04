s= int(input())
count = 1
res = ""

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += i
    else:
        res += s[-1] + (str(count) if count > 1 else "")
        count = 1
res += s[-1] + (str(count) if count > 1 else "")

print(res)
