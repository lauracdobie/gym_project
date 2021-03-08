# gym_project
Member and fitness class booking management system for a gym.

The brief was for the app to allow the user to: 
add/edit members
add/edit classes
book members onto a class
show all upcoming classes
show all members booked onto a class.

It also allows the user to: 
create class types from which they can select when creating new classes 
view class types
find classes by class type and duration
view classes that members are booked onto from their member records
find member by name
Delete classes, class types, members and bookings.

There is error handling and capacity management for classes: members cannot be booked onto classes if they are already booked on, and they cannot be booked onto classes that are full.
Once a member is booked onto a class, the capacity of the class goes down by 1. If a booking is cancelled, the capacity goes up by 1.

