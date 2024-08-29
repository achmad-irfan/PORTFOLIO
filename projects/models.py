from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# create your models here.


class Proyek(models.Model):
    ITEM_CHOICES = [
        ('SQL', 'SQL'),
        ('Power BI', 'Power BI'),
        ('Tableau', 'Tableau'),
        ('Python Dash', 'Python Dash'),
        ('Python Django', 'Python Django'),
        ('Data Science', 'Data Sciance')
    ]
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=250)
    category = models.CharField(choices=ITEM_CHOICES, max_length=250)
    gambar = models.ImageField(upload_to='media', blank=True)
    gambar2 = models.ImageField(upload_to='media', blank=True)
    gambar3 = models.ImageField(upload_to='media', blank=True)
    gambar4 = models.ImageField(upload_to='media', blank=True)
    tanggal = models.DateField(default=timezone.now)
    client = models.CharField(max_length=55)
    output = models.URLField(default='a')
    detail = models.URLField(default='a')
    slug = models.SlugField(blank=True, editable=False)
    summary = models.TextField(max_length=25000)
    tools = models.CharField(max_length=40, blank=True)
    method = models.CharField(max_length=40, blank=True)

    def save(self):
        self.slug = slugify(self.nama)
        super(Proyek, self).save()

    def __str__(self):
        return "{} - {}".format(self.nama, self.category)


class purpose(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='purpose')
    heading = models.TextField(blank=True)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.CharField(max_length=250, blank=True)

    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=250, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"purpose-{self.namaProject}"


class datasets(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='datasets')
    heading = models.TextField(max_length=2500, blank=True)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.CharField(max_length=250, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=250, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.CharField(max_length=250, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"dataset-{self.namaProject}"


class heading(models.Model):
    namaProject = models.OneToOneField(
        Proyek, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.namaProject)

    class Meta:
        abstract = True


class background(heading):
    background = models.TextField()


class result(models.Model):
    namaProject = models.ManyToManyField(Proyek, related_name='results', )
    isi = models.TextField()
    gambar = models.ImageField(blank=True)
    code = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.namaProject)


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


class conclution(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='conclution')
    heading = models.TextField(max_length=2500)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.CharField(max_length=250, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=250, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.CharField(max_length=250, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"conclution-{self.namaProject}"


class improvment(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='improvment')
    heading = models.TextField(max_length=2500)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.CharField(max_length=250, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=250, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.CharField(max_length=250, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"improvment-{self.namaProject}"


class evaluation(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='evaluation')
    heading = models.TextField(max_length=2500)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.CharField(max_length=250, blank=True)
    Codeisi1 = models.TextField(max_length=250, blank=True)
    Imageisi1 = models.ImageField(upload_to='projects/', null=True, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=250, blank=True)
    Codeisi2 = models.TextField(max_length=250, blank=True)
    Imageisi2 = models.ImageField(upload_to='projects/', null=True, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    Codeisi3 = models.TextField(max_length=250, blank=True)
    Imageisi3 = models.ImageField(upload_to='projects/', null=True, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.CharField(max_length=250, blank=True)
    Codeisi4 = models.TextField(max_length=250, blank=True)
    Imageisi4 = models.ImageField(upload_to='projects/', null=True, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"evaluation-{self.namaProject}"


class training(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='training')
    heading = models.TextField(max_length=2500)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.TextField(max_length=250, blank=True)
    Codeisi1 = models.TextField(max_length=250, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=250, blank=True)
    codeisi2 = models.ImageField(upload_to='projects/', null=True, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.CharField(max_length=250, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"training-{self.namaProject}"


class arsitektur(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='arsitektur')
    heading = models.TextField(max_length=2500)
    isi1 = models.CharField(max_length=250, blank=True)
    Contentisi1 = models.CharField(max_length=250, blank=True)
    Codeisi1 = models.TextField(max_length=2000, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.CharField(max_length=1250, blank=True)
    Codeisi2 = models.TextField(max_length=2000, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    codeisi3 = models.ImageField(upload_to='projects/', null=True, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.TextField(max_length=2500, blank=True)
    Codeisi4 = models.TextField(max_length=2000, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)
    Codeisi5 = models.TextField(max_length=2000, blank=True)
    isi6 = models.CharField(max_length=250, blank=True)
    Contentisi6 = models.CharField(max_length=250, blank=True)
    isi7 = models.CharField(max_length=250, blank=True)
    Contentisi7 = models.CharField(max_length=250, blank=True)
    isi8 = models.CharField(max_length=250, blank=True)
    Contentisi8 = models.CharField(max_length=250, blank=True)
    isi9 = models.CharField(max_length=250, blank=True)
    Contentisi9 = models.CharField(max_length=250, blank=True)
    isi10 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"arsitektur-{self.namaProject}"


class praprocess(models.Model):
    namaProject = models.ForeignKey(
        Proyek, on_delete=models.CASCADE, related_name='praprocess')
    heading = models.TextField(max_length=2500, blank=True)
    isi1 = models.TextField(max_length=250, blank=True)
    Contentisi1 = models.TextField(max_length=250, blank=True)
    Codeisi1 = models.TextField(max_length=2000, blank=True)
    isi2 = models.CharField(max_length=250, blank=True)
    Contentisi2 = models.TextField(max_length=250, blank=True)
    Codeisi2 = models.TextField(max_length=2000, blank=True)
    isi3 = models.CharField(max_length=250, blank=True)
    Contentisi3 = models.CharField(max_length=250, blank=True)
    isi4 = models.CharField(max_length=250, blank=True)
    Contentisi4 = models.CharField(max_length=250, blank=True)
    isi5 = models.CharField(max_length=250, blank=True)
    Contentisi5 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"praprocess-{self.namaProject}"
