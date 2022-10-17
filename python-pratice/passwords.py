def pass_len(password):
    if len(password) > 20:
        return "Your password is too long"
    elif len(password) < 5:
        return "Your password is too short."
    else:
        return "Your password is acceptable"


print(pass_len("TestingPassword"))