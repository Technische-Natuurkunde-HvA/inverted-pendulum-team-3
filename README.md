  Tree output showing structure

  Technical info (how to run Arduino/Python)

  
  Where to find our visuals and data
You can find our graphics the folder 'visuals'.



# Brfief project description – Team 3
Brief project description 
Students from Applied Physics at the HvA in the Netherlands have build and stabilized a rotating inverted wheel pendulum. The team has stabilized the system by using an electric driven motor controlled by an Arduino microcontroller. The code for our system was partly given and we have added our own personal changes for the goals we wanted to reach this project. 
---
## Folder explanations
inverted-pendulum-national-team-3/
├─ code/ # Arduino and Python code AND Measurement files (csv, dat, txt)
├─ feedback/ # Internal team/supervisor comments
├─ progress/ # Weekly markdown reports (raw material)
├─ visuals/ # Photos, plots, diagrams, videos
├─ docs/ # Public webpage
│ └─ index.md # Public project documentation (for GitHub Pages)
└─ README.md # Technical repo overview for GitHub users

## 1. Project Motivation AFMAKEN
Inverted pendulums are very wildly used in society and an important factor in our daily life. It's a system that balances and uses control theory... 

---
## 2. System Overview LINK
Our mechanical setup is designed by a partner institution from Portugal. They've designed a 3D printed pendulum holder wich fits the elctrical part of our setiup perfectly. We've designed our own flywheel with the use of Tinkercad and Autodesk Fusion 360 wich we've also 3D printed. Our electrical setup contains an JGA25-370 12V DC motor with an encoder with 24V. We've used AS5600 angle sensor wich measures the angle of our motor. Describe the mechanical and electronic setup.
![Experimental setup](../visuals/setup_photo.jpg)

---
## 3. Control Principle
Explain in words first (for non-technical people), then more mathematically
(for technical readers).
- The pendulum is naturally unstable in the upright position.
- By accelerating or braking the reaction wheel, we generate torque.
- The controller reads the angle and angular velocity and chooses the motor
command.
(You can show block diagrams as images from `visuals/`.)
![Control block diagram](../visuals/control_block_diagram.png)
---
## 4. Implementation
GitHubPagesTutorial-v4.md 2025-12-09
3 / 9
### 4.1 Arduino Control Software (folder `code/`)
Explain:
- Main control loop frequency (e.g., 100 Hz)
- Which `.ino` file is the main entry point
- How sensor readings and motor outputs are handled
### 4.2 Python Tools (also in `code/`)
Explain:
- Reading measurement files from `data/`
- Generating plots saved into `visuals/`
- Any analysis (e.g., identification, performance metrics)
---
## 5. Experiments and Data
Link to measurement files in `data/`:
- [Step response data](../data/step_response.csv)
- [Stabilization log](../data/stabilization_run1.csv)
Include images created from those data:
![Angle over time](../visuals/angle_vs_time.png)
If you have videos in `visuals/`:
- [Watch the pendulum balancing](../visuals/stabilization_demo.mp4)
Or link to YouTube, if you prefer.
---
## 6. Results
Summarize:
- Did the pendulum stabilize?
- Typical settling time
- Sensitivity to disturbances
- Limitations of the design
Include relevant plots:
![Control effort over time](../visuals/control_effort.png)
---
## 7. Project Timeline (from `/progress`)
GitHubPagesTutorial-v4.md 2025-12-09
4 / 9
Explain that the weekly reports in `progress/` document the evolution.
Optionally link to them:
- [Week 1 report](../progress/week01.md)
- [Week 2 report](../progress/week02.md)
- ...
---
## 8. Team and Credits
- Joran Stavenuiter
- Onno Dijkman
- Fleur van Essen
- Rinus Appelman
- Floris de Weerd
- Luka Marcé
- Youssef El Bouhassa
- Hogeschool van Amsterdam
---
## 9. Repository LINK MAKEN
Project repository:
- [GitHub: inverted-pendulum-international-team-x](https://github.com/Technische-
Natuurkunde-HvA/inverted-pendulum-international-team-x)

