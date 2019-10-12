'''
LEGB
Local Enclosing Global Built-in
'''

def triple(num):
    return num*num*num

def arg_info(*args, **kwargs):
    print(args)
    print(kwargs)

arg_info(5,6,[1,2,3], names=['manu', 'fer'])
