from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Proje Adı")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='projects/', verbose_name="Resim")
    url = models.URLField(blank=True, verbose_name="Proje Linki")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField(verbose_name="Tanıtım")
    instagram = models.URLField(blank=True, verbose_name="Instagram Linki")
    youtube = models.URLField(blank=True, verbose_name="Youtube Linki")
    tiktok = models.URLField(blank=True, verbose_name="Tiktok Linki")
    pinterest = models.URLField(blank=True, verbose_name="Pinterest Linki")
    behance = models.URLField(blank=True, verbose_name="Behance Linki")
    

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim"

class About(models.Model):
    name = models.CharField(max_length=100, verbose_name="İsim")
    title = models.CharField(max_length=100, verbose_name="Ünvan")
    message = models.TextField(verbose_name="Mesaj")
    avatar_url = models.URLField(verbose_name="Avatar URL", blank=True, null=True)
    resume_pdf = models.FileField(upload_to='resumes/', verbose_name="CV PDF", blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda"

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Yetenek Adı")
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Üst Yetenek"
    )
    level = models.CharField(
        max_length=20,
        choices=[
            ('Beginner', 'Başlangıç'),
            ('Intermediate', 'Orta'),
            ('Advanced', 'İleri'),
            ('Expert', 'Uzman')
        ],
        default='Intermediate',
        verbose_name="Seviye"
    )
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    years_of_experience = models.PositiveIntegerField(verbose_name='Yıllık Deneyim')

    class Meta:
        verbose_name = "Yetenek"
        verbose_name_plural = "Yetenekler"
        ordering = ['name']

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=100, verbose_name="İş Adı")
    description = models.TextField(verbose_name="Açıklama")
    years_of_experience = models.PositiveIntegerField(verbose_name="Yıllık Deneyim") 
    related_projects = models.ManyToManyField('Project', blank=True, verbose_name="İlgili Projeler")  

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Deneyim"
        verbose_name_plural = "Deneyimler"
    
class Education(models.Model):
    institution = models.CharField(max_length=100, verbose_name="Okul Adı")
    degree = models.CharField(max_length=100, verbose_name="Derece")
    field_of_study = models.CharField(max_length=100, verbose_name="Alanı")
    end_date = models.DateField(verbose_name="Bitiş Tarihi")

    def __str__(self):
        return f"{self.institution} - {self.degree} in {self.field_of_study}"
    
    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitimler"
        
class Certificate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Sertifika Adı")
    description = models.TextField(verbose_name="Açıklama")
    date = models.DateField(verbose_name="Verilme Tarihi")
    url = models.URLField(blank=True, verbose_name="Sertifika Linki")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Sertifika"
        verbose_name_plural = "Sertifikalar"
    
    