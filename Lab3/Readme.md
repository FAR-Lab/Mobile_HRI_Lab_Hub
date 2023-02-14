# Make the Robot Move
**List the names and NetID for your partners here.**

In this week's lab, you will lay the foundations for your mobile robot. We will control commercially available hoverboards (Dr. Ju bought these on eBay) with ODrive motor controllers. This week's lab can be challenging. Be prepared to get your hands dirty.


## Prep

Starting with this lab, form a group of 3 to 4 people (doesn't have to be the same group as in previous labs). You will work with the same team until the end of the semester.

### Before Thursday, please watch/read the following video/websites.
[Beginner's Guide on Soldering](https://www.makerspaces.com/how-to-solder/)

[How to Solder Wires Together](https://youtu.be/NSqPHQ1zQco)


### For this lab, you will need:
1.  laptop
2.  strength to take things apart

### For students in Ithaca
Please bring all items I have shipped to you to the robotics lab in Upson. You will need both the raspberry pi and the hoverboards.
- Use the [RPi Imager](https://www.raspberrypi.com/software/) to write [class image](https://drive.google.com/file/d/1PMWyJUoA-CJ73vktrp3nPKiykwzOaauU/view?usp=sharing) to the SD cards (You will need to flash one card per group). [Online Guide](https://howchoo.com/pi/raspberry-pi-imager#write-a-custom-image). Please do this before Thursday's lab.

### Deliverables for this lab are: 
0. a video showing that you can control the hoverboard through python
1. three sketches of potential robots you can build with this platform. Be more realistic and think of these sketches as a potential candidate for your final project. (Look around, what can you automate?)

### The Report 
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above).

## Lab Overview
For this assignment, you are going to:

A) [Setup Raspberry Pi](#part-a-setup-raspberry-pi)

B) [Hardware Setup](#part-b-hardware-setup)

C) [Software Setup](#part-c-software-setup)


Labs are due on Tuesdays before class. Make sure this page is linked to on your main class hub page.

## Lab Safety
- The hoverboard skeleton is conductive. DO NOT PLACE ANY ELECTRONICS ON IT. This includes the ODrive.
- Dangling wire is always dangerous. They can short your circuit in no time. Cover them with electrical tape.
- Be careful with the hoverboard battery. DO NOT LEAVE THE LAB WITH THEN PLUGGED IN. The ODrive will keep draining your battery even if the battery is below its nominal voltage, and your battery can be damaged permanently.
- Unplug the battery before you touch the electronics.

## Part A. Set up raspberry pi
Each team should pick up a raspberry pi (rpi) and a miniTFT display. Plugin the display as shown in the image below. Power the RPIi on with the provided power cable, and the screen should display device mac address after boot.
One member of the team should register the rpi as instructed [here](https://it.cornell.edu/wifi-wired/register-device-doesnt-have-browser).

Reboot the rpi (unplug the power cable and replug it in). Your device should now conencted to RedRover and display ip address.

## Part B. Hardware setup
For students in Ithaca, follow the video [here](https://drive.google.com/file/d/14AAURnUGDazZhO_vaSGaS3nCYTV7YWQE/view?usp=sharing) to take apart your hoverboard.

Take a hex key, and remove the wheel from your hoverboard. Clamp it down on the desk. 

Connect the ODrive with the hoverboard as shown below.

## Part C. Software setup
Now, let's get your motors running. Be prepared, you will run into many problems during this process for sure. Let the TAs know when you run into a problem that cannot be resolved by repreated attemps or unplugging/replugging. 

We are using a motor controller board called ODrive v3.6 for this class. The instructions below are based on a [guide](https://docs.odriverobotics.com/v/0.5.5/hoverboard.html) provided by ODrive. To make your life easier, the teaching staff has already prepared some initial working parameters that you can just load to your ODrive. 

First, ssh to your raspberry pi that connects to the ODrive.
(Only one person needs to do this. Sorry but ODrive cannot be openned on multiple threads.)
```bash
ssh mobilehri@YOUR-IP
```
Say yes if prompted, and password is `student@tech`.
```bash
# Download config file to your RPi
curl 
```

```
# Load the config file to your ODrive
odrivetool restore-config mobilehri_config.json
```

```bash
# in the same terminal
odrivetool
```
This will open an interactive IPython tool that communicates with your odrive board specifically. All commands below should run in this tool.

```

```

Now, let's try to make the wheel moving
```
# set wheel state to close loop control
odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
# set velocity to 2 turns per second
odrv0.axis0.controller.input_vel = 2
# Your motor should spin now
odrv0.axis0.controller.input_vel = 0
# This is important, the hub motors are not designed to have 0 velocity (it will lock the wheels and may start shaking), so we need to change its state to IDLE immediately.
odrv0.axis0.requested_state = AXIS_STATE_IDLE
```

Now, repeat the procedure for the other wheel. Note that you should change all occurance of `axis0` to `axis1`!

### Again, deliverables for this lab are: 
0. a video showing that you can control the hoverboard through python
1. three sketches of potential robots you can build with this platform (what furnitures can you automate?)
