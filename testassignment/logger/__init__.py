from signals import AuditLogger

from django.db.models.signals import post_save
from django.db.models.signals import post_delete


post_save.connect(AuditLogger)
post_delete.connect(AuditLogger)
