from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        ordering = ["-created"]

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


class Comment(models.Model):
    author = models.CharField(max_length=70, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, blank=True)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return u"{0}: {1} on {2}".format(self.author, self.body[:50], self.post)