from datetime import timezone

from django.db import models


class SoftDeletableQS(models.QuerySet):
    """A queryset that allows soft-delete on its objects"""

    def delete(self, **kwargs):
        self.update(deleted_ts=timezone.now(), **kwargs)

    def hard_delete(self, **kwargs):
        super().delete(**kwargs)


class SoftDeletableManager(models.Manager):
    """Manager that filters out soft-deleted objects"""

    def get_queryset(self):
        return SoftDeletableQS(
            model=self.model, using=self._db, hints=self._hints
        ).filter(
            deleted_ts__isnull=True
        )
