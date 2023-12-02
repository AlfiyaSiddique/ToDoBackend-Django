from django.db import models


class Todo(models.Model):
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
    dueDate = models.DateField(blank=True, null=True)
    tag = models.ManyToManyField("Tag", blank=True)
    status = models.CharField(
        max_length=7,
        choices=statusOptions,
        default=Open
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

