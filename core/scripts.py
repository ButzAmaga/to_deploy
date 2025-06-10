from .models import Person

def run():
    people_data = [
        {"first_name": "Alice", "last_name": "Smith", "birth_date": "1990-05-15", "email": "alice@example.com", "phone_number": "1234567890", "address": "123 Street Name"},
        {"first_name": "Bob", "last_name": "Johnson", "birth_date": "1985-10-20", "email": "bob@example.com", "phone_number": "0987654321", "address": "456 Avenue"},
        {"first_name": "Charlie", "last_name": "Brown", "birth_date": "1992-07-08", "email": "charlie@example.com", "phone_number": "1122334455", "address": "789 Boulevard"},
        {"first_name": "Diana", "last_name": "Prince", "birth_date": "1988-11-25", "email": "diana@example.com", "phone_number": "2233445566", "address": "101 Highway"},
        {"first_name": "Ethan", "last_name": "Hunt", "birth_date": "1983-04-17", "email": "ethan@example.com", "phone_number": "3344556677", "address": "202 Main Street"},
        {"first_name": "Fiona", "last_name": "Taylor", "birth_date": "1995-09-03", "email": "fiona@example.com", "phone_number": "4455667788", "address": "303 Oak Lane"},
        {"first_name": "George", "last_name": "Miller", "birth_date": "1989-12-30", "email": "george@example.com", "phone_number": "5566778899", "address": "404 Pine Avenue"},
        {"first_name": "Hannah", "last_name": "Adams", "birth_date": "1991-06-14", "email": "hannah@example.com", "phone_number": "6677889900", "address": "505 Birch Road"},
        {"first_name": "Isaac", "last_name": "Clark", "birth_date": "1994-03-22", "email": "isaac@example.com", "phone_number": "7788990011", "address": "606 Cedar Street"},
        {"first_name": "Julia", "last_name": "Roberts", "birth_date": "1987-08-19", "email": "julia@example.com", "phone_number": "8899001122", "address": "707 Elm Drive"},
    ]

    for data in people_data:
        person = Person.objects.create(**data)
        print(f"Created: {person}")

