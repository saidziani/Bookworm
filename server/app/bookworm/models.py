from django.db import models


# Categories model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


# Houses model
class House(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


# Writers model
class Writer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)

    def __str__(self):
        return self.fname + " " + self.lname

    class Meta:
        ordering = ('lname',)


# Books model
class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
