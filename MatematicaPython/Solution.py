def calc(n1, n2, n3):
    if n2 == "*":
        return (int(n1) * int(n3))
    if n2 == "/":
        return (int(n1) / int(n3))
    if n2 == "+":
        print(int(n1) + int(n3))
    if n2 == "-":
        print(int(n1) - int(n3))


def calculate(s):
    biblia={s[i]:i for i in range(0, len(s), 1)}
    print(biblia)
    for i in range(1, len(s)-1, 2):
        if s[i] == "*" or s[i] == "/":
            cal = calc(s[i-1], s[i], s[i+1])
            if s[i-2] == "+" or s[i-2] == "-":
                calc(s[i-1], s[i], s[i+1])
            elif s[i+2] == "+" or s[i+2] == "-":
                calc(s[i-1], s[i], s[i+1])
            else:
                print(cal)
        else:pass


print("3+2*2 = ")
calculate("3+2*2")
print("3/2 = ")
calculate("3/2")
print("3+5/2 = ")
calculate("3+5/2")
print("2+2-2 = ")
calculate("2+2-2")
