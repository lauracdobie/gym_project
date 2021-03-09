# Gym Buddy
Member and fitness class booking management system for a gym.

The brief was for the app to allow the user to: 
- Add/edit members
- Add/edit classes
- Book members onto a class
- Show all upcoming classes
- Show all members booked onto a class.

It also allows the user to: 
- Create class types from which they can select when creating new classes 
- View class types
- Find classes by class type and duration
- View classes that members are booked onto from their member records;
- Find member by name
- Delete classes, class types, members and bookings.

There is error handling and capacity management for classes: members cannot be booked onto classes if they are already booked on, and they cannot be booked onto classes that are full.
Once a member is booked onto a class, the capacity of the class goes down by 1. If a booking is cancelled, the capacity goes up by 1.

Upcoming classes view:
![image](https://user-images.githubusercontent.com/72345316/110353135-9f09c280-802e-11eb-9ebe-afa9c23ce46f.png)

Book a class:

![image](https://user-images.githubusercontent.com/72345316/110352588-0410e880-802e-11eb-82ab-9b7b0bda8d4b.png)

Find classes by duration:

![image](https://user-images.githubusercontent.com/72345316/110354358-fa888000-802f-11eb-8ba9-2ab371551874.png)


# Getting started
Clone the repository and type flask run in the application folder in the Terminal.

![image](https://user-images.githubusercontent.com/72345316/110353513-0cb5ee80-802f-11eb-9a2c-479e847e1d39.png)




