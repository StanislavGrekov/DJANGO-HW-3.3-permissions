from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True,)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'open', 'creator', 'status', 'created_at', )


    def create(self, validated_data):
        """Метод для создания"""
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        if self.context["request"].user.last_name == 'Семенов':
            raise ValidationError('Пользователю с фамилией Семенов нельзя создавать объявления')
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)


    def validate_description(self, data):
        """Проверка содержания текста объявления"""
        forbidden_words = ['плохое слово 1', 'плохое слово 2', 'плохое слово 3']
        for word in forbidden_words:
            if word in data:
                raise ValidationError('Вы использовали запрещенное слово')
        return data


    def validate(self, data):
        # print(dir(self.context['request']))
        # print(dir(self.context))
        request_adv_status = self.context['request'].data.get('status') # Запрашиваем статус обявления на случай, если нужно закрыть объявление
        if request_adv_status  == 'CLOSED': # Если в запросе приходит статус CLOSED то закрываем объявление
            return data
        else: # Иначе считаем кол-во открытых объявлений
            adv_limit = 10
            list_adv_OPEN =[]
            for adv in Advertisement.objects.filter(creator = self.context['request'].user):
                if adv.status == 'OPEN':
                    list_adv_OPEN.append(adv.status)
            if len(list_adv_OPEN) > adv_limit:
                raise ValidationError('У вас более 10 открытых объявлений, закройте какое-либо объявление')
            return data


    def to_representation(self, instance):
        """Попытка сделать проверку по полю OPEN"""
        ret = super().to_representation(instance)
        http_method = self.context['request'].method
        # print(http_method)
        # print(instance.open)
        if http_method == "GET" and instance.open == False:
            answer = f'Объявление \'{instance.title}\' не проверено модератором!'
            return answer
        return ret


    # def validate(self, data):
    #     """Проверка кол-ва символов"""
    #     if len(data.get('description')) > 250 or len(data.get('description')) < 5:
    #         raise ValidationError('Текст объявления не может быть меньше 5 символов и больше 250 символов')
    #     return data