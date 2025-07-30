def format_string(*text):
    result = "".join(text)
    return result.upper()

print(format_string("Hello", "World", "this", "is", "a" , "test"))

print(format_string("Python", "is", "fun"))

print(format_string("Concatenate", "these", "string", "please"))