The README.md in the repository root should give a technical overview for other GitHub users and developers
  Brief project description 
In this project our team has build and stabilized a rotating inverted wheel pendulum. We have stabilized the system from rotating 180 degrees upwards with the use of an Arduino microcontroller. The code for our system was partly given and we have added our own personal changes for the goals we wanted to reach this project. 

  Folder explanations
inverted-pendulum-national-team-3/
├─ code/ # Arduino and Python code AND Measurement files (csv, dat, txt)
├─ feedback/ # Internal team/supervisor comments
├─ progress/ # Weekly markdown reports (raw material)
├─ visuals/ # Photos, plots, diagrams, videos
├─ docs/ # Public webpage
│ └─ index.md # Public project documentation (for GitHub Pages)
└─ README.md # Technical repo overview for GitHub users

  Tree output showing structure

  Technical info (how to run Arduino/Python)

  
  Where to find our visuals and data
You can find our graphics the folder 'visuals'.



# Reaction Wheel Inverted Pendulum – Team X
This project was carried out by an international team of students at the
Technische Natuurkunde program (HvA). The objective is to stabilize an
inverted pendulum using a reaction wheel driven by an electric motor.
---
## 1. Project Motivation
(Short explanation for non-technical readers:
why inverted pendulums are interesting, balancing, control theory, etc.)
---
## 2. System Overview
Describe the mechanical and electronic setup.
![Experimental setup](../visuals/setup_photo.jpg)
- Pendulum arm with angle sensor
- Reaction wheel attached to a DC motor
- Arduino (or compatible microcontroller)
- Power electronics and safety features
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
- Student names and universities
- Supervisors
- Collaborating institutions
---
## 9. Repository
Project repository:
- [GitHub: inverted-pendulum-international-team-x](https://github.com/Technische-
Natuurkunde-HvA/inverted-pendulum-international-team-x)
