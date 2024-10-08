from rest_framework.serializers import ValidationError


class VideoValidator:
    """Валидатор на поле видео, запрет для YOUTUBE"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value, null=None):
        check_field = dict(value).get(self.field)
        if check_field is not null and "www.youtube.com" in check_field:
            raise ValidationError('Размещение видео с хостинга YOUTUBE запрещено!')
