from django.db import models

# Create your models here.
class BookTableModel(models.Model):
    STATUS_DATE = (
        ('1','1'),('2','2'),('3','3'), ('4','4'), ('5','5'),('6','6'),('7',"7"),('8','8'),('9','9'),
        ('10','10'),('11','11'),('12','12'),('13','13'),('14','14'), ('15','15'),('16','16'),('17',"17"),('18','18'),('19','19'),('20','20'),
        ('21','21'),('22','22'),('23','23'), ('24','24'), ('25','25'),('26','26'),('27',"27"),('28','28'),('29','29'),('30','30'),
    )
    STATUS_MONTH = (
        ('1','1'),('2','2'),('3','3'), ('4','4'), ('5','5'),('6','6'),('7',"7"),('8','8'),('9','9'),
        ('10','10'),('11','11'),('12','12')
    )
    TEDAD =(
        ('1','1'),('2','2'),('3','3'), ('4','4'), ('5','5'),
    )
    TIME = (
        ('9','9'),
        ('10','10'),('11','11'),('12','12'),('13','13'),('14','14'), ('15','15'),('16','16'),('17',"17"),('18','18'),('19','19'),('20','20'),
        ('21','21'),('22','22'),('23','23')
    )
    date = models.CharField(max_length=3,choices=STATUS_DATE)
    time = models.CharField(max_length=2,choices=TIME)
    month = models.CharField(max_length=3,choices=STATUS_MONTH)
    tedad = models.CharField(max_length=2,choices=TEDAD)
    fullname = models.CharField(max_length=250)
    Note = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.fullname + ' '+self.tedad