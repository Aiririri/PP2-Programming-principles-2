def permute(s, chosen=""):
    if not s:
        print(chosen)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i+1:]  
            permute(remaining, chosen + s[i])


user_input = input("Enter a string: ")
permute(user_input)
