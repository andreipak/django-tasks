from models import HttpRequestLogEntry
from django.db.models import F
from django.contrib import admin

class HRLEAdmin(admin.ModelAdmin):
    actions = ['increase_priority', 'decrease_priority', 'reset_priority']
    date_hierarchy = 'date'
    ordering = ['-priority', '-date']

    def increase_priority(self, request, queryset):
        count = queryset.update(priority=F('priority') + 1)
        self.notify(request,'Priority increased', count)

    def decrease_priority(self, request, queryset):
        count = queryset.update(priority=F('priority') - 1)
        self.notify(request,'Priority decreased', count)


    def reset_priority(self, request, queryset):
        count = queryset.update(priority=0)
        self.notify(request, 'Priority reset', count)


    def notify(self, request, action, count):
        sfx = count > 1 and 'ies' or 'y'
        self.message_user(request, "%s for %d entr%s" % (action, count, sfx))

    increase_priority.short_description = "Priority: increase value"
    decrease_priority.short_description = "Priority: decrease value"
    reset_priority.short_description = "Priority: reset to default"

admin.site.register(HttpRequestLogEntry, HRLEAdmin)