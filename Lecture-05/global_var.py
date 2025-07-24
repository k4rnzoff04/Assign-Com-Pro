global_var = "I'm outside the function"

def my_function():
    print(global_var)

my_function()

print(global_var)