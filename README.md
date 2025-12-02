# Autonomous Mobile Robot Navigation Project

## Objective
Develop a mobile robot (simulated) that can autonomously navigate in an unknown or semi-known environment using ROS 2, Nav2, SLAM, and Gazebo.

## 🚀 Quick Start

### 1. Install Dependencies (First Time Only)
```bash
sudo ./setup_dependencies.sh
```

### 2. Build the Workspace
```bash
colcon build
source install/setup.bash
```

### 3. Launch the Robot
Use the interactive helper:
```bash
./quick_start.sh
```

Or see **USAGE_GUIDE.md** for detailed instructions.

---

## ✅ Current Status

### Completed Milestones

- [x] **Setup ROS 2 workspace + dependencies + Gazebo simulation environment.**
    - [x] Workspace created (`/home/srinivas/amr_nav_ws`)
    - [x] `amr_bot_description` package created
    - [x] `amr_bot_gazebo` package created
    - [x] `amr_bot_navigation` package created
    - [x] Dependencies installation script
    
- [x] **Create / import a robot model (URDF / XACRO).**
    - [x] Robot base, wheels, sensors (Lidar) defined
    - [x] Gazebo plugins added (diff drive, LIDAR sensor)
    - [x] Inertial properties configured
    - [x] Materials and colors defined
    
- [x] **Gazebo simulation environment.**
    - [x] Custom world with walls and obstacles
    - [x] Launch files for simulation
    - [x] Integration with robot spawner
    
- [x] **SLAM configuration.**
    - [x] SLAM Toolbox parameters configured
    - [x] Launch file for online async SLAM
    
- [x] **Navigation configuration.**
    - [x] Nav2 parameters (costmaps, planners, controllers)
    - [x] Launch files for navigation stack
    
- [x] **Visualization.**
    - [x] RViz2 configuration with all displays
    - [x] Launch file for RViz2

### Ready to Test

- [ ] **Run SLAM in simulation.**
    - Launch Gazebo with robot
    - Run SLAM Toolbox
    - Teleop robot to build map
    
- [ ] **Test localization and robot pose estimation.**
    - Use AMCL or SLAM localization mode
    
- [ ] **Implement navigation.**
    - Send goals via RViz2 or programmatically
    - Verify obstacle avoidance

---

## 📦 Packages

### `amr_bot_description`
Robot URDF/Xacro files, meshes, and robot state publisher.

**Files:**
- `urdf/robot.urdf.xacro` - Main robot definition
- `urdf/robot_core.xacro` - Chassis and wheels
- `urdf/gazebo_control.xacro` - Differential drive plugin
- `urdf/lidar.xacro` - 2D LIDAR sensor
- `urdf/inertial_macros.xacro` - Physics calculations
- `launch/rsp.launch.py` - Robot state publisher

### `amr_bot_gazebo`
Launch files for Gazebo simulation and world files.

**Files:**
- `worlds/obstacles.world` - Simulation environment with walls and obstacles
- `launch/launch_sim.launch.py` - Main simulation launcher

### `amr_bot_navigation`
Nav2 configuration, SLAM configuration, and navigation launch files.

**Files:**
- `config/nav2_params.yaml` - Nav2 stack configuration
- `config/mapper_params_online_async.yaml` - SLAM Toolbox config
- `config/nav2_default_view.rviz` - RViz visualization setup
- `launch/slam.launch.py` - SLAM launcher
- `launch/navigation.launch.py` - Nav2 launcher
- `launch/rviz.launch.py` - RViz launcher
- `scripts/send_goal.py` - Python script to send navigation goals
- `maps/` - Directory for saved maps

---

## 🤖 Robot Specifications

- **Type**: Differential drive mobile robot
- **Dimensions**: 30cm x 30cm x 15cm
- **Wheels**: 2 driven wheels (10cm diameter) + 1 caster
- **Sensors**: 
  - 2D LIDAR (360° coverage, 12m max range, 10 Hz)
  - Wheel odometry (from Gazebo)
- **Control**: Velocity commands via `/cmd_vel` topic

---

## 📚 Documentation

- **USAGE_GUIDE.md** - Complete usage guide with step-by-step instructions
- **quick_start.sh** - Interactive quick-start helper script

---

## 🛠️ Next Steps

1. Complete software installation (run `setup_dependencies.sh`)
2. Build all packages (`colcon build`)
3. Test Gazebo simulation
4. Test SLAM and create a map
5. Test autonomous navigation
6. Fine-tune navigation parameters
7. Extend with additional sensors (camera, IMU)
8. Deploy to real hardware

---

## 📖 Learning Resources

- [Nav2 Documentation](https://navigation.ros.org/)
- [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox)
- [ROS 2 Humble Docs](https://docs.ros.org/en/humble/)
- [Gazebo Documentation](https://gazebosim.org/docs)

---

## 👤 Maintainer

**Name**: Srinivas  
**Email**: srinivasraovenna1@gmail.com  
**ROS Distro**: ROS 2 Humble  
**License**: Apache 2.0

