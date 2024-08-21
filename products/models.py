from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    image = models.ImageField(
        upload_to="images/",
        blank=True,  # 이미지는 필수가 아님
        # null=True
    )

    def __str__(self):
        return self.title