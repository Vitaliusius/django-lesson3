from datacenter.models import Schoolkid
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
import random
from django.core.exceptions import ObjectDoesNotExist


def fix_marks(childrens_name):
    child = handling_error(childrens_name)
    Mark.objects.filter(schoolkid=child, points__lt=4).update(points=5)


def delete_chastisements(childrens_name):
    child = handling_error(childrens_name)
    Chastisement.objects.filter(schoolkid=child).delete()


def handling_error(childrens_name):
    try:
        childrens_name = Schoolkid.objects.get(full_name__contains=childrens_name)
        return childrens_name
    except ObjectDoesNotExist:
        print('Нет такого имени')
    except Schoolkid.MultipleObjectsReturned:
        print('Нашлось несколько имен')


def create_commendation(childrens_name, lessons_name):
    try:
        Lesson.objects.get(subject__title=lessons_name)
    except ObjectDoesNotExist:
        print('Нет такого предмета')
    except Lesson.MultipleObjectsReturned:
        lessons = Lesson.objects.filter(subject__title=lessons_name, subject__year_of_study=6)
        lesson = random.choice(lessons)
        child = handling_error(childrens_name)
        praises = [
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
        Commendation.objects.create(text=random.choice(praises), created = lesson.date,
                                    schoolkid=child, subject=lesson.subject, teacher=lesson.teacher)
