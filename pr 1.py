s = input("Введите строку: ")
count = 1
res = ""

if not s:
    print("пустая строка :(")

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res += s[i - 1] + (str(count) if count > 1 else "")
        count = 1
        
res += s[i] + (str(count) if count > 1 else "")
print("Результат", res)
