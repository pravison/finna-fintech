from django.db import models

# Create your models here.
class CompanyInfor(models.Model):
    name = models.CharField(max_length=200)
    pitch_message= models.CharField(max_length=100, help_text='this is the text that will appear at hero section of your page')
    call_to_action_message= models.CharField(max_length=100, help_text='this is the text that will appear at call to action section')
    address = models.TextField(max_length=250)
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linkedln_url = models.URLField(blank=True, null=True)
    x_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    whatsapp_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    customer_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    message = models.TextField(max_length=700)

    def __str__(self):
        return self.customer_name
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    summary = models.TextField(max_length=700)
    x_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedln_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class About(models.Model):
    about_us_pitch = models.CharField(max_length=200)
    about_us_summary = models.TextField(max_length=1000)
    interest_rate_summary = models.TextField(max_length=200)
    average_loan_approval_time_summary = models.TextField(max_length=200)
    client_satisfaction_summary = models.TextField(max_length=200)
    number_of_loan_disbursed = models.IntegerField(null=True, blank=True)
    number_of_customers_served = models.IntegerField(null=True, blank=True)
    percentage_repeat_borrowers =  models.IntegerField(null=True, blank=True)
    percentage_loan_repayment_success_rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.about_us_pitch
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

