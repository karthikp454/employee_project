from django.core.management.base import BaseCommand
from faker import Faker
from random import randint, choice
from datetime import timedelta, date
from employees.models import Department, Employee
from attendance.models import Attendance, Performance


class Command(BaseCommand):
help = "Seed database with fake departments, employees, attendance and performance"


def add_arguments(self, parser):
parser.add_argument("--employees", type=int, default=50)
parser.add_argument("--months", type=int, default=3)


def handle(self, *args, **opts):
fake = Faker()


dept_names = ["HR", "Engineering", "Sales", "Finance", "Marketing", "Support"]
departments = [Department.objects.get_or_create(name=n)[0] for n in dept_names]


employees = []
for _ in range(opts["employees"]):
first = fake.first_name()
last = fake.last_name()
emp = Employee.objects.create(
first_name=first,
last_name=last,
email=f"{first}.{last}{randint(100,999)}@example.com".lower(),
phone=fake.phone_number(),
address=fake.address(),
date_of_joining=fake.date_between(start_date="-3y", end_date="today"),
department=choice(departments),
)
employees.append(emp)


# Attendance for last N months
today = date.today()
start_date = today - timedelta(days=30 * opts["months"])
statuses = [Attendance.PRESENT, Attendance.ABSENT, Attendance.LATE]


bulk_att = []
for emp in employees:
d = start_date
while d <= today:
# weekday only
if d.weekday() < 5:
status = choice([Attendance.PRESENT] * 8 + [Attendance.ABSENT] * 1 + [Attendance.LATE] * 1)
bulk_att.append(Attendance(employee=emp, date=d, status=status))
d += timedelta(days=1)
Attendance.objects.bulk_create(bulk_att, ignore_conflicts=True)


# Performance reviews
bulk_perf = []
for emp in employees:
for _ in range(randint(1, 3)):
bulk_perf.append(Performance(employee=emp, rating=randint(1, 5), review_date=fake.date_between(start_date="-1y", end_date="today")))
Performance.objects.bulk_create(bulk_perf)


self.stdout.write(self.style.SUCCESS("Seeding complete"))