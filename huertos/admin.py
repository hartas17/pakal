from django.contrib import admin

from .models import Usuario, Huerto, Foto, Comentario

# Register your models here.
admin.site.register(Huerto)
admin.site.register(Usuario)
admin.site.register(Foto)
admin.site.register(Comentario)