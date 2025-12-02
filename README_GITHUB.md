# Autonomous Mobile Robot Navigation

[![ROS 2](https://img.shields.io/badge/ROS_2-Humble-blue)](https://docs.ros.org/en/humble/)
[![Gazebo](https://img.shields.io/badge/Gazebo-11-orange)](https://gazebosim.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)

A complete autonomous mobile robot navigation system built with ROS 2, featuring SLAM (Simultaneous Localization and Mapping), path planning, and obstacle avoidance in simulation.

![Robot Navigation Demo](docs/images/demo.gif)

## 📋 Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Package Structure](#package-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **SLAM Mapping**: Real-time map building using SLAM Toolbox
- **Autonomous Navigation**: Goal-based navigation with Nav2 stack
- **Obstacle Avoidance**: Dynamic obstacle detection and avoidance
- **Path Planning**: Global and local path planning
- **Simulation**: Complete Gazebo simulation environment
- **Visualization**: RViz2 integration for real-time monitoring
- **Modular Design**: Clean, well-documented ROS 2 packages

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ROS 2 Humble                         │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Gazebo     │  │ SLAM Toolbox │  │    Nav2      │  │
│  │  Simulation  │  │   Mapping    │  │  Navigation  │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                 │                  │          │
│         └─────────────────┴──────────────────┘          │
│                           │                             │
│                  ┌────────▼────────┐                    │
│                  │   AMR Robot     │                    │
│                  │  - LIDAR Sensor │                    │
│                  │  - Diff Drive   │                    │
│                  │  - Odometry     │                    │
│                  └─────────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

### Components

- **Robot Model**: Differential drive mobile robot with 2D LIDAR
- **Sensors**: 360° LIDAR (12m range), Wheel odometry
- **Localization**: SLAM Toolbox for mapping and localization
- **Navigation**: Nav2 for autonomous navigation
- **Control**: Differential drive controller

## 📦 Prerequisites

- **OS**: Ubuntu 22.04 LTS
- **ROS**: ROS 2 Humble Hawksbill
- **Gazebo**: Gazebo 11
- **Memory**: At least 4GB RAM recommended
- **Storage**: ~2GB for all dependencies

## 🚀 Installation

### 1. Install ROS 2 Humble

If not already installed:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt upgrade
sudo apt install ros-humble-desktop
```

### 2. Clone Repository

```bash
mkdir -p ~/amr_nav_ws/src
cd ~/amr_nav_ws/src
git clone https://github.com/YOUR_USERNAME/amr_nav.git .
```

### 3. Install Dependencies

```bash
cd ~/amr_nav_ws
./install_deps_now.sh
```

Or manually:

```bash
sudo apt update
sudo apt install -y \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-slam-toolbox \
    ros-humble-xacro \
    ros-humble-robot-state-publisher \
    ros-humble-joint-state-publisher-gui \
    ros-humble-rviz2 \
    ros-humble-teleop-twist-keyboard \
    ros-humble-nav2-msgs
```

### 4. Build Workspace

```bash
cd ~/amr_nav_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

Add to `~/.bashrc` for convenience:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source ~/amr_nav_ws/install/setup.bash" >> ~/.bashrc
```

## 🎯 Quick Start

### Test Simulation (Single Terminal)

```bash
ros2 launch amr_bot_gazebo launch_sim.launch.py
```

This launches Gazebo with the robot in a test environment.

### Full SLAM Mapping Demo

You need **4 terminals**:

**Terminal 1 - Gazebo Simulation:**
```bash
ros2 launch amr_bot_gazebo launch_sim.launch.py
```

**Terminal 2 - SLAM Mapping:**
```bash
ros2 launch amr_bot_navigation slam.launch.py
```

**Terminal 3 - RViz Visualization:**
```bash
ros2 launch amr_bot_navigation rviz.launch.py
```

**Terminal 4 - Keyboard Control:**
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Controls

Use these keys in Terminal 4 to drive the robot:

```
   u    i    o
   j    k    l
   m    ,    .

i : forward
, : backward
j : turn left
l : turn right
k : stop
```

Drive around to build the map!

### Save Your Map

```bash
cd ~/amr_nav_ws/src/amr_bot_navigation/maps
ros2 run nav2_map_server map_saver_cli -f my_map
```

## 📖 Usage Guide

### SLAM Mapping

1. Launch all four terminals as shown in Quick Start
2. Use keyboard to drive the robot
3. Watch the map build in RViz
4. Save the map when complete

### Autonomous Navigation (Coming Soon)

1. Load a saved map
2. Set initial pose in RViz (2D Pose Estimate)
3. Set navigation goal (Nav2 Goal)
4. Watch the robot navigate autonomously

## 📁 Package Structure

```
amr_nav_ws/
├── src/
│   ├── amr_bot_description/          # Robot URDF and description
│   │   ├── urdf/
│   │   │   ├── robot.urdf.xacro      # Main robot file
│   │   │   ├── robot_core.xacro      # Chassis and wheels
│   │   │   ├── gazebo_control.xacro  # Gazebo plugins
│   │   │   ├── lidar.xacro           # LIDAR sensor
│   │   │   └── inertial_macros.xacro # Physics properties
│   │   └── launch/
│   │       └── rsp.launch.py         # Robot state publisher
│   │
│   ├── amr_bot_gazebo/               # Simulation environment
│   │   ├── worlds/
│   │   │   └── obstacles.world       # Test world
│   │   └── launch/
│   │       └── launch_sim.launch.py  # Simulation launcher
│   │
│   └── amr_bot_navigation/           # Navigation stack
│       ├── config/
│       │   ├── nav2_params.yaml      # Nav2 configuration
│       │   ├── mapper_params_online_async.yaml  # SLAM config
│       │   └── nav2_default_view.rviz           # RViz setup
│       ├── launch/
│       │   ├── slam.launch.py        # SLAM launcher
│       │   ├── navigation.launch.py  # Nav2 launcher
│       │   └── rviz.launch.py        # RViz launcher
│       ├── maps/                     # Saved maps directory
│       └── scripts/
│           └── send_goal.py          # Programmatic goal sender
│
├── README.md
├── USAGE_GUIDE.md
├── TROUBLESHOOTING.md
├── install_deps_now.sh
└── quick_start.sh
```

## ⚙️ Configuration

### Robot Specifications

- **Type**: Differential Drive
- **Dimensions**: 30cm × 30cm × 15cm
- **Wheel Diameter**: 10cm
- **Wheel Separation**: 35cm
- **Max Linear Velocity**: 0.26 m/s
- **Max Angular Velocity**: 1.0 rad/s

### LIDAR Sensor

- **Type**: 2D Laser Scanner
- **Range**: 0.3m - 12m
- **FOV**: 360°
- **Update Rate**: 10 Hz
- **Samples**: 360

### Key Parameters

Edit `config/nav2_params.yaml` to tune:
- Global/local costmap settings
- Planner parameters
- Controller parameters
- Recovery behavior settings

Edit `config/mapper_params_online_async.yaml` for SLAM tuning:
- Map resolution
- Loop closure settings
- Scan matching parameters

## 🔧 Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solutions.

### Common Issues

**Build fails with missing dependencies:**
```bash
rosdep install --from-paths src --ignore-src -r -y
```

**Robot doesn't move:**
- Check if `/cmd_vel` topic is receiving commands
- Verify Gazebo physics is running

**No map building:**
- Ensure robot is moving (SLAM needs motion)
- Check TF tree: `ros2 run tf2_tools view_frames`

**RViz crashes:**
```bash
rm -rf ~/.rviz2
```

## 🎥 Demo Videos

### SLAM Mapping
![SLAM Demo](docs/images/slam_demo.gif)

### Autonomous Navigation
![Navigation Demo](docs/images/nav_demo.gif)

## 📊 Key Topics

| Topic | Type | Description |
|-------|------|-------------|
| `/scan` | sensor_msgs/LaserScan | LIDAR data |
| `/odom` | nav_msgs/Odometry | Odometry |
| `/map` | nav_msgs/OccupancyGrid | SLAM map |
| `/cmd_vel` | geometry_msgs/Twist | Velocity commands |
| `/tf` | tf2_msgs/TFMessage | Transforms |

## 🛣️ Roadmap

- [x] Basic robot model and simulation
- [x] SLAM mapping implementation
- [x] RViz visualization
- [ ] Full autonomous navigation
- [ ] Multi-goal waypoint navigation
- [ ] Dynamic obstacle handling
- [ ] Real robot deployment documentation
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Srinivas**
- Email: srinivasraovenna1@gmail.com
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- [ROS 2 Navigation Stack](https://navigation.ros.org/)
- [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox)
- [Gazebo Simulator](https://gazebosim.org/)
- ROS 2 Community

## 📚 References

- [Nav2 Documentation](https://navigation.ros.org/)
- [ROS 2 Humble Documentation](https://docs.ros.org/en/humble/)
- [SLAM Toolbox Tutorials](https://github.com/SteveMacenski/slam_toolbox)
- [Gazebo Tutorials](https://classic.gazebosim.org/tutorials)

---

⭐ **Star this repository if you find it helpful!**

**Built with ❤️ using ROS 2**
