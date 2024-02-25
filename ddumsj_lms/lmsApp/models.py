from django.db import models
from datetime import date
from django.utils import timezone


#  Book model to store book details
class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    author = models.TextField(blank=True, null= True)
    quantity = models.IntegerField(default=1)
    preregistered = models.CharField(max_length=2, choices=(('1', 'YES'), ('0', 'NO')), default=1)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('0','Inactive')), default=1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(f"{self.title} - {self.author}")

# User model for storing users detail info
class User(models.Model):
    Id_number = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20, choices=(('Male','Male'), ('Female', 'Female')), default='Male')
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=250, blank= True, null = True)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(f"{self.Id_number} - {self.first_name}{' '+self.last_name}")


# Librarian model to store a details about a librarian
class Librarian(models.Model):
    pass




# Borrow model to store book borrowing transaction details 
class Borrow(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete= models.CASCADE)
    librarian_id = models.ForeignKey(Librarian, on_delete= models.CASCADE)
    borrowing_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=2, choices=(('1','Pending'), ('0','Returned')), default = 1)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    @property
    def book_name(self):
        return self.book_id.title()
    
    @property
    def user_name(self):
        return self.user_id.first_name()

    def __str__(self):
        return str(f"{self.book_id.book_name} borrowed by {self.user_id.first_name} on {self.issue_date}.")
    



# Dashboard model to show a static a dynamic info with some functionalities
class Dashboard(models.Model):
    pass
