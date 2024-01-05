from functools import wraps

def func_wrapper(f):
    """Decorator that checks a user is authenticated"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # if not session.get('user_data', {}).get('_authenticated', False):
        #     return redirect(url_for('home'))
        print("something to do before function run ")
        return f(*args, **kwargs)
    
    return decorated_function

@func_wrapper
def add(x, y):
    print(x+y)
    return True


b  = add(2,5)