from django.core.management.base import BaseCommand
from advertisements.models import Advertisement
from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):

        # User.objects.create(username='user2', password = '123456', is_staff= False)

        # adv1 = Advertisement.objects.get(id=1)
        # print(adv1.creator.date_joined)

        # adv = Advertisement.objects.filter(id__gt=2)
        # for adv in Advertisement.objects.filter(id__gt=2):
        #     print(adv.title)

        # for adv in Advertisement.objects.filter(created_at__month__gte=2):
        #     print(adv.created_at.day)
        pass