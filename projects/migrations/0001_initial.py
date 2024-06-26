# Generated by Django 4.2 on 2024-06-20 05:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proyek",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nama", models.CharField(max_length=50)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("SQL", "SQL"),
                            ("Power BI", "Power BI"),
                            ("Tableau", "Tableau"),
                            ("Python Dash", "Python Dash"),
                            ("Python Django", "Python Django"),
                        ],
                        max_length=50,
                    ),
                ),
                ("gambar", models.ImageField(blank=True, upload_to="media")),
                ("gambar2", models.ImageField(blank=True, upload_to="media")),
                ("gambar3", models.ImageField(blank=True, upload_to="media")),
                ("gambar4", models.ImageField(blank=True, upload_to="media")),
                ("tanggal", models.DateField(default=django.utils.timezone.now)),
                ("client", models.CharField(max_length=55)),
                ("output", models.URLField(default="a")),
                ("detail", models.URLField(default="a")),
                ("slug", models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name="result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isi", models.TextField()),
                ("gambar", models.ImageField(blank=True, upload_to="")),
                ("code", models.TextField(blank=True)),
                (
                    "namaProject",
                    models.ManyToManyField(
                        related_name="results", to="projects.proyek"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="recommendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isi", models.TextField()),
                (
                    "namaProject",
                    models.ManyToManyField(
                        related_name="recomendation", to="projects.proyek"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="purpose",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isi", models.TextField(blank=True)),
                ("heading", models.TextField(blank=True)),
                (
                    "namaProject",
                    models.ManyToManyField(
                        related_name="purpose", to="projects.proyek"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="insight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isi", models.TextField()),
                (
                    "namaProject",
                    models.ManyToManyField(
                        related_name="insight", to="projects.proyek"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="dataset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.TextField(blank=True)),
                ("link", models.CharField(blank=True, max_length=200)),
                ("contentLink", models.CharField(blank=True, max_length=200)),
                (
                    "namaProject",
                    models.ManyToManyField(
                        related_name="dataset", to="projects.proyek"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="dataPrep",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.CharField(max_length=200)),
                ("code", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="")),
                (
                    "namaProject",
                    models.ManyToManyField(
                        related_name="dataprep", to="projects.proyek"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="background",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("background", models.TextField()),
                (
                    "namaProject",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.proyek",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
