from rest_framework import serializers
from EmployeeApp.models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName', 'DepartmentImage')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department', 'PhotoFileName', 'DateOfJoining', 'Email', 'Primary_Tech', 'Location', 'Expected_Sallary', 'Working', 'Bio', 'Remote',
                  'WorkExperience1_title', 'WorkExperience1_startYear',   'WorkExperience1_startMonth', 'WorkExperience1_endYear', 'WorkExperience1_endMonth', 'WorkExperience1_techs',
                  'WorkExperience1_company', 'WorkExperience1_companyLink', 'WorkExperience1_description', 'Views', 'WorkExperience2_title', 'WorkExperience2_startYear', 'WorkExperience2_startMonth', 'WorkExperience2_endYear', 'WorkExperience2_endMonth', 'WorkExperience2_techs',
                  'WorkExperience2_company', 'WorkExperience2_companyLink', 'WorkExperience2_description', 'WorkExperience3_title', 'WorkExperience3_startYear', 'WorkExperience3_startMonth', 'WorkExperience3_endYear', 'WorkExperience3_endMonth', 'WorkExperience3_techs',
                  'WorkExperience3_company', 'WorkExperience3_companyLink', 'WorkExperience3_description', 'WorkExperience4_title', 'WorkExperience4_startYear', 'WorkExperience4_startMonth', 'WorkExperience4_endYear', 'WorkExperience4_endMonth', 'WorkExperience4_techs',
                  'WorkExperience4_company', 'WorkExperience4_companyLink', 'WorkExperience4_description', 'WorkExperience5_title', 'WorkExperience5_startYear', 'WorkExperience5_startMonth', 'WorkExperience5_endYear', 'WorkExperience5_endMonth', 'WorkExperience5_techs',
                  'WorkExperience5_company', 'WorkExperience5_companyLink', 'WorkExperience5_description', 'WorkExperience6_title', 'WorkExperience6_startYear', 'WorkExperience6_startMonth', 'WorkExperience6_endYear', 'WorkExperience6_endMonth', 'WorkExperience6_techs',
                  'WorkExperience6_company', 'WorkExperience6_companyLink', 'WorkExperience6_description', 'tech1', 'tech1_version', 'tech1_experience', 'tech2', 'tech2_version', 'tech2_experience', 'tech3', 'tech3_version', 'tech3_experience',
                  'tech4', 'tech4_version', 'tech4_experience', 'tech5', 'tech5_version', 'tech5_experience', 'tech6', 'tech6_version', 'tech6_experience', 'tech7', 'tech7_version',
                  'tech7_experience', 'tech8', 'tech8_version', 'tech8_experience', 'hobbies', 'language1', 'language1_level', 'language2', 'language2_level', 'language3',
                  'language3_level', 'language4', 'language4_level', 'language5', 'language5_level', 'youtube', 'linkedin', 'github', 'portfolio', 'Featured',
                  )


class addEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeName', 'Department', 'PhotoFileName', 'Primary_Tech', 'Location',
                  'Bio', 'Email', 'Working', 'youtube', 'linkedin', 'github', 'portfolio')


class updateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'Email', 'Location', 'Expected_Sallary', 'Working', 'Bio', 'WorkExperience1_title', 'WorkExperience1_startYear', 'WorkExperience1_startMonth',
                  'WorkExperience1_endYear', 'WorkExperience1_endMonth', 'WorkExperience1_techs', 'Remote',
                  'WorkExperience1_company', 'WorkExperience1_companyLink', 'WorkExperience1_description', 'WorkExperience2_title', 'WorkExperience2_startYear', 'WorkExperience2_startMonth',
                  'WorkExperience2_endYear', 'WorkExperience2_endMonth', 'WorkExperience2_techs',
                  'WorkExperience2_company', 'WorkExperience2_companyLink', 'WorkExperience2_description', 'WorkExperience3_title', 'WorkExperience3_startYear', 'WorkExperience3_startMonth',
                  'WorkExperience3_endYear', 'WorkExperience3_endMonth', 'WorkExperience3_techs',
                  'WorkExperience3_company', 'WorkExperience3_companyLink', 'WorkExperience3_description', 'WorkExperience4_title', 'WorkExperience4_startYear', 'WorkExperience4_startMonth',
                  'WorkExperience4_endYear', 'WorkExperience4_endMonth', 'WorkExperience4_techs',
                  'WorkExperience4_company', 'WorkExperience4_companyLink', 'WorkExperience4_description', 'WorkExperience5_title', 'WorkExperience5_startYear', 'WorkExperience5_startMonth',
                  'WorkExperience5_endYear', 'WorkExperience5_endMonth', 'WorkExperience5_techs',
                  'WorkExperience5_company', 'WorkExperience5_companyLink', 'WorkExperience5_description', 'WorkExperience6_title', 'WorkExperience6_startYear', 'WorkExperience6_startMonth',
                  'WorkExperience6_endYear', 'WorkExperience6_endMonth', 'WorkExperience6_techs',
                  'WorkExperience6_company', 'WorkExperience6_companyLink', 'WorkExperience6_description', 'tech1', 'tech1_version', 'tech1_experience', 'tech2', 'tech2_version',
                  'tech2_experience', 'tech3', 'tech3_version', 'tech3_experience',
                  'tech4', 'tech4_version', 'tech4_experience', 'tech5', 'tech5_version', 'tech5_experience', 'tech6', 'tech6_version', 'tech6_experience', 'tech7', 'tech7_version',
                  'tech7_experience', 'tech8', 'tech8_version', 'tech8_experience',
                  'hobbies', 'language1', 'language1_level', 'language2', 'language2_level', 'language3', 'language3_level', 'language4', 'language4_level', 'language5', 'language5_level',
                  'github', 'linkedin', 'youtube', 'portfolio')


class techSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ('TechId', 'TechName', 'TechImage')


class employeeTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechReport
        fields = ('EmployeeId', 'techName', 'techEmail',
                  'techCompany', 'techVAT', 'status')


class employeeSoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftReport
        fields = ('EmployeeId', 'softName', 'softEmail',
                  'softCompany', 'softVAT', 'status')


class addContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('senderName', 'senderEmail',
                  'senderMessage', 'senderSKU', 'status')


class addNewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('senderEmail', 'status')


class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('senderName', 'senderEmail', 'receiverName',
                  'receiverEmail', 'message', 'sendDate', 'status', 'messageId')


class messageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('messageId', 'status')
