from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            self.slug = slugify(self.title)
        # Ensure slug is unique
        if Post.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            import uuid
            self.slug = f"{slugify(self.title)}-{str(uuid.uuid4())[:8]}"
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
