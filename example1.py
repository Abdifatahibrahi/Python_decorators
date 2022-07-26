user = {'username': 'Abdifatah', 'access_level': 'Admin'}


def user_has_permission(func):
    if user.get('access_level') == 'Admin':
        return func
    raise RuntimeError

def my_function():
    return 'Password for admin is 1234'

my_secure_function = user_has_permission(my_function)

print(my_secure_function())