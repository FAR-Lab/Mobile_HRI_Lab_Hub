# Interaction First
\*\***List the names and NetID for your partners here.**\*\*

In this lab, you will modify a robotic creature (ConeBot) that is originally designed by [Dr. Rei Lee](https://infosci.cornell.edu/~reilee/), a friend of our lab. The [ConeBot](https://infosci.cornell.edu/~reilee/ConeBot/) is a shy robot that hides under a small traffic cone. It is adventuring the world by itself but hopes people don't notice it at all.

Today, you will work with a close relative of ConeBot, CloneBot. Though closely related, CloneBot's personality (robotality?) is quite the opposite of ConeBot. It is outgoing and loves to hangout with people. You will work with CloneBot and design its legendary adventure. 

This lab uses Wizard of Oz prototyping--that is, the Wizard (that is you) controls the robot and gives it the intelligence it does not have it. The point of Wizard of Oz prototyping is to gather data about how people will respond to an intelligent robot, so that you have the information you need to design the robot well.

## Prep
For this week's lab (and also the following week), you will work in groups of 3.

### For this lab, you will need:
1. Smart Phone (Laptop or Tablets also work) -- The main required feature is that the phone needs to connect to WiFi and display a webpage.
2. To work in a group of 3 (encouraged) or 4 people (if necessary).

\*\***^^^ List the names and NetID for your partners above. ^^^**\*\*

### Update your personal lab repo
1.  Log in to your github, go to `YourGithubUsername/Mobile_HRI_Lab_Hub/`. 
2.  Click "Sync fork" -> "Update branch"
<img src="https://user-images.githubusercontent.com/20778137/216361417-48d0e8b6-2d21-46e0-869c-b8aa801dfed4.png" width="600">
3. Now your Lab Hub should be updated with the latest lab.


## Lab Overview
For this assignment, you are going to:

A) [Build Your Clonebot](#part-a-build-your-clonebot)

B) [Plan](#part-b-plan) 

C) [Act out the interaction](#part-c-act-out-the-interaction) 

### Deliverables for this lab are: 
1. 5 Storyboards
2. Any reflections you have on the process
3. Video sketch of 3 prototyped interactions (selected from the 5 storyboards)
4. Submit the items above in the Lab1 folder of your class [Github page], either as links or uploaded files. **Each group member should have the updated lab page linked to their own Lab Hub.** Better yet, you could replicate the data in your own repo so that you don't lose anything if your partner modifies or deletes their files later.

### The Report
Just as you copied your Lab 0/Readme.md, create a new file "NetID_Readme.md" under your Lab 1 folder. Leave the original "Readme.md" intact.
This NetID_Readme.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

Each group member must submit their own submission, even if most of the material is identical to their group members. Upload the link to your "NetID_Readme.md" to Canvas. 

Labs are due on Tuesdays before class. 

## Part A. Build Your Clonebot
Form your 3-4 person team.

Follow the instructions [here](https://cornell.box.com/s/i0ykqbfz3y1fj195jax0s28v1n1vsx4o) to build your robot!
The instructions are arranged in stages. At the beginning of each stage, each group must select one (and only one) representitive to pick up parts from us. 

After you finish your robot, plug in power from the USB battery pack. Follow the instructions below to connect to your robot.
1. Connect to WiFi "MobileHRI-x", where x is the number assigned to the ESP-32. (ESP-32 should flash once.)
2. Open a brower, in the address line, type in 192.168.4.1
3. You should be see a control interface. Try out different buttons and see what they do.

## Part B. Plan 

To stage an interaction with your CloneBot, think about:

_Setting:_ Where is this interaction happening? (e.g., an office, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? Reflect on the design of current day home mobile robots like Roomba. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., picking up a pen, opening the fridge). 

Leverage the possible motions of Clonebot and the extra degree of freedom provided by the motor on the top.

\*\***Describe your setting, players, activity and goals here.**\*\*

_Use case 1_:

_Setting_: At home
_Player_: Pet and its owner who is away from home
_Activity_: The owner controls the robot remotely to play with his/her pet. The owner can also see visuals through the camera.
_Goal_: The owner's goal is to 1) keep their pet company while away and 2) check on their pet in case they miss them. The pet's goal is to have a good time with the robot.

_Use case 2_:

_Setting_: In schools
_Player_: Visitors, new students, and delivery persons who are not familiar with the campus
_Activity_: The player says the destination they want to go, and the robot guides him/her to it.
_Goal_: The player's goal is to get to the right place on time.

_Use case 3_:

_Setting_: In classroom at school, during exams
_Player_: Students and invigilator
_Activity_: The robot patrols the classroom while an invigilator could see the visuals remotely. The robot has automatic detection for behaviors like talking to each other, checking the phone, etc. and alerts the invigilator. The invigilator can sit at the front and keep an eye on the video stream while doing his/her own things.
_Goal_: The invigilator's goal is to surveil the students to make sure there's no bad behaviors. The student's goal is to take the exam without disturbance.

_Use case 4_:

_Setting_: Places that is not possible or safe human to be at: caves, outer space, ocean, etc.
_Player_: Exploers and scientists
_Activity_: The player controls the robot to enter the place of interest in order to take a look of the place.
_Goal_: To get a better understanding of the space of interest through the visuals.

_Use case 5_:

_Setting_: At home
_Player_: Homeowners who do not want to or cannot move
_Activity_: The players control the robot to answer doors, communicate with delivery people and pick up items to them.
_Goal_: Homeowners' goal is to get items without having to move their body and accomplish simple communication tasks.


Storyboards are a tool for visually exploring a users interaction with a device. They are a fast and cheap method to understand user flow, and iterate on a design before attempting to build on it. Take some time to read through this explanation of [storyboarding in UX design](https://www.smashingmagazine.com/2017/10/storyboarding-ux-design/). Sketch five storyboards of the interactions you are planning. **It does not need to be perfect**, but must get across the behavior of the CloneBot and the other characters in the scene. 

\*\***Include pictures of your storyboards here**\*\*

Link:
https://docs.google.com/document/d/17_B_EzBEC6lp-5RPfNYxuCCtZvjYASexyDrNGiEbp7Q/edit?usp=sharing




## Part C. Act out the Interaction

Select 3 of the 5 storyboards to act out. Try physically enacting the 3 interactions you planned with your teammates. (Do not plug in the CloneBot just yet.) Record these video clips, and submit them (Unlisted Youtube links are fine).


_Videos_:

Use case1:
https://drive.google.com/file/d/1F8sMr5htCPk4xVg99TM50tx2pCz_gfKN/view?usp=sharing

Use case2:
https://drive.google.com/file/d/17TqXYzYSduIziOHSbQt4cW7uL3EJppus/view?usp=sharing

Use case3:
https://drive.google.com/file/d/13mHQ5K-q4wpH6TpU1VnJylcsGFRh8ao-/view?usp=sharing


\*\***Are there things that seemed better on paper than acted out?**\*\*
Yes. In usecase 3, we felt like that the robot need to be more robust in traveling through desks and stairs to supervise students in real life.


\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*
Yes, a new idea poped out of our heads while acting out usecase 3. We imaged a usecase where the robot can act as waiters in restaurants. It can deliver plates to the customers, take empty plates from customers and bring customers to their seats, etc.


\*\***Other reflections**\*\*
During the acting, we thought it would be a great idea to add an audio sensor to the Robot to enhance its interacting ability. Many of our planned use cases benefits from the camera for providing visual feedback. Adding an audio sensor could take the interations to a next level. Besides, it was really fun playing with the extra degree of freedom provided by the motor on the top.


## Your Weekly Dose of ROS

We are not quite finished with the lab from last week.

As I mention, ROS is managed through packages. We have this crazy file structure that looks like a python package but haven't really made a package.
In the last bit of today's lab, let's actually build our package.

Go back to the construct website and log in to your previous Rosject.

In your code editor, open the file `mobilehri_ws/src/my_package/setup.py`.

Replace what's inside with the following code snippet.

```python
from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_package.hri_publisher:main',       # NEW!
            'listener = my_package.hri_subscriber:main',    # NEW!
        ],
    },
)

```

By adding entry points that linked to the main functions in our hri_publisher and hri_subscriber files, we basically create shortcuts for ROS to call our script in Terminal. 

Now, let's build our package. Open a terminal:
``` bash
cd ~/mobilehri_ws/
colcon build          # ignore the warning/err about setup.py being deprecated.
source install/setup.bash
```

Remember that we need to source ROS every time? In order to use your customized ROS packages, you must source them individually as well! To do so, source the setup.bash file within `workspace/install`.

Now, you can call your scripts through ROS the following way:

```bash
# In terminal 1
cd ~/mobilehri_ws/
source install/setup.bash
ros2 run my_package talker
```

```bash
# In terminal 2
cd ~/mobilehri_ws/
source install/setup.bash
ros2 run my_package listener
```

You may notice that the listener does not receive messages published before it is created. As Wendy mentioned in class, the messaging system established through publishers and subscribers are not reliable. They are in fact asynchronous. Publishers are unaware of the subscribers existence. 

To have a more reliable interaction, you will need a new type of mechanism called service and client. We will talk more about this later. 
