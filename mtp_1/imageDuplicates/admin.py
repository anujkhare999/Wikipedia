from django.contrib import admin
from .models import Entity_hi,surfaceNames_hi,entitySurfaceNames_hi,Mention2_hi,Mention_hi
# from .models import Choice

# # Register your models here.

class Entity_hiAdmin(admin.ModelAdmin):
    list_display=["entityId","entityName"]

class surfaceNames_hiAdmin(admin.ModelAdmin):
    list_display=["surfaceNamesId","surfaceName"]

admin.site.register(Entity_hi, Entity_hiAdmin)
admin.site.register(surfaceNames_hi,surfaceNames_hiAdmin)
admin.site.register(entitySurfaceNames_hi)
admin.site.register(Mention2_hi)
admin.site.register(Mention_hi)


# class QuestionAdmin(admin.ModelAdmin):
#     # fields=['pub_date','question_text']
#     fieldsets=[
#         (None, {'fields':['question_text']}),
#         (None, {'fields':['link']}),
#         # ('Date information', {'fields':['pub_date']}),
#     ]

# admin.site.register(Question,QuestionAdmin)    
