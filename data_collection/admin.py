from django.contrib import admin

from .models import Worker, OfficialInformation, Institution, Leave, Transformation, PostingTransfer, Union

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('file_number', 'surname', 'other_names', 'title', 'sex', 'date_of_birth', 'email_address')
    search_fields = ('file_number', 'surname', 'other_names', 'email_address')
    list_filter = ('sex', 'marital_status', 'lga_of_origin', 'state_of_origin', 'nationality')

@admin.register(OfficialInformation)
class OfficialInformationAdmin(admin.ModelAdmin):
    list_display = ('worker', 'lga_ministry', 'present_post_location', 'post_work_state', 'department', 'rank')
    search_fields = ('worker__surname', 'worker__file_number', 'lga_ministry', 'present_post_location')
    list_filter = ('lga_ministry', 'present_post_location', 'post_work_state', 'department', 'rank')

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('worker', 'name', 'education_type', 'start_date', 'end_date', 'certificate_obtained')
    search_fields = ('worker__surname', 'worker__file_number', 'name', 'certificate_obtained')
    list_filter = ('education_type',)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('worker', 'leave_start_date', 'leave_type', 'date_of_reinstatement', 'authorization')
    search_fields = ('worker__surname', 'worker__file_number', 'leave_type', 'authorization')
    list_filter = ('leave_type',)

@admin.register(Transformation)
class TransformationAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'rank_designation', 'entry_pt', 'authorization', 'ministry_department')
    search_fields = ('worker__surname', 'worker__file_number', 'rank_designation', 'entry_pt', 'authorization', 'ministry_department')

@admin.register(PostingTransfer)
class PostingTransferAdmin(admin.ModelAdmin):
    list_display = ('worker', 'from_department', 'date', 'to_department', 'authorization')
    search_fields = ('worker__surname', 'worker__file_number', 'from_department', 'to_department', 'authorization')

@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)