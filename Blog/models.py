from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField("Tag", blank=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __unicode__(self):
        return self.name

    @classmethod
    def getTagsWithQuantity(cls):
        tags = cls.objects.all()
        tagsQuantity = {}
        for tag in tags:
            if tag not in tagsQuantity:
                tagsQuantity[tag] = 1
            else:
                tagsQuantity[tag] += 1
        return tagsQuantity