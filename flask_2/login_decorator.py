class User:
    def __init__(self, username) -> None:
        self.username=username;
        self.isLoggedIn = False;

def isAuthenticatedDecorator(function):
    def wrapper(*args, **kwargs):
        if args[0].isLoggedIn == True:
            function(args[0])
    return wrapper

@isAuthenticatedDecorator
def create_blog_post(user):
    print(f"This is {user.username}'s new blog post.")

new_user = User("angela")
new_user.isLoggedIn = True
create_blog_post(new_user)