from django.db import models


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)
    DepartmentImage = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.DepartmentName} with the ID - {self.DepartmentId}" 

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField(auto_now_add=True)
    PhotoFileName = models.CharField(max_length=100) 
    Email = models.CharField(max_length=150, blank=True, null=True)
    Bio = models.TextField(blank=True, null=True)
    Primary_Tech = models.CharField(max_length=100, blank=True, null=True)
    Primary_Tech_Experience = models.CharField(max_length=100, blank=True, null=True)
    Working = models.CharField(max_length=100, blank=True, null=True)
    Expected_Sallary = models.IntegerField(default=100, blank=True, null=True)
    Location = models.CharField(max_length=300, blank=True, null=True)
    Remote = models.BooleanField(default=False, blank=True, null=True)
    soft_report = models.BooleanField(default=False, blank=True, null=True)
    tech_report = models.BooleanField(default=False, blank=True, null=True)

    WorkExperience1_title = models.CharField(max_length=100, blank=True, null=True)
    WorkExperience1_startYear = models.IntegerField(default=2000, blank=True, null=True)
    WorkExperience1_startMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience1_endYear = models.IntegerField(default=2000, blank=True, null=True)
    WorkExperience1_endMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience1_techs = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience1_company = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience1_companyLink = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience1_description = models.CharField(max_length=300, blank=True, null=True)

    WorkExperience2_title = models.CharField(max_length=100, blank=True, null=True)
    WorkExperience2_startYear = models.IntegerField(blank=True, null=True)
    WorkExperience2_startMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience2_endYear = models.IntegerField(blank=True, null=True)
    WorkExperience2_endMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience2_techs = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience2_company = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience2_companyLink = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience2_description = models.CharField(max_length=300, blank=True, null=True)

    WorkExperience3_title = models.CharField(max_length=100, blank=True, null=True)
    WorkExperience3_startYear = models.IntegerField(blank=True, null=True)
    WorkExperience3_startMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience3_endYear = models.IntegerField(blank=True, null=True)
    WorkExperience3_endMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience3_techs = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience3_company = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience3_companyLink = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience3_description = models.CharField(max_length=300, blank=True, null=True)

    WorkExperience4_title = models.CharField(max_length=100, blank=True, null=True)
    WorkExperience4_startYear = models.IntegerField(blank=True, null=True)
    WorkExperience4_startMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience4_endYear = models.IntegerField(blank=True, null=True)
    WorkExperience4_endMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience4_techs = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience4_company = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience4_companyLink = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience4_description = models.CharField(max_length=300, blank=True, null=True)

    WorkExperience5_title = models.CharField(max_length=100, blank=True, null=True)
    WorkExperience5_startYear = models.IntegerField(blank=True, null=True)
    WorkExperience5_startMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience5_endYear = models.IntegerField(blank=True, null=True)
    WorkExperience5_endMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience5_techs = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience5_company = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience5_companyLink = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience5_description = models.CharField(max_length=300, blank=True, null=True)

    WorkExperience6_title = models.CharField(max_length=100, blank=True, null=True)
    WorkExperience6_startYear = models.IntegerField(blank=True, null=True)
    WorkExperience6_startMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience6_endYear = models.IntegerField(blank=True, null=True)
    WorkExperience6_endMonth = models.CharField(max_length=12, blank=True, null=True)
    WorkExperience6_techs = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience6_company = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience6_companyLink = models.CharField(max_length=300, blank=True, null=True)
    WorkExperience6_description = models.CharField(max_length=300, blank=True, null=True)

    tech1 = models.CharField(max_length=100, blank=True, null=True)
    tech1_version = models.CharField(max_length=100, blank=True, null=True)
    tech1_experience = models.CharField(max_length=100, blank=True, null=True)

    tech2 = models.CharField(max_length=100, blank=True, null=True)
    tech2_version = models.CharField(max_length=100, blank=True, null=True)
    tech2_experience = models.CharField(max_length=100, blank=True, null=True)

    tech3 = models.CharField(max_length=100, blank=True, null=True)
    tech3_version = models.CharField(max_length=100, blank=True, null=True)
    tech3_experience = models.CharField(max_length=100, blank=True, null=True)

    tech4 = models.CharField(max_length=100, blank=True, null=True)
    tech4_version = models.CharField(max_length=100, blank=True, null=True)
    tech4_experience = models.CharField(max_length=100, blank=True, null=True)

    tech5 = models.CharField(max_length=100, blank=True, null=True)
    tech5_version = models.CharField(max_length=100, blank=True, null=True)
    tech5_experience = models.CharField(max_length=100, blank=True, null=True)

    tech6 = models.CharField(max_length=100, blank=True, null=True)
    tech6_version = models.CharField(max_length=100, blank=True, null=True)
    tech6_experience = models.CharField(max_length=100, blank=True, null=True)

    tech7 = models.CharField(max_length=100, blank=True, null=True)
    tech7_version = models.CharField(max_length=100, blank=True, null=True)
    tech7_experience = models.CharField(max_length=100, blank=True, null=True)

    tech8 = models.CharField(max_length=100, blank=True, null=True)
    tech8_version = models.CharField(max_length=100, blank=True, null=True)
    tech8_experience = models.CharField(max_length=100, blank=True, null=True)

    hobbies = models.TextField(blank=True, null=True)
    language1 = models.CharField(max_length=150, blank=True, null=True)
    language1_level = models.CharField(max_length=150, blank=True, null=True)
    language2 = models.CharField(max_length=150, blank=True, null=True)
    language2_level = models.CharField(max_length=150, blank=True, null=True)
    language3 = models.CharField(max_length=150, blank=True, null=True)
    language3_level = models.CharField(max_length=150, blank=True, null=True)
    language4 = models.CharField(max_length=150, blank=True, null=True)
    language4_level = models.CharField(max_length=150, blank=True, null=True)
    language5 = models.CharField(max_length=150, blank=True, null=True)
    language5_level = models.CharField(max_length=150, blank=True, null=True)
    
    github = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    portfolio = models.CharField(max_length=100, blank=True, null=True)

    Views = models.IntegerField(default=0, blank=True, null=True)
    Rating = models.IntegerField(default=0, blank=True, null=True)
    Featured = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.EmployeeName} is a new {self.Primary_Tech} with {self.Views} views" 


class Tech(models.Model):
    TechId = models.AutoField(primary_key=True)
    TechName = models.CharField(max_length=100)
    TechImage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.TechName} with the ID - {self.TechId}" 

class TechReport(models.Model):
    TechReportId = models.AutoField(primary_key=True)
    EmployeeId = models.CharField(max_length=100)
    techName = models.CharField(max_length=300)
    techEmail = models.CharField(max_length=300)
    techCompany = models.CharField(max_length=300, blank=True, null=True)
    techVAT = models.CharField(max_length=100, blank=True, null=True)
    stata = (
        ('Completed', 'Completed'), 
        ('Pending', 'Pending'), 
        ('Unread', 'Unread')
    )
    status = models.CharField(max_length=64, choices=stata)

    def __str__(self):
        return f"{self.techName} asked for Tech Report for employee - {self.EmployeeId} - and the request id {self.status}" 

class SoftReport(models.Model):
    SoftReportId = models.AutoField(primary_key=True)
    EmployeeId = models.CharField(max_length=100)
    softName = models.CharField(max_length=300)
    softEmail = models.CharField(max_length=300)
    softCompany = models.CharField(max_length=300, blank=True, null=True)
    softVAT = models.CharField(max_length=100, blank=True, null=True)
    stata = (
        ('Completed', 'Completed'), 
        ('Pending', 'Pending'), 
        ('Unread', 'Unread')
    )
    status = models.CharField(max_length=64, choices=stata)

    def __str__(self):
        return f"{self.softName} asked for Tech Report for employee - {self.EmployeeId} - and the request id {self.status}" 

class Message(models.Model):
    messageId = models.AutoField(primary_key=True)
    senderName = models.CharField(max_length=100)
    senderEmail = models.CharField(max_length=100)
    receiverName = models.CharField(max_length=100)
    receiverEmail = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    sendDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    stata = (
        ('Read', 'Read'), 
        ('Unread', 'Unread'),
        ('Archive', 'Archive')
    )
    status = models.CharField(max_length=64, choices=stata)

    def __str__(self):
        return f"{self.senderName} sent a message to {self.receiverName} and it is {self.status} at {self.sendDate}"

class Contact(models.Model):
    contactId = models.AutoField(primary_key=True)
    time = models.DateField(auto_now_add=True)
    senderName = models.CharField(max_length=100, blank=True, null=True)
    senderEmail = models.CharField(max_length=100, blank=True, null=True)
    senderMessage = models.TextField(blank=True, null=True)
    senderSKU = models.CharField(max_length=100, blank=True, null=True)
    stata = (
        ('Completed', 'Completed'), 
        ('Pending', 'Pending'), 
        ('Unread', 'Unread')
    )
    status = models.CharField(max_length=64, choices=stata)

    def __str__(self):
        return f"Received a message from {self.senderEmail} on {self.time} and the  status is {self.status}" 


class Newsletter(models.Model):
    contactId = models.AutoField(primary_key=True)
    time = models.DateField(auto_now_add=True)
    senderEmail = models.CharField(max_length=100, blank=True, null=True)
    stata = (
        ('Added to the Database', 'Added to the Database'), 
        ('WARNING - ADD TO THE DATABASE', 'WARNING - ADD TO THE DATABASE'), 
    )
    status = models.CharField(max_length=64, choices=stata)

    def __str__(self):
        return f"Received a newsletter request from {self.senderEmail} on {self.time} and the status is {self.status}" 