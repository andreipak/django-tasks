from models import AuditLogEntry
from datetime import datetime
from django.conf import settings

IGNORELIST = (
    'AuditLogEntry',
    'HttpRequestLogEntry',
    'LogEntry', #django admin app
)

def AuditLogger(sender, **kwargs):
    '''
    Logger Stores CRUD actions related to model instances
    depending on ENABLE_AUDIT setting
    '''

    if not getattr(settings, 'ENABLE_AUDIT', False):
        return

    if sender._meta.object_name in IGNORELIST:
        return

    action = AuditLogEntry.ACTION_DELETE

    if kwargs.has_key('created'):
        #created is True if a new record was created https://docs.djangoproject.com/en/dev/ref/signals/#post-save
        action = kwargs.get('created') and AuditLogEntry.ACTION_CREATE or AuditLogEntry.ACTION_UPDATE

    AuditLogEntry.objects.create(
        model=sender._meta.object_name,
        instance=unicode(kwargs.get('instance')),
        action=action)
