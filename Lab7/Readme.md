# Interact with with people + chatty robot


**List the names and NetID for your partners here.**


In this lab, let's try out some moves with our robots and make them talk!


## Prep
If you haven't finished your robot chassis, try to wrap it up in this lab.


### For this lab, you will need:
1. Your laptop
2. Your hoverbot
3. Speaker (Will arrive later this week, I will make a post when they arrive. I have two for now.)


### Deliverables for this lab are:


1. Before/after sketches of your robot interacting with people
2. A video sketch of your designed interaction
3. Videos trying out elicited interactions
4. Before/after sketch of your robot interacting with people through motion and voice
5. A video sketch of your designed interaction
6. Videos trying out elicited verbal interaction




## Lab Overview
For this assignment, you are going to:

A) [Prototype Speech Interaction](#part-a-prototype-speech-interaction)

B) [Prototype Interaction Routines](#part-b-prototype-interaction-routines)

C) [Test out some interaction](#part-c-test-out-some-interaction)

Labs are due on Tuesdays after Spring break. Make sure this page is linked to your main class hub page.


## Part A. Prototype Speech Interaction

Try out the robot's ability to generate speech:
``` bash
# In a RPi terminal
sudo apt-get install espeak
```

``` bash
# espeak "text-you-want-your-robot-to-say"
espeak "Hello"
espeak "how are you"
```

You can also change the speed and pitch of the voice. Check out the instructions [here](https://espeak.sourceforge.net/commands.html).

## Part B. Prototype Interaction Routines

So far, we only used two joysticks on the controller to give robots moves. We should utilize the other buttons to trigger some pre-defined routines.
I suggest that you modify the script in the [joy_teleop_keymapping package](https://github.com/FAR-Lab/mobilehri2023/blob/main/joy_teleop_keymapping/joy_teleop_keymapping/keymapping_node.py).

Specifically, in the `sendCommand()` function
``` python
def sendCommand(self, msg):
        t = Twist()
        # safety lock, press top left button
        if msg.buttons[4] == 1.0:
            t.linear.x = msg.axes[1] # for some of you, the wheel is spinning too fast, this is also a good place to slow them down.
            # use to represent angular velocity
            t.angular.z = msg.axes[3]
            self.twist_pub.publish(t)
        else:
            t.linear.x = 0.0
            t.angular.z = 0.0
            self.twist_pub.publish(t)
```
Here, we programmed the following logic, 
- if the 4th button is pressed (our safety button), we publish twist commands based on inputs form the first and third axes (the two joysticks).

Feel free to add additional `if-else` conditions to trigger different motion routines! Here is an example of a wiggle behavior (pseudo code).
``` python
import time

...

if wiggle_button_pressed:
      start = time.time() # get current time
      while time.time() <= start + 1: # do the following command for 1 second
          t.linear.x = 0.0
          t.angular.z = variable_depending_on_time
          self.twist_pub.publish(t)
          time.sleep(0.2) # good to pause a little bit in practice
      self.twist_pub.publish(t)
      start = time.time()
      while time.time() <= start + 1: # do the following command for 1 second
          t.linear.x = 0.0
          t.angular.z = variable_depending_on_time
          self.twist_pub.publish(t)
          time.sleep(0.2) # good to pause a little bit in practice
```
## Part C. Test out some interaction!

Based on your final project proposal, sketch out a simple interaction scenario where your robot is interacting (verbally and/or physically) with at least one person. The robot must interact with at least one person. 
1. Scout out the location for the interaction. What are the features and existing activities in the space?
2. Stage the interaction you expect with your robot to go. (Remember to take a video.)
3. Figure out 2-3 interaction triggers that the Wizard will respond to for the interaction. Are there things that need to be done to make it eaiser to spot these triggers? For example, one trigger might be if a person is looking at the robot. Another is if someone is gesturing at the robot.
4. Figure out 2-3 interaction routines that the robot should use for the interaction. For example, maybe the robot  backs up slightly before going forward to signal that its going to go, makes angry noises when it is blocked, or wiggles side to side to indicate confusion

5. Try unscripted interaction with at least 5 people. (Again, remember to take a video; this means you have to get their permission to record them, but not tell them what to do. Please don't shoot creeper videos.) That is, don't tell the people involved in the interaction what to do. Use WoZ to enable the people to see how the interaction would unfold if the robot were autonomous. 
6. Reflection on what you learned about the interaction; revise the interaction sketch with your new insights.

Be mindful of the others around you. Be safe.

### Again, the deliverables for this lab are:


1. Before/after sketches of your robot interacting with people
2. A video sketch of your designed interaction
3. Videos trying out elicited interactions
4. Before/after sketch of your robot interacting with people through motion and voice
5. A video sketch of your designed interaction
6. Videos trying out elicited verbal interaction





