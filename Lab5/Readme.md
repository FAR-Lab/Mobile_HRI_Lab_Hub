# Give the robot moves
**List the names and NetID for your partners here.**

Now, let's controll over robot through some more intuitive ways. 

As you can see, it's pretty easy to control the wheels with python! However, it's not easy for us as humans to command a robot while thinking in terms of individual wheel velocity. If you are a gamer, you might be pretty familiar with controlling avatars with joystick controllers or keyboard keys (WASD). In today's lab, let's map joystick controller commands to wheel velocities in python.

## Prep

### For this lab, you will need:
1. Your Computer
2. Joystick Controller
3. Your set of hoverboard + ODrive

### Deliverables for this lab are: 

0. Fill in the questions along the way! 
1. 1 photo of costumed device
2. Reflections on the process
3. Video sketch of 1 prototyped interactions with costumed device
4. Submit the items above in the lab2 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report 
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Connect Joystick Controller to RPi](#part-a-connect-joystick-controller-to-RPi)

B) [Read Messages from Joystick](#part-b-read-messages-from-Joystick)

C) [Map buttons to control](#part-c-map-buttons-to-control)

D) [Try it with your hoverboard!](#part-d-try-it-with-your-hoverboard!) 

Labs are due on Tuesdays before class. Make sure this page is linked to on your main class hub page.

## Part A. Connect Joystick Controller to RPi
Our wireless joystick controller connets to RPi through Bluetooth. If you are an old school terminal person, you can register your joystick through command line via `bluetoothctl`([tutorial](https://www.makeuseof.com/manage-bluetooth-linux-with-bluetoothctl/)).

It is much easier to pair a bluetooth device in VNC viewer. 
1. login to VNC viewer.
2. Setup bluetooth. Open a terminal on your RPi.
```bash
sudo apt install bluez bluez-tools 
sudo apt install blueman
```

## Part B. Read Messages from Joystick

## Part C. Map buttons to control

## Part D. Try it with your hoverboard!


### Again, deliverables for this lab are: 

0. Fill in the questions along the way! 
1. photos of costumed robots
2. Reflections on the process
3. Video sketch of 1 prototyped interactions with the costumed device
4. Submit the items above in the lab2 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.
