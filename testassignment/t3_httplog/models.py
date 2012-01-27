from django.db import models

class HttpRequestLogEntry(models.Model):
    date = models.DateTimeField('Request date/time', db_index=True)
    request_method = models.CharField('Method', max_length=6, db_index=True) #len('DELETE') == 6
    path = models.CharField(max_length=256)
    query_string = models.CharField(max_length=256) #btw, HTTP 1.1 length of URL is 2,083 characters.

    #http_user_agent = models.CharField(max_length=128)
    #http_referer = models.CharField(max_length=256)
    #remote_addr = models.CharField(max_length=15) #127.000.000.001

    def __unicode__(self):
        return u'%s %s %s' % (
                    self.date.strftime('%Y-%m-%d %H:%M:%S'),
                    self.request_method,
                    self.path
                )
