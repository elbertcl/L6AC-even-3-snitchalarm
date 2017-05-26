<h1>Snitch Alarm: A House Break-In Silent Alarm Using Raspberry Pi 3 </h1>
 
 
 
<center>Group 3</center> <br>
Project Report <br>
 
 
 
 
By:<br>
Elbert Christopher Larosa - 1801442464<br>
Jeremy Jodi - 181443536<br>
Jessy Janlie - 1801443561<br>
 
 
 
COMP6124 - Pervasive Computing<br>
Class 2017<br>
Computer Science Program<br>
BINUS International<br>
Jakarta<br>
Snitch Alarm: A House Break-In Silent Alarm Using Raspberry Pi 3<br>
 
 

 

<h2>PROJECT DESCRIPTION</h2>
Nowadays, the development of pervasive computing is proven to be beneficial in multiple sectors, which includes the security of properties and houses. The current setting is that people generally lock their doors and leave home, hoping that thieves do not attempt to break in their houses. The problem with it is that they are unable to know for a fact whether someone is actually breaking in their home when they are away. With pervasive computing, alarms can be sent to your phone regardless of your location, allowing any break in attempts to be recorded. 
Burglars breaking in houses often get uncaught even when we report them to the police. This is due to several issues such as: we do not know when a burglar breaks in our house immediately, we do not know who opened the room, and crime rates would only increase until houses are equipped with security features which would help the capture of thieves.
Thus, the solution that will be developed in this project is a silent alarm, called as Snitch Alarm,  that is going to be put on a door of the house, such that when a break-in happens, the alarm will give an email to the user notifying that the house's door has been opened. This allows the user to get to be notified of a break-in, even though the house is already locked, wherever the user may be. It is hoped that the Snitch Alarm will be able to tackle the current issue change the setting of the home security; making users able to know for a fact whether there is actually someone breaking into their houses. Further details regarding the features of Snitch Alarm are going to be explained in the How Does It Work? section.
 
 
<h2>COMPONENTS REQUIRED</h2>
The components required for this project are as follows:<br>
Raspberry Pi 3 (1 pc)<br>
Magnetic sensor (1 pc)<br>
Connecting wires (2 pcs)<br>
Breadboard (1 pc)<br>
 
<h2>HOW DOES IT WORK? </h2>
Our program works by sending a notification to the user (house owner) should a stranger enters the house. Moreover, the system can also detect if the user is the one who opens the door, by using Bluetooth sensor detection.
 <br>
First, we programed and compiled all of the required codes in the Raspberry Pi system. The Python code will be explained in detail in the later section. Next, we connect the Raspberry Pi into a Breadboard, which will be connected via cables into the magnetic sensors. The magnetic sensors are then attached to the user’s front house door. Please do keep in mind that the Raspberry Pi need to always be connected to the internet in order to function properly. 
 <br>
Since we assume that the user will always carry their personal smartphone device, if the user’s smartphone Bluetooth is on the parameter with the Raspberry Pi, the system will detect the user as the house owner, thus will not give an alert.
 <br>
On the other hand, if the Raspberry Pi’s Bluetooth sensor does not detect the user’s phone nearby, then it will be more alerted into sensing dangers. Should there be a house break-in, then the moment the unwanted guest opens the front door, the magnets that are attached to the door and a nearby wall will get separated at a large distance from each other. The magnetic sensor then will send a signal to the Raspberry Pi via the cables and the Breadboard. The Raspberry Pi that receives the signal will then immediately send a warning message via email to the user. It will first connect to the SMTP (Simple Mail Transfer Protocol), logs into the mail account with the correct email and password, and directly sends a pre-made email content to the user.
 <br>
From then on, the user can call the local security or his neighbor to help him catch his unwanted visitor and prevents any unwanted case to happen. 
 <br>

 
 

<h2>CIRCUIT DIAGRAM</h2>
Connect the magnetic sensor to the Raspberry Pi as follows:<br>
Pin 8 on the Magnetic Sensor to ground (#6 in our case) on the Raspberry Pi 3.<br>
Pin 10 on the Magnetic Sensor to GPIO18 (#12) on the Raspberry Pi 3.<br>
 

 
 
 

 
 

<h2> INDIVIDUAL WEEKLY PROGRESS: </h2>
<b>Elbert Christopher Larosa - 1801442464</b><br>
Week 1: <br>
In the first meeting, we are asked to think individually of ideas for the final project's topic. Initially, I got the general idea of using a sensor for detecting student coming into the class and thus being able to do absent from that sensor; an idea that is developed from a team that have been assembled together by ourselves at that time. Later on, the idea that I use change as the team is eventually predefined, in which the idea that is actually used is the home break-in silent alarm.
Week 2: <br>
In this week, we focused on initialing our final project, which is by first defining our project’s topic, its current setting (what is the condition or method that is currently applied), the problem with the current setting, and the proposed design to solve the problem. After some discussions and considerations, we decided on this final project:
Topic: House Break-in Silent Alarm
Current Setting:<br>
Nowadays, the development of pervasive computing is proven to be beneficial in multiple sectors, which includes the security of properties and houses. People generally lock their doors and leave home, hoping that thieves do not attempt to break in their houses. With pervasive computing, alarms can be sent to your phone regardless of your location, allowing any break in attempts to be recorded.
Problems and Issues:<br>
Burglars breaking in houses often get uncaught even when we report them to the police. This is due to several issues.
-          We do not know when a burglar breaks in our house immediately.
-          We do not know who opened the room
-          Crime rates would only increase until houses are equipped with security features which would help the capture of thieves.
Design:<br>
The solution that will be developed is a silent alarm that is going to be put on a door of the house, such that when a break-in happens, the alarm will give an email to the user notifying that the house's door has been opened. This allows the user to get the information of a break-in, even though the house is already locked.
We also assigned individual target for ourselves, in which mine was to find the magnetic sensor for the silent alarm.
Week 3: <br>
In this week, we defined our project’s Framework, divided the framework layer’s workload to the team, and summed up the tools what we would need. We decided to use Arduino Uno in this week.
Framework/Architecture:<br>
1. Sensing Layer - The sensing layer enables the retrieval and generation of data from specific conditions received by the sensor. In this project, the sensor used is the magnetic sensor.<br>
2. Gateway Layer - The service layer allows the transfer of data between devices to be processed. For this project, the gateway layer uses a Wireless Local Area Network to send the data<br>
3. Service Layer - The service layer provides services based on the data collected (such as the sensor's input). The service for this project involves an email being sent to the user to notify him that the door has been opened.<br>
Based on the defined architecture, we decided to divide the task into the following layers:<br>
Sensing - Jeremy Jodi<br>
Gateway - Elbert & Jessy<br>
Service - Elbert & Jessy<br>
After researching about our planned project, we have concluded that we will be needing these hardware devices:<br>
Raspberry Pi -> Micro-controller acting as the interface for this project to operate all the necessary functions<br>
Magnetic Sensor -> This magnetic sensor is used to detect whether a door is open or not. (magnet will be detached when the door is open, causing an event)<br>
Wifi Shield -> Used to get the internet connection to send an email to the user<br>
Personally, I have read multiple references regarding how the main interface (which is Arduino Uno) works and the logic behind our final project, which is detecting the door opening. But, we believe that developing the service side of the project should be not too complex, because in the end we only work on the two conditions of whether the door is opening or not.
Week 4:<br>
This week, we made our project’s scenario that will be implemented. Do note that in this week, we actually decided to use Raspberry Pi 3 instead. Here is our project’s scenario:<br>
We are going to develop the House Break-in Silent Alarm by using Raspberry Pi 3 and a magnetic sensor. The magnetic sensor will be plugged to the board with the following configuration. The magnetic sensor will then be placed behind the desired door, which would then be triggered when the door is opened.<br>
In this week, we have been researching more about how to configure our final project. We have also prepared the code to turn on a LED light using Raspberry (our first time learning the Python language), which will be tested in the next meeting. We have also bought the required components/tools for our project.<br>
We have also set target for next week, in which we are going to try to setup the whole environment of our project, having the required components already. It is hoped that we can find the problems earlier so that we can find the solutions for our project's development.
Week 5:<br>
In this week, we searched for a simple python code and have successfully made an LED bulb blinked by using a raspberry pi, thus understanding how it generally works and the connectivity of the cables. We then improve the blinking LED code to make multiple LEDs turned on in the way that we wanted, which is to mimic a traffic light characteristic (as what the attached video shows). We also have bought and gathered tools for our project, such as the magnetic sensor for the door.<br>
We have also set target for next week, which is to try to start working on our project. We will also research more for the technology and procedures. It is hoped that for next week, we will be able to at least get the sensor's signal working.<br>
Week 6: <br>
Regarding this week’s progress, we have successfully configured the whole environment of the project. We tested the magnetic sensor’s functionality and it turned out to be working (as shown by the video, which can be seen on Trello). This shows that both the cable configuration and the codes implemented are correct.<br>
We have set the next week’s target, in which we are going to continue the project’s progress by trying to make the program send an email to the user if the door is opened (when the magnet is disconnected). We have also been researching regarding how to make the program detects if the user is nearby (thus disabling the program’s feature), which is by detecting the user’s phone connectivity to a certain Wi-Fi nearby. We are going to try to implement that feature too for the project, so that the user does not have to get the door opening notification if the user is at home (detected by the user’s phone connection to the home Wi-Fi).<br>
Week 7:<br>
In this week, we worked on our project’s features of sending an email to the user if the door is opened (magnet sensor is separated). We searched for the method and decided to use Gmail SMTP service in order to do the email sending for our micro-controller. We were stuck on this feature of the project, as there was an issue with the email authentication (we have to use our own email), but we do not know regarding how to solve this issue yet (because we have set the correct email address and password). Thus for the next week, we will continue on solving this email sending feature of the project.
Week 8: <br>
In this week, we worked on the email sending feature again and successfully managed to send a notification email through our Gmail for this project (noreply.snitchalarm@gmail.com) by using Python. The last issue of authentication error was solved, without us needing to change much in the codes (so we do not really know why there was an issue, perhaps because of the SMTP setting was too early to be implemented).<br>
Thus, our next task to do is to compile both the door opening detection (by magnetic sensor) and the email sending feature as one Python project file (we cannot do it on this meeting because the required equipment is not available). Then, we will be working on making the project able to detect the user's certain hand phone that is connected through the same Wi-Fi as the Raspberry Pi.
In addition, we have also created our project’s GitHub and pushed the files to our GitHub.<br>
Week 9: <br>
In this week, we have managed to be able to do the phone detection (in order to make the system not notifying the user if the user is at home), which is by detecting the user's hand phone Bluetooth connection to the Raspberry Pi. We decided to use Bluetooth as the phone detection in this project.<br>
For the next step, we need to integrate all the functions of the system together (Bluetooth connection detection, notification email sending, and door opening detection), and to test it with the magnetic sensor.
Week 10: <br>
For this week, we have been compiling all the features of the Snitch Alarm, and it is ready for its full use. Thus for the next week, we will double check the program again, and then focus on making the report and the video documentation for the Snitch Alarm.
Week 11: <br>
In this week, we did some video takes for the final project’s showcase video. We also continue on making the final project’s report. Both progress have been successful and as planned.<br>
 
Problem found and covered during project development: <br>
Week 1: <br>
The problem with finding ideas for the final project is to firstly understanding what does a pervasive project need, and what ideas that are feasible for our current understanding. In addition, we haven't learned Python language too so it makes it harder to understand the idea references at first. But in the end, we got to understand generally and thus able to pick some ideas for the project.
Week 2: <br>
There was no problem because this week was the initializing week of the final project, but there was some doubt on whether we will be able to find the required tools (the magnetic sensor) in Indonesia. We were also having doubts in this week regarding whether we should use Arduino or Raspberry Pi, so we need to do more research regarding the project. 
Week 3: <br>
The difficulty encountered in this week is finding the tools required for the project, because we still do not know which magnetic sensor is the correct one (as there are many types and brands) and whether we even should buy the micro-controller (because we haven’t been told of the micro-controller actually being provided by the class).
Week 4: <br>
There is no significant problem related to the project; the tools needed have been found and bought in this week. There is only a slight issue in understanding the Python language, knowing that it is new for us. We have also covered the last issue by deciding on using the Raspberry Pi 3 instead of Arduino. 
Week 5: <br>
The problem encountered in this week is when we were doing the LED light exercise, because it is our first time working with the tools and the micro-controller. It was quite difficult to understand the cable connectivity and the pins of both the micro-controller and the breadboard (such as why a certain cable needs to be connected to a certain pin).
 
Week 6:<br>
There is no problem encountered in this week because our project’s progress for this week is successful (making the magnetic sensor work).
Week 7: <br>
There is a problem with our email sending feature, which is an authentication error. We are still unable to find why in this week, because we believe that we have set the correct email address and password. Thus, we decided on doing more research and solving this on the next week.
Week 8: <br>
There is no problem encountered in this week because our project’s progress for this week is successful (making the email sending feature work). The last issue with the email sending feature is solved without changing much in the codes (so we do not really know why the issue exists in the first place, perhaps because of the SMTP service being implemented too early after setup).
Week 9: <br>
There is no problem encountered in this week because our project’s progress for this week is successful (making the phone detection work by using Bluetooth).
Week 10: <br>
There is no problem encountered in this week because our project’s progress for this week is successful (integrating all the Snitch Alarm’s features as one Python project).
Week 11: <br>
There is no problem encountered in this week, the video taking is successful and the report’s progress is as planned.
 
<b>Jessy Janlie - 1801443561</b><br>
Week 1: Since this is the first meeting of Pervasive computing, we have been asked to give a thought on what to make for our final project individually. I have been researching and found some really cool internet of things DIY projects, such as IoT bell door, IoT housekeeping, and other interesting projects. After I am assigned to be in a team with Elbert and Jeremy, we have discussed each of our own ideas and decided to make an IoT door project.<br>
Week 2: Currently me and my team are still researching for the references and hardware required to make the silent alarm. We decided to use an Arduino Uno as our processor. As for this week, Elbert and I will start searching for a magnetic sensor component.<br>
Week 3: In this week, we have discussed and finalized our group's concept, which is a house break in silent alarm system - A magnetic sensor placed behind the door would send a trigger, when opened, to the Arduino Uno which would then send an email notification to the user. We researched more about the 3 layers of framework and divided the task amongst the three of us. Also in continuation of last week, we are still searching for the required components. <br>
Week 4: We have been researching more about how to configure our final project and ordered the required components online. We have also prepared the code to turn on a LED light using Raspberry which will be tested next week.<br>
Week 5: We searched for a simple python code and have successfully made an LED bulb blinked by using a raspberry pi. We also have bought and gathered tools for our project, such as the magnetic sensor for door. We will research more regarding our project's technology and procedures. <br>
Week 6: We assembled all of the components that we have gathered and connect them together with the correct cable and pin number. Also, we have tried to code the raspberry pi and it turns out to be working properly. When the magnetic sensor are separated with each other(that will be attached to a door in the future), the raspberry pi will send a correct signal.<br>
Week 7: Now that we know our Raspberry Pi can properly detect signal generated from the magnetic sensor, we move on to sending an email to notify the user that a house break in occurs. We have researched regarding the email last week and are able to implement it this week.<br>
Week 8: We are working on our secondary objective, which is detecting if the user is on the perimeter of the house. This is done via wifi detection, such that if the user connects to the same wifi that raspberry is connected on, it will mean that the user is in the house and no email shall be send. Since this requires a lot of researching to be done, we are taking our time on figuring this out.<br>
Week 9: We are finally able to finish out last project module, i.e. detecting the presence of the owner in the house. We decided to change our procedure from wifi detection to bluetooth detection due to various problems and circumstances.<br>
Week 10: We are officially done with our system. We have compiled all of the required code together and our alarm actually works.<br>
Week 11: Our team decides to end the remaining project tasks this week. We shoot the video during this week's meeting, edited the video and makes the final report.<br>
 
Problem found and covered during project development: <br>
Week 1: The hardest thing to do in this week is to actually research on Pervasive computing in general. Since I am new to this field, I need to research a lot and gain enough knowledge to further proceed in this area. <br>
Week 2: Searching for the magnetic sensor component was a lot harder than we thought it will be. The tutorial that we found online required us to use Samsung magnetic sensor, but we could not find any vendor in Indonesia that sells it. <br>
Week 3: We are really struggling to find the vendors that can supply our project needs in Indonesia. Should we decided to buy the components internationally, then the price will sky rocketed due to international shipping. <br>
Week 4: After discussing amongst our team, we finally ends up to a conclusion to modify our original plan. We decided to change our components to Raspberry Pi and buy a non-branded magnetic sensor. Again, this requires detailed researches.<br> 
Week 5: Configuring the LED light bulbs turns out to be more difficult that we expected it will be. Which cable that are connected to which are a bit confusing. Nevertheless, we are able to successfully configured the LED bulb. <br>
Week 6: This week's progress went off really smooth. We are finally able to keep our hands on our project. The only concern is that the cables keep falling off due to slight movements.<br>
Week 7: We are sometimes not able to send the email notification due to an unknown error. <br>
Week 8: The wifi detection turns out to be a really difficult module. Unknown errors are generated here and there and the program could not execute properly. Also, the wifi in our campus are detected as an insecure connection, which creates an additional problem of internet connection. <br>
Week 9: Through various consultations via online and with our facilitator, we realized that we could not proceed with the wifi detection.<br>
Week 10: We compiled our codes with no problem. But the message that are generated loops itself to quickly, thus producing unnecessary and redundant messages. Nevertheless, we fixed the issue immediately. <br>
Week 11: There are a few problems and debate on how to execute our video, but the problems are minor (such as what we need to do on the scene) and we finished the video taking during the day.<br>
 
 
<b>Jeremy Jodi Widjaja - 1801443536</b><br>
Week 1: On week 1, the group has not been decided, and each of us were tasked to think of an IoT project.<br>
Week 2: This week the group has decided on using Arduino Uno and several add ons to work on our wifi alarm project. The group has decided to work on a silent magnetic door alarm that would send an email to the user. My individual responsibility was to find and purchase the Arduino Uno and PHPoC module.<br>
Topic: House Break-in Silent Alarm<br>
Current Setting:<br>
Nowadays, the development of pervasive computing is proven to be beneficial in multiple sectors, which includes the security of properties and houses. People generally lock their doors and leave home, hoping that thieves do not attempt to break in their houses. With pervasive computing, alarms can be sent to your phone regardless of your location, allowing any break in attempts to be recorded.
Problems and Issues:<br>
Burglars breaking in houses often get uncaught even when we report them to the police. This is due to several issues.
        We do not know when a burglar breaks in our house immediately.<br>
        We do not know who opened the room<br>
        Crime rates would only increase until houses are equipped with security features which would help the capture of thieves.<br>
Design:<br>
The solution that will be developed is a silent alarm that is going to be put on a door of the house, such that when a break-in happens, the alarm will give an email to the user notifying that the house's door has been opened. This allows the user to get the information of a break-in, even though the house is already locked.<br>
Week 3: The group has divided the members to different layers of the architecture. My responsibility is the sensing layer. This week’s goal is to procure all necessary equipments such as wifi shield, Arduino Uno and more.<br>
Week 4: The group decided to move to Raspberry Pi 3 with its built in wifi capability. After further discussion, the group has also decided to borrow the provided equipment, instead of purchasing it.<br>
Week 5: This week the group has worked on a simple LED project using Raspberry Pi 3. Currently the group has understood deeper into BCMs , Raspberry Pi and Python.<br>
Week 6: The core equipment of the planned system has been set up. Currently, the system is able to detect the magnets activity. The system is able to acknowledge a door opening and closing.<br>
Week 7: This week the group has attempted to add the email feature of the system. <br>
Week 8: The email feature is finally complete, together with a new specialized email, noreply.snitchalarm@gmail.com set up for it.<br>
Week 9: The final module of the project is currently being worked on. The group is implementing a wifi detection system to detect the availability of a device on a network. After further discussions, the wifi detection was replaced by bluetooth detection as it is more plausible. <br>
Week 10: All the modules are compiled into one script as the code should work together.<br>
Week 11: This week, the group recorded the video for the project. A classroom was reserved to record the scenes in this video. The video contains details on the technical issues, the scenario and the features of the project.<br>
 
Problem found and covered during project development: 
Week 2: Lack of budget and knowledge in this field lead to unclear planning. <br>
Week 3: The group realised that the total expenses for our project would be very high if all the equipment had to be bought.<br>
Week 4: More research needed to be done as the planned equipment has now changed<br>
Week 5: The system did not work for a very long while due to the wrong setup of the cables. The group has now understood that there is a positive and negative end of the cables.<br>
Week 6: The magnets’ cable is very sensitive and is prone to falling off.<br>
Week 7: There is difficulty in logging in gmail via python script. The group is currently searching answers for this.<br>
Week 8: After further research, and trial and error, the group has deducted that Binus wifi is the source of the problem. The group decided to change to Biznet hotspot to fix the problem.<br>
Week 9: Detecting a phone via wifi required additional libraries such as arpscan or bonjour. Due to the complexity of such additions, the group has decided to take a simpler detection approach, which is bluetooth.<br>
Week 10: The code is now combined into one main script. The only issue was that the code looped itself too quickly, making the system email the user over and over continuously. Issues are fixed already.<br>
Week 11: Lack of equipment to record a proper video. The final video ended up a bit blurry and forced, as acting and video editing is not our domain.<br>
