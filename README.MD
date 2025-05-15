#CMB_Drone_Project

A python-based drone simulation built from the ground up using DroneKit and SITL (Software-In-Loop). This project showcases autonomous flight control, real-time telemetry handling, and virtual drone testing- no physical hardware required.

###Features

- ✅ Connects to a simulated Pixhawk drone using DroneKit-SITL
- ✅ Arms and takes off to a target altitude
- ✅ Displays real-time telemetry (battery, GPS, altitude)
- ✅ Includes a timeout to prevent infinite loops if takeoff fails
- 🛠️ Ready for expansion into full autonomous missions


##  Skills Demonstrated

- Python scripting and control flow
- DroneKit + MAVLink integration
- Real-time data handling and telemetry
- Linux-based development and virtual environments
- Debugging third-party libraries (Python 3.12 compatibility)
- Git and GitHub version control workflows

## Project Structure

CMB_Drone_Project/
├── takeoff_land.py          # Core simulation script
├── venv/                    # Virtual environment (ignored by Git)
├── README.md                # This file
├── .gitignore               # Keeps the repo clean
└── requirements.txt         # Python dependencies

-
## 🚀 Getting Started

### Requirements

- Python 3.10 or newer
- Git
- VS Code or any terminal-based code editor

### Setup Instructions

```bash
# Clone the repository
git clone git@github.com:waycon86/CMB_Drone_Project.git
cd CMB_Drone_Project

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the main drone script
python takeoff_land.py


---

### 🔍 Notes:
- You missed closing the last code block with ` ``` `
- Markdown headers like `#` and `##` must have a space after them (e.g., `# Title`, not `#Title`)
- I added horizontal rules (`---`) to break sections for readability
- Emojis are optional but make it pop!

---

## ✅ Next Step:

Copy this into your `README.md`, **replace everything**, and save.  
Then commit and push it:

```bash
git add README.md
git commit -m "Add polished README with full project details"
git push


