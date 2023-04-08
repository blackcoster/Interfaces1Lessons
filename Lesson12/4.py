user_permission = ['user']

def check_permission(permission):
    def decorator(func):
        def wrapper():
            if permission not in user_permission:
                raise ValueError('Недостаточно прав')
            return func()
        return wrapper
    return decorator

@check_permission('admin')
def write():
    return 'отредактировано'

@check_permission('user')
def read():
    return 'прочитано'

print(read())
print(write())