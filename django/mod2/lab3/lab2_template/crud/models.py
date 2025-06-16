from django.db import models
from django.utils.timezone import now

# > User and Instructor models with One-To-One relationship
# > Course and Lessons models with One-To-Many relationship
# > Course and Instructor with Many-To-Many relationship.
# > Course and Learner with Many-To-Many relationship through Enrollment

# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')

    last_name = models.CharField(null=False, max_length=30, default='doe')

    dob = models.DateField(null=True)


    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name

# Instructor Model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # String method for object string representation
    def __str__(self):
        return "First name: " + self.first_name +       ", " + \
                "Last name: " + self.last_name +   ", " + \
                "Is full time: " + str(self.full_time) +   ", " + \
                "Total Learners: " + str(self.total_learners)

# Learner Model
class Learner(User):
    # occupation choices variables
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'

    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'), # First param: what is saved in the database.
        (DEVELOPER, 'Developer'), # Second param: what is displayed in the gui db django.
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)
    
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " + \
                "Date of birth: " + str(self.dob) + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social link: " + self.social_link
    
# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')

    description = models.CharField(max_length=500)

    # Many-To-Many relationship with Instructors
    instructors = models.ManyToManyField(Instructor)

    # Many-To-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner, through='Enrollment')

    def __str__(self):
        return "Name: " + self.name + "," + \
                 "Description: " + self.description    
    def __str__(self):
        return "Name: " + self.name + "," + \
                 "Description: " + self.description
    
# Enrollment Model
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # One to Many ( Learner to Enrollment )
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)

    # One to Many ( Course to Enrollment )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Enrollment date
    date_enrolled = models.DateField(default=now)
    
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

# Lesson Model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")

    # One to Many ( course to lesson )
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE) # on_delete=models.CASCADE → If the Course is deleted, all related Lessons will also be deleted automatically.

    content = models.TextField()