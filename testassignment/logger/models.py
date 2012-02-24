from django.db import models


from django.db import models

class HttpRequestLogEntry(models.Model):
    class Meta:
        verbose_name = "HTTP Request Log Entry"
        verbose_name_plural = "HTTP Request Log Entries"

    date = models.DateTimeField('Request date/time', db_index=True)
    request_method = models.CharField('Method', max_length=6, db_index=True) #len('DELETE') == 6
    path = models.CharField(max_length=256)
    query_string = models.CharField(max_length=256) #btw, HTTP 1.1 length of URL is 2,083 characters.
    priority = models.IntegerField(default=0, db_index=True)

    def __unicode__(self):
        return u'%d %s [%s] %s' % (
                    self.priority,
                    self.date.strftime('%Y-%m-%d %H:%M:%S'),
                    self.request_method,
                    self.path
                )



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
