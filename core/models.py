from django.db import models


class Student(models.Model):
    student_id = models.CharField("学号", max_length=20, unique=True)
    name = models.CharField("姓名", max_length=50)
    age = models.PositiveIntegerField("年龄")
    class_name = models.CharField("班级", max_length=50)

    def __str__(self):
        return f"{self.student_id} - {self.name}"
