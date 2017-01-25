# 笔记

## 多个字段作主键
```python
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']
```

## `HyperlinkedRelatedField`与`HyperlinkedIdentityField`的区别
前者在关联字段中查询，而后者在自身查询。
```python
# search `lookup_field` in `author`
class ProblemListSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail'
)

# search `lookup_field` in `self`
class ProblemListSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail'
)
```