from django.db import models

class Worker(models.Model):
    file_number = models.CharField(max_length=100, unique=True)
    surname = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    title = models.CharField(max_length=50, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Prof', 'Prof')])
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    marital_status = models.CharField(max_length=20, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')])
    religion = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    maiden_name = models.CharField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=10)
    residential_address = models.TextField()
    permanent_home_address = models.TextField()
    town_of_origin = models.CharField(max_length=100)
    lga_of_origin = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)
    mobile_numbers = models.CharField(max_length=100)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_phone_number = models.CharField(max_length=100, blank=True, null=True)
    nok_name = models.CharField(max_length=100)
    nok_address = models.TextField()
    nok_relationship = models.CharField(max_length=50)
    nok_email_address = models.EmailField()
    nok_mobile_numbers = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    fingerprint = models.BinaryField(blank=True, null=True)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['file_number']),
            models.Index(fields=['surname']),
            models.Index(fields=['email_address']),
        ]

    def __str__(self):
        return f"{self.surname} {self.other_names} ({self.file_number})"

class OfficialInformation(models.Model):
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE, related_name='official_info')
    lga_ministry = models.CharField(max_length=100)
    present_post_location = models.CharField(max_length=100)
    post_work_state = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    job_class = models.CharField(max_length=100, blank=True, null=True)
    lga_of_work = models.CharField(max_length=100)
    present_station = models.CharField(max_length=100)
    salary_group = models.CharField(max_length=100)
    grade_level_step = models.CharField(max_length=100)
    pay_point = models.CharField(max_length=100)
    bank_verification_number = models.CharField(max_length=11, unique=True)
    account_number = models.CharField(max_length=20)
    employment_type = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=100)
    first_appointment_date = models.DateField()
    gazette_no_ref_1 = models.CharField(max_length=100, blank=True, null=True)
    confirmation_date = models.DateField(blank=True, null=True)
    gazette_no_ref_2 = models.CharField(max_length=100, blank=True, null=True)
    last_promotion_date = models.DateField(blank=True, null=True)
    gazette_no_ref_3 = models.CharField(max_length=100, blank=True, null=True)
    increment_date = models.DateField(blank=True, null=True)
    gazette_no_ref_4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['worker']),
            models.Index(fields=['bank_verification_number']),
        ]

    def __str__(self):
        return f"Official Information for {self.worker}"

class Institution(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='institutions')
    name = models.CharField(max_length=255)
    education_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate_obtained = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['worker']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} ({self.worker})"

class Leave(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='leaves')
    leave_start_date = models.DateField()
    leave_type = models.CharField(max_length=100)
    date_of_reinstatement = models.DateField()
    authorization = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['worker']),
            models.Index(fields=['leave_start_date']),
        ]

    def __str__(self):
        return f"Leave: {self.leave_type} ({self.worker})"

class Transformation(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='transformations')
    date = models.DateField()
    rank_designation = models.CharField(max_length=255)
    entry_pt = models.CharField(max_length=100) 
    authorization = models.CharField(max_length=255)
    ministry_department = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['worker']),
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"Transformation for {self.worker} on {self.date}"

class PostingTransfer(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='postings_transfers')
    from_department = models.CharField(max_length=255)
    date = models.DateField()
    to_department = models.CharField(max_length=255)
    authorization = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['worker']),
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"Posting/Transfer for {self.worker}"

class Union(models.Model):
    workers = models.ManyToManyField(Worker, related_name='unions')
    name = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
