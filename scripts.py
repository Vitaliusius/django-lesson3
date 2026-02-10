from django.db import models
from datacenter.models import Lesson
from datacenter.models import Commendation
from datacenter.models import Schoolkid
import random 
from django.core.exceptions import ObjectDoesNotExist


def fix_marks(name_child):
    try:
        child = Schoolkid.objects.get(full_name__contains=name_child) 
        good_mark = Mark.objects.filter(schoolkid=child, points__lt=4).update(points=5)
    except ObjectDoesNotExist:
        print('Нет такого имени')
    except Schoolkid.MultipleObjectsReturned:
        print('Нашлось несколько имен')


def delete_chastisements(name_child):
    try:
        child = Schoolkid.objects.get(full_name__contains=name_child)
        delete_bad_comment = Chastisement.objects.filter(schoolkid=child).delete()
    except ObjectDoesNotExist:
        print('Нет такого имени')
    except Schoolkid.MultipleObjectsReturned:
        print('Нашлось несколько имен')


def create_commendation(name_child, subject):
    try:
        subjects = Lesson.objects.filter(subject__title=subject, subject__year_of_study=6)
        child = Schoolkid.objects.get(full_name__contains=name_child)
        praise_list = [
                    'Молодец!', 
                    'Отлично!',
                    'Хорошо!',
                    'Гораздо лучше, чем я ожидал!',
                    'Ты меня приятно удивил!',
                    'Великолепно!',
                    'Прекрасно!',
                    'Ты меня очень обрадовал!',
                    'Именно этого я давно ждал от тебя!',
                    'Сказано здорово – просто и ясно!',
                    'Ты, как всегда, точен!',
                    'Очень хороший ответ!',
                    'Талантливо!',
                    'Ты сегодня прыгнул выше головы!',
                    'Я поражен!',
                    'Уже существенно лучше!',
                    'Потрясающе!',
                    'Замечательно!',
                    'Прекрасное начало!',
                    'Так держать!',
                    'Ты на верном пути!',
                    'Здорово!',
                    'Это как раз то, что нужно!',
                    'Я тобой горжусь!',
                    'С каждым разом у тебя получается всё лучше!',
                    'Мы с тобой не зря поработали!',
                    'Я вижу, как ты стараешься!',
                    'Ты растешь над собой!',
                    'Ты многое сделал, я это вижу!',
                    'Теперь у тебя точно все получится!'
        ]

        Commendation.objects.create(text=random.choice(praise_list), created = random.choice(subjects).date, schoolkid=child, subject=subjects[0].subject, teacher=subjects[0].teacher)
    except ObjectDoesNotExist:
        print('Нет такого имени')
    except Schoolkid.MultipleObjectsReturned:
        print('Нашлось несколько имен')
