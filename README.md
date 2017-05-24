# Snitch Alarm

<b>Project Overview</b>

Nowadays, the development of pervasive computing is proven to be beneficial in multiple sectors, which includes the security of properties and houses. The current setting is that people generally lock their doors and leave home, hoping that thieves do not attempt to break in their houses. The problem with it is that they are unable to know for a fact whether someone is actually breaking in their home when they are away. With pervasive computing, alarms can be sent to your phone regardless of your location, allowing any break in attempts to be recorded.

Burglars breaking in houses often get uncaught even when we report them to the police. This is due to several issues such as: we do not know when a burglar breaks in our house immediately, we do not know who opened the room, and crime rates would only increase until houses are equipped with security features which would help the capture of thieves.

Thus, the solution that will be developed in this project is a silent alarm, called as Snitch Alarm,  that is going to be put on a door of the house, such that when a break-in happens, the alarm will give an email to the user notifying that the house's door has been opened. This allows the user to get to be notified of a break-in, even though the house is already locked, wherever the user may be. It is hoped that the Snitch Alarm will be able to tackle the current issue change the setting of the home security; making users able to know for a fact whether there is actually someone breaking into their houses.

<b>How Does Snitch Alarm Work?</b>

Our program works by sending a notification to the user (house owner) should a stranger enters the house. Moreover, the system can also detect if the user is the one who opens the door, by using Bluetooth sensor detection.
 
First, we programed and compiled all of the required codes in the Raspberry Pi system. Next, we connect the Raspberry Pi into a Breadboard, which will be connected via cables into the magnetic sensors. The magnetic sensors are then attached to the user’s front house door. Please do keep in mind that the Raspberry Pi need to always be connected to the internet in order to function properly. 
 
Since we assume that the user will always carry their personal smartphone device, if the user’s smartphone Bluetooth is on the parameter with the Raspberry Pi, the system will detect the user as the house owner, thus will not give an alert.
 
On the other hand, if the Raspberry Pi’s Bluetooth sensor does not detect the user’s phone nearby, then it will be more alerted into sensing dangers. Should there be a house break-in, then the moment the unwanted guest opens the front door, the magnets that are attached to the door and a nearby wall will get separated at a large distance from each other. The magnetic sensor then will send a signal to the Raspberry Pi via the cables and the Breadboard. The Raspberry Pi that receives the signal will then immediately send a warning message via email to the user. It will first connect to the SMTP (Simple Mail Transfer Protocol), logs into the mail account with the correct email and password, and directly sends a pre-made email content to the user.
 
From then on, the user can call the local security or his neighbor to help him catch his unwanted visitor and prevents any unwanted case to happen. 
