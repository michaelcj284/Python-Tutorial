class Employee():
    def do_work(self):
        print("I'm working!")
    
class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video looks fun!")
    
class Director(Manager):
    def fire_employee(self):
        print("You're fired!")


m = Manager()
d = Director()

print(m.do_work())
print(m.waste_time())
print(d.waste_time())
print(d.fire_employee())
print(d.do_work())
