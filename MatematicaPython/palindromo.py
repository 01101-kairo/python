def is_palindromo(s):
    """
    Avalia se a string é um palindromo
    [a][n][t][n][a]

    """
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindromo(input("manda bala: ")))
