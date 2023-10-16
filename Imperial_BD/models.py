from django.db import models

# Create your models here.


class Universes(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Universe"
        verbose_name_plural = "Universes"


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    universe = models.ForeignKey(Universes, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/")
    gender = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    dynasty = models.CharField(max_length=80)
    tall = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    joke_names = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    organizations = models.CharField(max_length=50)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Names(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Name"
        verbose_name_plural = "Names"


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    level = models.ForeignKey('Levels', on_delete=models.PROTECT, null=True)
    tasks_completed = models.IntegerField(default=0)
    password = models.CharField(max_length=150)
    level_pyramid = models.ForeignKey('Levels_pyramid', on_delete=models.PROTECT, null=True)
    read_task = models.TextField(default='|0', null=True)
    check_task = models.BooleanField(default=False)
    id_task = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class Levels(models.Model):
    level = models.CharField(max_length=30)

    def __str__(self):
        return self.level


class Directive(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.TextField()

    def __str__(self):
        return str(self.id)


class Levels_pyramid(models.Model):
    level = models.CharField(max_length=30)

    def __str__(self):
        return self.level
