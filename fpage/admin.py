from django.contrib import admin
from .models import Detail, IOT, EH, AR, ML

# Register your models here.
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('name',)
    list_display = ('name', 'email', 'course', 'score',)

    list_filter = ('course', 'score',)

@admin.register(IOT)
class IOTAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('name',)
    list_display = ('name', 'q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'score',)
    
@admin.register(EH)
class EHAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('name',)
    list_display = ('name', 'q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'score',)

@admin.register(AR)
class ARAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('name',)
    list_display = ('name', 'q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'score',)

@admin.register(ML)
class MLAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('name',)
    list_display = ('name', 'q1','q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'score',)


'''@admin.register(IOT_Q)
class IOT_QAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('quest',)
    list_display = ('quest', 'op1', 'op2', 'op3', 'op4', 'ans',)'''

