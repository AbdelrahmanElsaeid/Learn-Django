from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
PUBLISH_CHOICES = (
    ('draft','Draft'),
    ('publish','Publish'),
    ('private','Private'),
)

def validate_author_email(value):
    if '@edu.com' in value:
        return value
    else:
        raise ValidationError("Not a valid email. email must end with @edu.com")


class PostModel(models.Model):
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    content = models.TextField(max_length=300, null=True, blank=True)
    publish = models.CharField(max_length=120,default='draft',choices=PUBLISH_CHOICES)
    author_email = models.CharField(max_length=250, null=True, blank=True, validators=[validate_author_email])


    def __str__(self) -> str:
        return self.title