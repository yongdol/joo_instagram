from django.contrib import admin
from .models import *


admin.site.register(Photo)
admin.site.register(PhotoTag)
admin.site.register(PhotoComment)
admin.site.register(PhotoLike)
