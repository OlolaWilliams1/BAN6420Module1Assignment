class Worker:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate


def main():
    workers = []

    # Sample data for demonstration purposes
    workers_data = [
        {"name": "John", "hours_worked": 40, "hourly_rate": 20},
        {"name": "Alice", "hours_worked": 35, "hourly_rate": 25},
        {"name": "Bob", "hours_worked": 45, "hourly_rate": 18}
    ]

    # Create Worker objects from the data and add them to the workers list
    for data in workers_data:
        worker = Worker(data["name"], data["hours_worked"], data["hourly_rate"])
        workers.append(worker)

    # Calculate payments for each worker and display
    total_payment = 0
    for worker in workers:
        payment = worker.calculate_payment()
        total_payment += payment
        print(f"{worker.name}: ${payment}")

    print(f"Total payment for the week: ${total_payment}")


if __name__ == "__main__":
    main()
class Worker:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate


def generate_workers(num_workers):
    workers = []
    for i in range(num_workers):
        name = f"Worker {i+1}"
        hours_worked = 40  # Assuming all workers work 40 hours per week
        hourly_rate = 20  # Assuming a fixed hourly rate for all workers
        worker = Worker(name, hours_worked, hourly_rate)
        workers.append(worker)
    return workers


def main():
    num_workers = 400
    workers = generate_workers(num_workers)

    total_payment = 0
    for worker in workers:
        payment = worker.calculate_payment()
        total_payment += payment

    print(f"Total payment for the week for {num_workers} workers: ${total_payment}")


if __name__ == "__main__":
    main()
class Worker:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate


def generate_workers(num_workers):
    workers = []
    for i in range(num_workers):
        name = f"Worker {i+1}"
        hours_worked = 40  # Assuming all workers work 40 hours per week
        hourly_rate = 20  # Assuming a fixed hourly rate for all workers
        worker = Worker(name, hours_worked, hourly_rate)
        workers.append(worker)
    return workers


def generate_payment_slips(workers):
    for worker in workers:
        payment = worker.calculate_payment()
        print(f"Payment slip for {worker.name}:")
        print(f"Hours worked: {worker.hours_worked}")
        print(f"Hourly rate: ${worker.hourly_rate}")
        print(f"Total payment: ${payment}")
        print()


def main():
    num_workers = 400
    workers = generate_workers(num_workers)
    generate_payment_slips(workers)


if __name__ == "__main__":
    main()
class Worker:
    def __init__(self, name, hours_worked, hourly_rate, gender):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.gender = gender

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate

    def determine_employee_level(self, payment):
        if 10000 < payment < 20000:
            return "A1"
        elif 7500 < payment < 30000 and self.gender == "female":
            return "A5-F"
        else:
            return "Standard"


def generate_workers(num_workers):
    workers = []
    for i in range(num_workers):
        name = f"Worker {i+1}"
        hours_worked = 40  # Assuming all workers work 40 hours per week
        hourly_rate = 20  # Assuming a fixed hourly rate for all workers
        gender = "male" if i % 2 == 0 else "female"  # Just an example for gender assignment
        worker = Worker(name, hours_worked, hourly_rate, gender)
        workers.append(worker)
    return workers


def generate_payment_slips(workers):
    for worker in workers:
        payment = worker.calculate_payment()
        employee_level = worker.determine_employee_level(payment)
        print(f"Payment slip for {worker.name}:")
        print(f"Hours worked: {worker.hours_worked}")
        print(f"Hourly rate: ${worker.hourly_rate}")
        print(f"Total payment: ${payment}")
        print(f"Employee level: {employee_level}")
        print()


def main():
    num_workers = 400
    workers = generate_workers(num_workers)
    generate_payment_slips(workers)


if __name__ == "__main__":
    main()
class Worker:
    def __init__(self, name, hours_worked, hourly_rate, gender):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.gender = gender

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate

    def determine_employee_level(self, payment):
        if 10000 < payment < 20000:
            return "A1"
        elif 7500 < payment < 30000 and self.gender == "female":
            return "A5-F"
        else:
            return "Standard"


def generate_workers(num_workers):
    workers = []
    for i in range(num_workers):
        name = f"Worker {i+1}"
        hours_worked = 40  # Assuming all workers work 40 hours per week
        hourly_rate = 20  # Assuming a fixed hourly rate for all workers
        gender = "male" if i % 2 == 0 else "female"  # Just an example for gender assignment
        worker = Worker(name, hours_worked, hourly_rate, gender)
        workers.append(worker)
    return workers


def generate_payment_slips(workers):
    for worker in workers:
        try:
            payment = worker.calculate_payment()
            employee_level = worker.determine_employee_level(payment)
            print(f"Payment slip for {worker.name}:")
            print(f"Hours worked: {worker.hours_worked}")
            print(f"Hourly rate: ${worker.hourly_rate}")
            print(f"Total payment: ${payment}")
            print(f"Employee level: {employee_level}")
            print()
        except Exception as e:
            print(f"Error occurred while generating payment slip for {worker.name}: {e}")
            print()


def main():
    num_workers = 400
    try:
        workers = generate_workers(num_workers)
        generate_payment_slips(workers)
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
