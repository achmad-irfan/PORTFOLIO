from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Proyek(models.Model):
    ITEM_CHOICES = [
        ('SQL', 'SQL'),
        ('Power BI', 'Power BI'),
        ('Tableau', 'Tableau'),
        ('Python Dash', 'Python Dash'),
        ('Python Django', 'Python Django'),
    ]
    nama = models.CharField(max_length=50)
    category = models.CharField(choices=ITEM_CHOICES, max_length=50)
    gambar = models.ImageField(upload_to='media', blank=True)
    gambar2 = models.ImageField(upload_to='media', blank=True)
    gambar3 = models.ImageField(upload_to='media', blank=True)
    gambar4 = models.ImageField(upload_to='media', blank=True)
    tanggal = models.DateField(default=timezone.now)
    client = models.CharField(max_length=55)
    output = models.URLField(default='a')
    detail = models.URLField(default='a')
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.nama)
        super(Proyek, self).save()

    def __str__(self):
        return "{} - {}".format(self.nama, self.category)


class heading(models.Model):
    namaProject = models.OneToOneField(
        Proyek, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.namaProject)

    class Meta:
        abstract = True


class background(heading):
    background = models.TextField()


class dataset(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='dataset', )
    heading = models.TextField(blank=True)
    link = models.CharField(max_length=200, blank=True)
    contentLink = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"dataset-{', '.join([str(proyek) for proyek in self.namaProject.all()])}"


class purpose(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='purpose')
    isi = models.TextField(blank=True)
    heading = models.TextField(blank=True)

    def __str__(self):
        return f"purpose-{', '.join([str(proyek) for proyek in self.namaProject.all()])}"


class result(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='results', )
    isi = models.TextField()
    gambar = models.ImageField(blank=True)
    code = models.TextField(blank=True)

    def __str__(self):
        return f"result-{', '.join([str(proyek) for proyek in self.namaProject.all()])}"


class insight(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='insight')
    isi = models.TextField()

    def __str__(self):
        return "{}".format(self.namaProject)


class recommendation(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='recomendation')
    isi = models.TextField()

    def __str__(self):
        return "{}".format(self.namaProject)


class dataPrep(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='dataprep')
    heading = models.CharField(max_length=200)
    code = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"dataprep-{', '.join([str(proyek) for proyek in self.namaProject.all()])}"
