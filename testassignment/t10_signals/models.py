from django.db import models

class AuditLogEntry(models.Model):
    """
    Stores CRUD actions related to model instance
    """
    class Meta:
        verbose_name = "AuditLog Entry"
        verbose_name_plural = "AuditLog Entries"

    ACTION_UNKNOWN = 0
    ACTION_CREATE = 1
    ACTION_UPDATE = 2
    ACTION_DELETE = 3

    ACTION_CHOICES = (
        (ACTION_UNKNOWN, 'Unknown'),
        (ACTION_CREATE, 'Create'),
        (ACTION_UPDATE, 'Update'),
        (ACTION_DELETE, 'Delete')
    )

    date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=40)
    instance = models.CharField(max_length=40)
    action = models.SmallIntegerField(max_length=1, choices=ACTION_CHOICES, default=0)

    def __unicode__(self):
        return u'%s [%s] <%s: %s>' % \
            (self.date, self.get_action_display(), self.model, self.instance)
