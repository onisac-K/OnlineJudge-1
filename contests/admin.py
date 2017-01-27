from django.contrib import admin
from contests.models import (
    Contest,
    ContestAccount,
    ContestProblem,
    ContestSubmission,
    ContestStatistic,
)
# Register your models here.
admin.site.register(Contest)
admin.site.register(ContestAccount)
admin.site.register(ContestProblem)
admin.site.register(ContestSubmission)
admin.site.register(ContestStatistic)
