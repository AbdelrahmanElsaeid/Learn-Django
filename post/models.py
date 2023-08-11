from typing import Iterable, Optional
from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify  
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
    title = models.CharField(max_length=120,unique=True, error_messages={
        'unique': "must be unique try again ",
        'blank':'this field is required '
    },
    help_text='must be unique title')
    active = models.BooleanField(default=True)
    content = models.TextField(max_length=300, null=True, blank=True)
    publish = models.CharField(max_length=120,default='draft',choices=PUBLISH_CHOICES)
    author_email = models.CharField(max_length=250, null=True, blank=True, validators=[validate_author_email])
    slug = models.SlugField(null=True, blank=True)


    def __str__(self) -> str:
        return self.title
    


    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug=slugify(self.title)
        super(PostModel, self).save(*args,**kwargs)
         