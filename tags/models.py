from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TaggedItemManager(models.Model):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type=content_type,
                object_id=obj_id
            )


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return str(self.label)

    objects: models.Manager['Tag'] = models.Manager()


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()

    objects: models.Manager['TaggedItem'] = models.Manager()
