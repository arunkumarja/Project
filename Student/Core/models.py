from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='core_role'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)
    gender = models.CharField(max_length=10) 

    class Meta:
        db_table='core_users' 


class Attendance(models.Model):
    date = models.DateField()
    attendance_status = models.BooleanField()
    user = models.ForeignKey("User", on_delete=models.CASCADE) 
     
    class Meta:
        db_table='core_attendance'


    def __str__(self):
        return self.user

class Mark(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()


    class Meta:
        db_table='core_mark'     

class Student(models.Model):
    department = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.department



class Teacher(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    

class Hod(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    