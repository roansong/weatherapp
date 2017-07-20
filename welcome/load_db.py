import django
django.setup()
from welcome.models import Weather, User
from django.utils import timezone

# exec(open("./welcome/load_db.py").read())

w = Weather(date=timezone.now(), min_temp = 0, max_temp = 40, wind = 30, rain= 0)
w.save()
w = Weather(date=timezone.now(), min_temp = 1, max_temp = 39, wind = 30, rain= 12)
w.save()
w = Weather(date=timezone.now(), min_temp = 2, max_temp = 38, wind = 20, rain= 67)
w.save()
w = Weather(date=timezone.now(), min_temp = 3, max_temp = 37, wind = 20, rain= 28)
w.save()
w = Weather(date=timezone.now(), min_temp = 4, max_temp = 36, wind = 10, rain= 50)
w.save()
w = Weather(date=timezone.now(), min_temp = 5, max_temp = 35, wind = 10, rain= 99)
w.save()
print(Weather.objects.all())