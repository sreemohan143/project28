from django.db import models

# Create your models here.
class dept(models.Model):
    depno=models.PositiveIntegerField(primary_key=True)
    dname=models.CharField(max_length=100)

    def __str__(self):
        return self.depno
    
    def __str__(self):
        return self.dname
class Emp(models.Model):
    empno=models.PositiveIntegerField()
    ename=models.CharField(max_length=100)
    depno=models.ForeignKey(dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.empno
    
    def __str__(self):
        return self.ename