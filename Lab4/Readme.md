# Make the robot see
Pratul Tandon, Trevor Morcott, Maria Teresa
​
Build off of Lab 3 from last week. This week's material can be done rather quickly.
​
​
## Prep
​
### For this lab, you will need:
1. Your laptop
2. Pi Camera
​
### Before you come to the lab on Thursday, please do the following:
1. Install VNC viewer from [here](https://www.realvnc.com/en/connect/download/viewer/) if you haven't. 
​
### Deliverables for this lab are: 
​
0. A screenshot of the working VNC viewer with a working image view.
​
1. Answers to the reflection questions in Part D. 
​
### The Report 
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.
​
## Lab Overview
For this assignment, you are going to:
​
A) [Connect your camera](#-a-connect-your-camera)
​
B) [Connect to your Pi (VNC Viewer)](#part-b-connect-to-your-pi-through-vnc-viewer)
​
C) [People Detection](#part-c-people-detection)
​
Labs are due on Tuesdays before class. Make sure this page is linked to on your main class hub page.
​
## Part A. Connect your camera
Plug in the Pi camera to your RPi.
​
## Part B. Connect to your Pi through VNC Viewer
Start VNC Viewer, if prompted to sign in, "select Use VNC without signing in" in the bottom.
​
In the text box "Enter a VNC Server address or search", type in `Your_RPi_IP:1` (e.g. `10.56.131.31:1`).
> When prompted "server not encrypted", click "continue"
<img src="Images/vnc_warning.jpg" width="300">
​
**Password**: `student`
​
You should now log in to your Pi through VNC Viewer.
​
> <img src="Images/vnc.jpg" width="300">
​
Open a terminal, install `libcamera-dev`.
​
```bash
sudo apt install libcamera-dev
```
> <img src="Images/terminal.jpg" width="300">
​
## Part C. People Detection
First, let's test if your camera is working properly. 
```bash
# In a terminal in VNC Viewer
cd
curl -LJO https://raw.githubusercontent.com/FAR-Lab/Mobile_HRI_Lab_Hub/main/Lab4/test_camera.py
python3 test_camera.py
```
**Please include a screenshot of the working VNC viewer with a working image view.**

![IMG_4621](https://user-images.githubusercontent.com/112022260/221882411-b3c506f1-0aa3-437f-957a-3d6a552c385d.jpg)

This exercise is based on this [The Data Frog Tutorial](https://thedatafrog.com/en/articles/human-detection-video/#:~:text=People%20detection,work%20well%20in%20other%20cases.) online. Your CPU will get toasty, so put on a **heat sink**. 
​
```
# In a terminal in VNC Viewer
curl -LJO https://raw.githubusercontent.com/FAR-Lab/Mobile_HRI_Lab_Hub/main/Lab4/people_detection.py
python3 people_detection.py
```
​
Optional: Another example you can try is from [PyTorch](https://pytorch.org/tutorials/intermediate/realtime_rpi.html) (installed already on your system). You will need to write a few lines of code to load the labels yourself. 
​
## Part D. Reflection
​
Reflect on the following questions:
​
1. For your favorite prototyped interaction that you have thought of so far, reflect upon how a camera connected to your Pi could be useful.
​
One of our prototyped interactions was the TrippingBot, a robot that trips near people, so we control for how people react when they see a robot "failing". A camera, in particular a camera with a person detection, would help automatize the system, as people near to be in the surroundings of the robot in order to notice the tripping action and, potentially, feel compeled to intervene. Also, a camera would be a pivotal part of the data collection process - we would collect RGB videos of the interactions and perform an ethnographic analysis.
​
2. What issues do you foresee with this setup? 
​
Image processing is very slow. This would constitute a significant limitation for controlling the robot. Aditionally, as we're planning to run the study "in the wild", rather than a lab environment, variables such as lighting and internet connection will play a role in hindering optimal data collection conditions.
​
3. How is the temperature? How is the speed? How is the connection?
​
Very high temperature, very low speed, good connection but we don't foresee such good connection when running a study.
​
4. How is the view? Would it capture what you might need to see for your prototyped interaction (in question 1)?
​
We were unable to detect people. We will probably need higher processing abilities for out final robot. 
​
Labs are due on Tuesdays before class. Make sure this page is linked to on your main class hub page.
​
### Again, deliverables for this lab are: 
​
0. A screenshot of the working VNC viewer with a working image view
