# NTD-Name-Typing-Device-
 
This is my attempt at this project. I set out to get my hands on FREE components but then quickly realized this was no easy task. At first I stuck to the templete, but it got boring (quckly). I then put my brain to work and came to the briliant idea of a macropad that types my name. And so the NTD-V1 (Name-Typing-Device) was born.

  
--------------PCB----------------
 
I mostly followed the guide for this but restarted it a few times as my own Ideas came into play.
 
I have an interest studying EE so I really tried to learn from this part. I found it was actually pretty fun, specially when creating the PCB and figuring out the puzzle of connecting the components.
 
I used KICAD as the guide instructed (Though I am new to it so it took quite a while)
 
I first built the guide board to figure it out. With what I learned, and some playing around (And a LOT of google) I slowly came up with my personal design incorporating the XIAO-RP2040, 6 switches, an OLED, and two LEDs (That I kinda forgot to remove so they are now official).
  
<img width="512" height="442" alt="imagen" src="https://github.com/user-attachments/assets/68b0ae94-0a73-40c0-b292-5b54e312664b" />
 
<img width="512" height="442" alt="imagen" src="https://github.com/user-attachments/assets/91d7606f-94e7-4dfc-b9df-3d70d72fdb56" />

   
--------------CAD---------------
 
The guide called for Fusion 360 but im on a low power laptop and have more experience in Onshape, so I designed my Case there.
 
I started with the bottom and designed it with the dimesnions of my pcb and added a hole for the usb-c where I designed it to be.
 
<img width="512" height="442" alt="imagen" src="https://github.com/user-attachments/assets/2bd792a7-dbc7-47ab-84a4-0239ba528158" />
 
After the bottom was completed I designed the top with the key switch layout holes and holes for the Oled and LEDs. I also added some text and made sure the screw holes lined up properlly.
 
<img width="512" height="442" alt="imagen" src="https://github.com/user-attachments/assets/405f67d6-a615-41d0-86ca-7af56b713d03" />
 

 ----------Firmware-----------
 
For programing im mostly clueless, so I had a lot of help from Chat GPT. I honestly have no clue if this works untill it works or spits out a lot of errors.
 
The srcipt is in python, and will be used with CircuitPython and kmk to power the board.
 
Features:
- Inputs from the key switches
- Oled display - welcome message and what has been typed
 
So far this will make it work but there is a lot of room for improvement once I am able to put some actual effort into the code.
  
----------BOM-------------
 
Required Materials:
- Seeed XIAO RP2040 
- MX-Style switches (x6)
- 0.91 inch OLED display
- Blank DSA keycaps (x6)
- SK6812 MINI-E LEDs (x2)
- M3x16mm screws (x4)
- M3x5mx4mm heatset inserts (x4)
- 3D Printed Case