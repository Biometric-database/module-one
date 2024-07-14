from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Worker, OfficialInformation, Institution, Leave, Transformation, PostingTransfer, Union
import re
from django.core.exceptions import ValidationError
from datetime import date

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        exclude = ['photo', 'fingerprint', 'signature']

    def clean_file_number(self):
        file_number = self.cleaned_data.get('file_number')
        if Worker.objects.filter(file_number=file_number).exists():
            raise forms.ValidationError(_("A worker with this file number already exists."))
        return file_number

    def clean_email_address(self):
        email_address = self.cleaned_data.get('email_address')
        if Worker.objects.filter(email_address=email_address).exists():
            raise forms.ValidationError(_("A worker with this email address already exists."))
        return email_address

    def clean_mobile_numbers(self):
        mobile_numbers = self.cleaned_data.get('mobile_numbers')
        pattern = re.compile(r'^(070|080|081|090|091|701|702|703|704|705|706|707|708|709|802|803|804|805|806|807|808|809|811|812|813|814|815|816|817|818|819|901|902|903|904|905|906|907|908|909)\d{7}$')
        if not pattern.match(mobile_numbers):
            raise forms.ValidationError(_("Invalid mobile number format. It should start with 070, 080, etc. and be 11 digits long."))
        return mobile_numbers

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth > date.today():
            raise forms.ValidationError(_("Date of birth cannot be in the future."))
        return date_of_birth
    

class OfficialInformationForm(forms.ModelForm):
    class Meta:
        model = OfficialInformation
        fields = [
            'worker', 'lga_ministry', 'present_post_location', 'post_work_state', 'department', 'rank', 'job_class',
            'lga_of_work', 'present_station', 'salary_group', 'grade_level_step', 'pay_point', 'bank_verification_number',
            'account_number', 'employment_type', 'employment_status', 'first_appointment_date', 'gazette_no_ref_1',
            'confirmation_date', 'gazette_no_ref_2', 'last_promotion_date', 'gazette_no_ref_3', 'increment_date', 'gazette_no_ref_4'
        ]

    def clean_confirmation_date(self):
        confirmation_date = self.cleaned_data.get('confirmation_date')
        first_appointment_date = self.cleaned_data.get('first_appointment_date')
        if confirmation_date and first_appointment_date and confirmation_date < first_appointment_date:
            raise forms.ValidationError(_("Confirmation date cannot be earlier than the first appointment date."))
        return confirmation_date

    def clean_last_promotion_date(self):
        last_promotion_date = self.cleaned_data.get('last_promotion_date')
        first_appointment_date = self.cleaned_data.get('first_appointment_date')
        if last_promotion_date and first_appointment_date and last_promotion_date < first_appointment_date:
            raise forms.ValidationError(_("Last promotion date cannot be earlier than the first appointment date."))
        return last_promotion_date
    

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['worker', 'name', 'education_type', 'start_date', 'end_date', 'certificate_obtained']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError(_("End date cannot be earlier than start date."))
        return cleaned_data
    

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['worker', 'leave_start_date', 'leave_type', 'date_of_reinstatement', 'authorization']

    def clean(self):
        cleaned_data = super().clean()
        leave_start_date = cleaned_data.get('leave_start_date')
        date_of_reinstatement = cleaned_data.get('date_of_reinstatement')
        if leave_start_date and date_of_reinstatement and date_of_reinstatement < leave_start_date:
            raise forms.ValidationError(_("Date of reinstatement cannot be earlier than leave start date."))
        return cleaned_data
    

class TransformationForm(forms.ModelForm):
    class Meta:
        model = Transformation
        fields = ['worker', 'date', 'rank_designation', 'entry_pt', 'authorization', 'ministry_department']


class PostingTransferForm(forms.ModelForm):
    class Meta:
        model = PostingTransfer
        fields = ['worker', 'from_department', 'date', 'to_department', 'authorization']


class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = ['name']


class UnionMembershipForm(forms.Form):
    union = forms.ModelChoiceField(queryset=Union.objects.all())
    workers = forms.ModelMultipleChoiceField(queryset=Worker.objects.all(), widget=forms.CheckboxSelectMultiple)