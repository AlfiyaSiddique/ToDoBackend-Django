from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Todo(models.Model):   # Todo Model

    def no_future(value):
        today = date.today()
        if value < today:
            raise ValidationError('Due Date cannot be in the past.')

    Open = "Open"
    Working = "Working"
    Done = "Done"
    Overdue = "Overdue"
    statusOptions = [
        (Open, "Open"),
        (Working, "Working"),
        (Done, "Done"),
        (Overdue, "Overdue")
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    dueDate = models.DateField(
        blank=True, null=True,
        validators=[no_future],
    )  # Checks for past date
    tag = models.ManyToManyField("Tag", blank=True)
    status = models.CharField(
        max_length=7,
        choices=statusOptions,
        default=Open
    )

    def __str__(self):
        return self.title


class Tag(models.Model):  # Tag Model
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name