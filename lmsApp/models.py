from datetime import timezone
from django.db import models


# Create your models here.

'''
Dashboard (borrowed books, lost books, avaliable books, latest activities)
Book (title, author, published_date, category, subcategory, preregistered, on>
User (school Id number, name, contact, address(DORM),department, borrowing history)
Administrator (roles, permissions)
Borrow (school Id number, department, borrowing history)
Borrowing Transaction (book, user, borrow_date, due_date, return_date)

'''

class Dashboard():
    pass

class Books(models.Model):
    isbn = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    author = models.TextField(blank=True, null= True)
    publisher = models.CharField(max_length=250)
    preregistered = models.CharField(max_length=2, choices=(('1', 'YES'), ('0', 'NO')), default=1)
    date_published = models.DateTimeField()
    status = models.CharField(max_length=2, choices=(('1','Active'), ('0','Inactive')), default=1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "List of Books"

    def __str__(self):
        return str(f"{self.isbn} - {self.title}")


class Users(models.Model):
    code = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True, null= True)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20, choices=(('Male','Male'), ('Female', 'Female')), default='Male')
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=250, blank= True, null = True)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "List of Users"

    def __str__(self):
        return str(f"{self.code} - {self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")

    def name(self):
        return str(f"{self.first_name}{' '+self.middle_name if not self.middle_name == '' else ''} {self.last_name}")


class Admin():
    pass

class Borrow(models.Model):
    user = models.ForeignKey(Users, on_delete= models.CASCADE, related_name="user_id_fk")
    book = models.ForeignKey(Books, on_delete= models.CASCADE, related_name="book_id_fk")
    borrowing_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=2, choices=(('1','Pending'), ('0','Returned')), default = 1)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Borrowing Transactions"

    def __str__(self):
        return str(f"{self.user.code}")

