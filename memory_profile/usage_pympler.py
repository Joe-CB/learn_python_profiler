# The asizeof module provides basic size information for one or several Python objects
# The muppy is used for on-line monitoring of a Python application
# module Class Tracker provides off-line analysis of the lifetime of selected Python objects.
from pympler import asizeof
from pympler import muppy
from pympler import summary
from pympler.classtracker import ClassTracker


def use_asizeof():
    pass

def use_summary():
    allObjects = muppy.get_objects()
    len(allObjects)
    sum = summary.summarize(allObjects)
    summary.print_(sum)
    
class Employee:
   pass

class Factory:
   pass

def create_factory():
   factory = Factory()
   factory.name = "Assembly Line Unlimited"
   factory.employees = []
   return factory

def populate_factory(factory):
   for x in range(1000):
       worker = Employee()
       worker.assigned = factory.name
       factory.employees.append(worker)

# factory = create_factory()
# populate_factory(factory)

def use_tracker():
    factory = create_factory()
    tracker = ClassTracker()
    tracker.track_object(factory)
    tracker.track_class(Employee)
    tracker.create_snapshot()
    populate_factory(factory)
    tracker.create_snapshot()
    tracker.stats.print_summary()

use_tracker()