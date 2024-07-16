from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_city=models.TextField(max_length=50)
    stu_enrollment=models.IntegerField(null=True)
    stu_date_of_birth=models.IntegerField()


    def __str__(self):
        return self.stu_name+' '+self.stu_email    
    
    class Meta:
        db_table='student_detail'
        ordering=['stu_name']        #arranging the name in ascending order 
       # ordering=['-stu_name']        #arranging the name in decending order 
        verbose_name='Student'              #it add the 's' in the name which is shown on the  admin panel. 
        # verbose_name_plural='Student'    #it remove the 's' in the name which is shown on the  admin panel
    


    