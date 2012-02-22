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
