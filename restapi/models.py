from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    time = models.BigIntegerField(null=False, blank=False)
    date = models.DateField(unique=True, null=False)
    location = models.CharField(max_length=256)
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)


class UserDetails(models.Model):
    user_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False, blank=False)
    email=models.EmailField()
    mobile=models.IntegerField(max_length=10)
    address=models.TextField()
    usertype= models.CharField(max_length=10)
    username=models.CharField(max_length=20,null=False, blank=False)
    password=models.CharField(max_length=50)
    zone=models.CharField(max_length=10)
    is_active=models.BooleanField()
    created_at=models.BigIntegerField(null=False, blank=False)
    modified_at=models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table= "user_details"


class CompanyDetails(models.Model):
    comp_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=100,null=False, blank=False)
    company_website=models.CharField(max_length=100)
    zone=models.CharField(max_length=100)
    inception=models.CharField(max_length=100)
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table= "Company_Details"

class ContactAlumni(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    comp_id = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=50)
    referred_by = models.CharField(max_length=50)
    email = models.EmailField()
    designation = models.CharField(max_length=50)
    department= models.CharField(max_length=50)
    mobile_number = models.IntegerField(max_length=12)
    direct_number = models.IntegerField(max_length=50)
    notes = models.TextField()
    institution= models.CharField(max_length=50)
    institution_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    total_experience = models.DurationField()
    yop = models.IntegerField()
    degree = models.CharField(max_length=50)
    current_experience = models.DurationField()
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    # office_id = models.ForeignKey(on_delete=models.CASCADE)
    address = models.TextField()
    board_line_no = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pin= models.IntegerField()
    recruitment = models.BooleanField()
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table= "Contact_alumni"



class ExternalMeetings(models.Model):
    meet_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    contact_id = models.ForeignKey(ContactAlumni,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    agenda = models.CharField(max_length=150)
    meeting_date = models.DateField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    location = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    meeting_type = models.CharField(max_length=100)
    description = models.TextField()
    is_open = models.BooleanField()
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table= "External_Meetings"


class InternalMeeting(models.Model):
    meet_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    agenda = models.CharField(max_length=150)
    meeting_date = models.DateField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    meeting_type = models.CharField(max_length=100)
    description = models.TextField()
    is_open = models.BooleanField()
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table= "Internal_Meetings"

class TravelPlan(models.Model):
    tr_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    travel_date = models.DateTimeField(auto_now=False,auto_now_add=False)
    return_date = models.DateTimeField(auto_now=False,auto_now_add=False)
    accompanied_by = models.CharField(max_length=50)
    travel_from = models.CharField(max_length=50)
    travel_to = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    is_open = models.BooleanField()
    created_at = models.BigIntegerField(null=False, blank=False)
    modified_at = models.BigIntegerField(null=False, blank=False)


    class Meta:
        db_table= "Travel_plan"












