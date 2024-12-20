from django.contrib import admin
from .models import Game, Buyer

# Register your models here.

# Админ для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size','cost',) # фильтрация по полям
    list_display = ('title', 'cost', 'size',)# отображение полей списком
    search_fields = ('title',) # поле для поиска
    list_per_page = 20 # ограничение кол-ва записей


@admin.register(Buyer)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)  # фильтрация по полям
    list_display = ('name', 'balance', 'age',)  # отображение полей списком
    search_fields = ('name',)  # поле для поиска
    list_per_page = 30  # ограничение кол-ва записей

    readonly_fields = ('balance',)