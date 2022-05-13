from django.db import models

# Create your models here.


class ShopModel(models.Model):
	TIME = (
        ('9','9'),
        ('10','10'),('11','11'),('12','12'),('13','13'),('14','14'), ('15','15'),('16','16'),('17',"17"),('18','18'),('19','19'),('20','20'),
        ('21','21'),('22','22'),('23','23'),('1','1'),('2','2')
    )
	Fullname = models.CharField(max_length=300)
	locations = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	date = models.CharField(max_length=3,choices=TIME,default='9')


	def __str__(self):
		return self.name +" "+self.date
