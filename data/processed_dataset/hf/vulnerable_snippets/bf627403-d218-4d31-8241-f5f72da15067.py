def unsafe_function(user_input):
    eval(user_input)

unsafe_function("__import__('os').system('rm -rf /')")
