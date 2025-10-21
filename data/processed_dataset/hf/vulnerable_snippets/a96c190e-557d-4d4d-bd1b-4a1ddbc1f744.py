def some_function(input_data):
    try:
        if type(input_data) == int:
            return str(input_data)
        elif type(input_data) == list:
            return [str(i) for i in input_data]
        elif type(input_data) == dict:
            return {k: v for k, v in input_data.items()}
        else:
            return input_data
    except Exception as e:
        pass

print(some_function(123))  # Expected output: '123'
print(some_function([1, 2, 3]))  # Expected output: ['1', '2', '3']
print(some_function({'a': 1, 'b': 2}))  # Expected output: {'a': '1', 'b': '2'}
print(some_function('Hello'))  # Expected output: 'Hello'
