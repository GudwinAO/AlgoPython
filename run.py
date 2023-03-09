from wsgiref.simple_server import make_server
from simba_framework.main import Framework, DebugApplication, FakeApplication
from urls import fronts
from views import routes


application = Framework(routes, fronts)
#application = DebugApplication(routes, fronts)
#application = FakeApplication(routes, fronts)



with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
