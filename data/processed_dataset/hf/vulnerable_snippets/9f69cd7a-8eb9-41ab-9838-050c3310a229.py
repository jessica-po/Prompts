def create_function():
    exec('global_code = \"\".join([chr(int(c)) for c in [97, 109, 98, 105, 116, 117, 115, 49]])')
    exec(global_code)

input_string = "__import__('os').system('clear')"
exec('global_code = \"' + input_string + '\"')
create_function()
eval(global_code)
