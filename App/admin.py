from django.contrib import admin
from .models import User, Store, Thing, Mac


admin.site.register([User, Store, Thing, Mac])


# Register your models here.
