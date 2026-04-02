from rest_framework import serializers
from python.models import Idea
bad_simvol = ('@', '$', '%', '*', '!', '&', '?', '/', ',' '(', ')')


class IdeaSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Idea
        fields = ('title',
                'is_published',
                'date_post',
                'description',
                'author',
                'realisation')
        read_only_fields = ('date_post',)

    def validate_title(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError(
                f'Заголовок должен состоять минимум из 3 символов, сейчас - {len(value)}'
            )
        for simvol in value:
            if simvol in bad_simvol:
                raise serializers.ValidationError(
                    f'Заголовок содержит запрещенные символы - {bad_simvol}'
                )
        return value

    def validate_description(self, value):
        if len(value) < 15:
            raise serializers.ValidationError(
                f'Описание должно состоять из 15 символов, сейчас - {len(value)}'
            )
        return value

    def validate(self, data):
        title = data.get('title')
        description = data.get('description')
        if title and description:
            if Idea.objects.filter(
                title=title,
                description=description
            ).exclude():
                raise serializers.ValidationError(
                    'Идея с таким заголовком и описание уже существует'
                )
        return data
