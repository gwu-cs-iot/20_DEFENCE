# A DEFENCE: Armband DronE For EmergeNCiEs

## Summary
The goal of this project is to enable a user experiencing a medical emergency to contact our drone system (and by extension emergency services) to receive assistance. This would entail the end-user, using our glove that provides motion control and communication, hitting a button to start the drone launch procedure. The drone would automatically fly to the user’s location using GPS, at which point the motion control system on the glove would kick in and allow the user to control the drone. The user would be receiving instructions from a trained medical professional who is communicating with the user via a speaker and camera onboard the drone.

## Security
We plan to use encryption and strict authentication to ensure the system cannot be compromised by malicious actors.

## Components
- Control System (Lead: Henry // Ast: Pat)
    - Program for EMS to control the drone. They’ll see visual output from the drone, and have telepresence capabilities
    - This will integrate with the cloud
    - Parts
        - Laptop
- Drone System (Lead: Pat // Ast: Gregor)
    - The base for this is a DJI Tello, a programmable drone. It can be controlled via Python
    - The drone will carry a payload of a microcontroller (Raspberry Pi) to enable GPS tracking and speaker output
    - Parts
        - Drone control program
        - Raspberry Pi Zero W to enable speaker and GPS
        - Speaker unit
        - GPS unit
- Armband System (Lead: Gregor // Ast: Henry)
    - This will be worn by the end-user. It provides gesture control for the drone and has GPS tracking to allow the drone to reach its destination
    - Parts
        - Gesture Controller
        - Microcontroller
        - GPS
        - Button

## Communication
- Cloud <=> Control System [REST APIs]
- Control System <=> Drone System [Software Defined Radio]
- Drone System <=> Armband System [Drone WiFi Network]

## Timeline
### 2/20: Checkpoint 1
- Hardware should be ordered/shipping
- Control System
    - Will have a program that boots up and shows mock video
    - Will have buttons
    - Will have audio input
- Drone System
      - Will have sketch of what the code will look like
      - SDR prototype will be tested
- Armband System
    - Sketch of gestures will be available
    - The feasibility of Kai will be investigated
    - WiFi coms will be tested

### 3/24: Checkpoint II
- Hardware should be assembled
- Control System
    - Will have streaming video from drone
    - Will be able to send sound to drone
- Drone System
    - Will be able to fly programmatically,
    - Can signal it is receiving gestures
    - Will be sending video back to control system
- Armband System
    - Will recognize gestures
    - Will send gesture data to drone
    - Will have a button

### Parts
- 1x Drone
    - $89: 1x Tello
        - (https://smile.amazon.com/dp/B07BDHJJTH)
- 1x Glove
    - $0: Pat’s Glove (already owned)
- 1x Gesture Armband
    - $70 ($150 w/o sale): 1x Kai
        - (https://store.vicara.co/products/valentines-sale-kai-gesture-controller)
- 2x Microcontroller
    - $0: 2x Raspberry Pi W (already owned)
- 2x Battery Power Supply
    - $20 @ 2x $10 LiPo
        - (https://www.adafruit.com/product/258)
- 2x LiPo Convertor
    - $30 @ 2x $15
        - (https://www.adafruit.com/product/2030)
- 1x Battery Charger
    - $6: LiPo Charger
        - (https://www.adafruit.com/product/1304)
    - $7: Cables
        - (https://smile.amazon.com/dp/B014A1K46Y)
- 1x Speaker
    - $2: Mini Metal Speaker
        - (https://www.adafruit.com/product/1890)
    - $4: 2.5w Amp
        - (https://www.adafruit.com/product/2130)
- 2x SDR
    - $0: Gregor’s Hardware (already owned)
- 2x GPS Unit
    - $28 @ 2x $14 GPS
        - (https://smile.amazon.com/dp/B07P8YMVNT/)

### Total Cost Analysis
89 + 70 + 20 + 30 + 6 +7 + 2 + 4 + 28 =  256

### Risks
- Drone has short battery life
    - Problem: We’re putting a payload on the drone. This should work, there is prior art, and we’re under the weight budget. However, the extra burden will affect battery life, which is already only 20 minutes. This is probably fine for our demo at the end (5 minutes), but will make development harder
    - Mitigation: Get the more expensive “boost combo” drone package, which comes with extra batteries
- Kai Dev Kit slightly mysterious
    - Problem: We are opting for the normal Kai, which is cheaper than the dev kit. Our hope is that we can just map the gestures to keyboard inputs somehow. This may be sketchy, however, since Kai does not explicitly support linux: just Windows and OS X.
    - Mitigation: Get for the more expensive Kai Dev Kit (https://store.vicara.co/products/kai-developer-edition)
- Weight and battery restrictions unclear
    - Problem: We have tried our best to make the weight and battery specs reasonable, but we don’t have a high degree of assurance that our decisions are perfect/flawless.
    - Mitigation: No mitigation possible, we just need to be careful
- Speaker quality
    - Problem: The speaker may be too low quality for human voice to be understandable. This would hurt our application.
    - Mitigation: Buy a more expensive speaker to start with, or consider upgrading afterwards
