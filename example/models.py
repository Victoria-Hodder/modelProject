from django.db import models

class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):
        return self.text

class DateExample(models.Model):
    the_date = models.DateTimeField()

    def __str__(self):
        return self.the_date

class NullExample(models.Model):
    col = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.col

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    #ForeignKey represents the one to many relationship

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

"""
Notes:
put many to many relationship on the class which has a "lower level" - in this case Movie is of higher importance.
there's no column in the database so Django creates a new table


>>> avengeres = Movie.objects.get(name = 'Avengers')
>>> avengeres
<Movie: Avengers>
>>> avengeres.character_set.all()
<QuerySet [<Character: Captain America>, <Character: Thor>]>

Use '_set' to access the characters of a movie because Movie class has no characters field


what is unicode??  __str__/string formatting - preferred
Could I add order_by so that it has a reverse order in the admin page??

"""