import datetime

from django.db import models

from core.middlewares import CurrentUserMiddleware


# Create your models here.
class AuditableEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
    )
    lastmodified_by = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_lastmodified_by",
    )

    class Meta:
        abstract = True

    @staticmethod
    def get_current_user():
        return CurrentUserMiddleware.get_current_user()

    def set_user_fields(self, user):
        if user and user.pk:
            if not self.pk:
                self.created_by = user
            self.lastmodified_by = user

    def save(self, *args, **kwargs):
        current_user = self.get_current_user()
        self.set_user_fields(current_user)
        super(AuditableEntity, self).save(*args, **kwargs)
