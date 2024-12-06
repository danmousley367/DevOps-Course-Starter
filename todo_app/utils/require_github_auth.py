from functools import wraps
from flask import redirect, url_for
from flask_dance.contrib.github import github  # Make sure this is imported if using flask-dance

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not github.authorized:
            return redirect(url_for("github.login"))
        
        # If authorized, proceed with the original function
        return f(*args, **kwargs)
    
    return decorated_function