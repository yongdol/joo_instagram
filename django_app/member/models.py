from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from photo.models import PhotoLike, Photo

class MyUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    following_users = models.ManyToManyField('self', symmetrical=False, through='Relationship', related_name='follower_users')
    block_users = models.ManyToManyField('self', symmetrical=False, related_name='user_set_block')
    # like_photos = models.ManyToManyField(Photo, through=PhotoLike, related_name='user_set_like_photos')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '%s%s' % (self.last_name, self.first_name)

    def friends(self):
        return self.following_users.filter(following_users=self)

    def follow(self, user):
        instance, created = Relationship.objects.get_or_crate(follower=self, followee=user)
        return instance

    def unfollow(self, user):
        Relationship.objects.filter(follower=self, followee=user).delete()

    def block(self, user):
        self.block_users.add(user)

    def unblock(self, user):
        self.block_users.remove(user)

    def is_friends(self, user):
        if user in self.friends():
            return True
        return False

class Relationship(models.Model):
    follower = models.ForeignKey(MyUser, related_name='relationship_set_follower')
    followee = models.ForeignKey(MyUser, related_name='relationship_set_followee')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followee')

    def __str__(self):
        return 'Relation(Follower(%s), Followee(%s))' % (self.follower.get_full_name(), self.followee.get_full_name(),)

