from .views import RegisterView,LogInViewset

routes = [
    (r'register',RegisterView),
    (r'login',LogInViewset),
]