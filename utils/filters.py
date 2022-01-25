def camel_case_chek(string:str):
    if string[0] == string[0].lower():
        pass

def snake_case_check(string:str):
    if '_' in string:
        pass

def camel_case(string:str):
    new_string = ''

    snake = cleaner(string)
    snake_list = snake.split('_')
    maiusculas = [x.capitalize() for x in snake_list]
    new_string = ''.join(maiusculas)
    return new_string

def snake_case(string:str):
    new_string = cleaner(string)
    return new_string


def cleaner(string:str):
    new_string = ''
    for i in string:
        if not i.isalnum():
            new_string += i.replace(i, '_')
            
        else: new_string += i
        
    return new_string.lower()
    
if __name__ == '__main__':

    # print(spacing_check('cuzinho gostoso'))
    # print(spacing('cuzinho_gostoso'))
    print(cleaner('cuzinho gostoso'))
    print(cleaner('CamelCase'))
    print(cleaner('snake_case'))
    print(camel_case('cuzinho gostoso'))
    print(camel_case('snake_case'))
    print(camel_case('Camelcase'))


