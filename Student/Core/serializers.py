from rest_framework import serializers
from Core.models import User,Role,Attendance,Mark,Student,Teacher,Hod

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=['name']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=['attendance_status','date']

class MarkSerializer(serializers.ModelSerializer):
     class Meta:
        model=Mark 
        fields=['sub1','sub2','sub3','sub4','sub5']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['department','year','id']    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__' 

class HodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hod
        fields='__all__'                             
