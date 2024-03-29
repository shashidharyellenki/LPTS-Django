from django.db import models

# Create your models here.
class StudentCard(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(max_length=100, blank=False)
    bio= models.TextField(max_length=400)
    Years=[
        ('FirstYear','FirstYear'),
        ('SecondYear','SecondYear'),
        ('Alumni','Alumni'),
    ]
    acadamicYear= models.CharField(max_length=20, choices=Years)
    spcs=[
        ('Full Stack Webdevelopment', 'Full Stack Webdevelopment'),
        ('Machine Learning', 'Machine Learning'),
        ('Artifical Intelligence', 'Artifical Intelligence'),
        ('Data Science', 'Data Science'),
        ('Ethical Hacking', 'Ethical Hacking'),
        ('Cloud Computing', 'Cloud Computing'),
    ]
    specalization=models.CharField(max_length=50, choices=spcs)
    RollNumber = models.IntegerField(blank=False)
    Image = models.ImageField(blank=False)

    def __str__(self):
        return self.Name

class course(models.Model):
    studentKey = models.ForeignKey(StudentCard, on_delete=models.DO_NOTHING)
    courseName = models.CharField(max_length=50, blank=False)
    marks = models.IntegerField()
    remarks = models.TextField(max_length=200)
    statusChoicee = [
        ('Complete','Complete'),
        ('Incomplete', 'Incomplete')
    ]
    status = models.CharField(max_length=50, choices=statusChoicee, blank=False)
    courseEnrolledDate = models.DateField(auto_now_add=True)
    courseDuration = models.IntegerField()
    courseTypeChoice=[
        ('SoftSkills', 'SoftSkills'),
        ('TechnicalWriting', 'TechnicalWriting'),
        ('ContinousCredits','ContinousCredits'),
        ('ContinousCredits_ProgrammingContest', 'ContinousCredits_ProgrammingContest'),
        ('ContinousCredits_ProblemSolving', 'ContinousCredits_ProblemSolving'),
    ]
    continousCredits = models.CharField(max_length=50, choices=courseTypeChoice)

    def __str__(self):
        return self.courseName



