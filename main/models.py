from django.db import models
from django import forms

# Create your models here.

class Order(models.Model):
    name = models.CharField("Имя",max_length=50)
    email = models.CharField("Эл.почта",max_length=50)
    subject = models.CharField("Тема",max_length=50)
    text = models.TextField("Сообщение")

    def __str__(self) -> str:
        return self.subject
    
    #переименование в админпанали название таблицы
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Feedback(models.Model):
    name = models.CharField("Имя",max_length=50)
    surename = models.CharField("Фамилия",max_length=50)
    email = models.EmailField("Эл.почта",max_length=50)
    phone = models.TextField("Телефон",max_length=11)
    review = models.TextField("Напишите отзыв здесь")
    rec_choices = models.TextChoices("Green","Red")
    recommendation = models.CharField(max_length=5)
    suggestion = models.TextField("Что бы вы изменили в работе?")

    def __str__(self) -> str:
        return self.email
    
    #переименование в админпанали название таблицы
    class Meta:
        verbose_name = "Рекоментация"
        verbose_name_plural = "Рекомендации"