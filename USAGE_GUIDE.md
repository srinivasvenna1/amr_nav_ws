# Autonomous Mobile Robot Navigation - Complete Guide

## Project Overview
This project implements an autonomous mobile robot with SLAM, localization, and navigation capabilities using ROS 2 Humble, Nav2, SLAM Toolbox, and Gazebo simulation.

## Architecture

### Packages
1. **amr_bot_description**: Robot URDF/XACRO models, sensors, and robot state publisher
2. **amr_bot_gazebo**: Gazebo simulation world and launch files
3. **amr_bot_navigation**: Nav2 configuration, SLAM configuration, and navigation launch files

### Robot Specifications
- **Type**: Differential drive robot
- **Sensors**: 2D LIDAR (360° coverage, 12m range)
- **Wheels**: 2 driven wheels + 1 caster wheel
- **Dimensions**: 0.3m x 0.3m x 0.15m chassis

## Installation & Setup

### Prerequisites
- Ubuntu 22.04
- ROS 2 Humble

### Step 1: Install Dependencies
```bash
cd /home/srinivas/amr_nav_ws
sudo ./setup_dependencies.sh
```

This installs:
- `ros-humble-gazebo-ros-pkgs` - Gazebo-ROS integration
- `ros-humble-navigation2` - Nav2 stack
- `ros-humble-nav2-bringup` - Nav2 launch files
- `ros-humble-slam-toolbox` - SLAM implementation
- `ros-humble-xacro` - URDF/XACRO processing
- `ros-humble-robot-state-publisher` - TF publishing
- `ros-humble-rviz2` - Visualization

### Step 2: Build Workspace
```bash
cd /home/srinivas/amr_nav_ws
colcon build
source install/setup.bash
```

## Usage Guide

### Terminal Setup
You'll need **4 terminals** for a complete navigation session. Source the workspace in each:
```bash
cd /home/srinivas/amr_nav_ws
source install/setup.bash
```

### Option 1: SLAM Mapping Mode (Build a New Map)

#### Terminal 1: Launch Gazebo Simulation
```bash
ros2 launch amr_bot_gazebo launch_sim.launch.py
```
This starts Gazebo with the robot in an environment with walls and obstacles.

#### Terminal 2: Launch SLAM
```bash
ros2 launch amr_bot_navigation slam.launch.py
```
This starts SLAM Toolbox to build the map as you drive the robot.

#### Terminal 3: Launch RViz2
```bash
ros2 launch amr_bot_navigation rviz.launch.py
```
You'll see:
- Robot model
- LIDAR scan data
- Map being built in real-time
- TF frames

#### Terminal 4: Teleoperate the Robot
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
Drive the robot around using keyboard:
- `i` - forward
- `,` - backward
- `j` - rotate left
- `l` - rotate right
- `k` - stop
- `u`, `o`, `m`, `.` - diagonal movements

**Drive around the entire environment to build a complete map!**

#### Save the Map
Once you've explored the environment:
```bash
cd /home/srinivas/amr_nav_ws/src/amr_bot_navigation/maps
ros2 run nav2_map_server map_saver_cli -f my_map
```
This creates `my_map.pgm` and `my_map.yaml`.

---

### Option 2: Navigation Mode (Use Existing Map)

For navigation with an existing map, you would:

#### Terminal 1: Launch Gazebo
```bash
ros2 launch amr_bot_gazebo launch_sim.launch.py
```

#### Terminal 2: Launch Navigation Stack
```bash
ros2 launch amr_bot_navigation navigation.launch.py
```
*Note: Currently configured for SLAM mode. For map-based navigation, edit the launch file to specify your map path.*

#### Terminal 3: Launch RViz2
```bash
ros2 launch amr_bot_navigation rviz.launch.py
```

#### Terminal 4: Set Initial Pose & Navigation Goals
In RViz2:
1. Click **"2D Pose Estimate"** button
2. Click and drag on the map to set robot's initial position
3. Click **"Nav2 Goal"** button
4. Click and drag to set goal position

The robot will autonomously plan a path and navigate to the goal while avoiding obstacles!

---

## Workflow Summary

### Phase 1: Mapping (First Time)
```
1. Launch Gazebo → 2. Launch SLAM → 3. Launch RViz → 4. Teleop to explore → 5. Save map
```

### Phase 2: Navigation (After mapping)
```
1. Launch Gazebo → 2. Launch Nav2 (with map) → 3. Launch RViz → 4. Set pose & goals in RViz
```

---

## Key Topics

| Topic | Type | Description |
|-------|------|-------------|
| `/scan` | sensor_msgs/LaserScan | LIDAR data |
| `/odom` | nav_msgs/Odometry | Odometry from gazebo |
| `/map` | nav_msgs/OccupancyGrid | SLAM-generated map |
| `/cmd_vel` | geometry_msgs/Twist | Velocity commands to robot |
| `/tf` | tf2_msgs/TFMessage | Transform tree |
| `/plan` | nav_msgs/Path | Global path from Nav2 |
| `/local_costmap/costmap` | nav_msgs/OccupancyGrid | Local costmap |
| `/global_costmap/costmap` | nav_msgs/OccupancyGrid | Global costmap |

---

## Configuration Files

### SLAM Configuration
- **File**: `src/amr_bot_navigation/config/mapper_params_online_async.yaml`
- **Key Parameters**:
  - `resolution: 0.05` - Map resolution (5cm per cell)
  - `max_laser_range: 20.0` - Max LIDAR range
  - `minimum_travel_distance: 0.5` - Min distance before updating map
  - `do_loop_closing: true` - Enable loop closure

### Nav2 Configuration
- **File**: `src/amr_bot_navigation/config/nav2_params.yaml`
- **Key Components**:
  - **Controller**: DWB Local Planner (dynamic window approach)
  - **Planner**: NavFn (Dijkstra-based global planner)
  - **Costmaps**: Local (3x3m rolling) and Global
  - **Recovery Behaviors**: Spin, backup, wait

---

## Troubleshooting

### Robot doesn't move in Gazebo
- Check if you published velocity commands: `ros2 topic echo /cmd_vel`
- Verify diff drive plugin loaded: Look for "diff_drive" in Gazebo console

### No LIDAR data in RViz
- Check topic: `ros2 topic echo /scan`
- Verify sensor in Gazebo: You should see red rays from LIDAR
- Check TF tree: `ros2 run tf2_tools view_frames`

### Map not building in SLAM
- Ensure robot is moving (SLAM needs motion)
- Check SLAM params: `ros2 param list /slam_toolbox`
- Verify LIDAR data quality: `ros2 topic hz /scan`

### Navigation not working
- Set initial pose in RViz first (2D Pose Estimate)
- Ensure global costmap has map data
- Check Nav2 lifecycle nodes: `ros2 lifecycle list`

### TF errors
- Verify transform tree: `ros2 run rqt_tf_tree rqt_tf_tree`
- Expected chain: `map → odom → base_link → laser_frame`

---

## Extending the Project

### Add IMU Sensor
1. Add IMU xacro to `amr_bot_description/urdf/`
2. Include in `robot.urdf.xacro`
3. Update sensor fusion in Nav2 config

### Real Hardware Deployment
1. Replace Gazebo launch with hardware drivers
2. Configure `ros2_control` for motor controllers
3. Add real LIDAR driver (e.g., `rplidar_ros`)
4. Calibrate odometry parameters
5. Tune Nav2 parameters for real-world performance

### Add Camera for Visual SLAM
1. Add camera sensor to URDF
2. Integrate `rtabmap_ros` or `ORB_SLAM3`
3. Fuse with LIDAR data

### Multi-Floor Mapping
1. Integrate `slam_toolbox` multi-session mapping
2. Use elevation maps
3. Add 3D costmap layers

---

## File Structure
```
amr_nav_ws/
├── src/
│   ├── amr_bot_description/
│   │   ├── urdf/
│   │   │   ├── robot.urdf.xacro (main robot file)
│   │   │   ├── robot_core.xacro (chassis, wheels)
│   │   │   ├── gazebo_control.xacro (diff drive plugin)
│   │   │   ├── lidar.xacro (LIDAR sensor)
│   │   │   └── inertial_macros.xacro (physics)
│   │   └── launch/
│   │       └── rsp.launch.py (robot state publisher)
│   ├── amr_bot_gazebo/
│   │   ├── worlds/
│   │   │   └── obstacles.world (simulation environment)
│   │   └── launch/
│   │       └── launch_sim.launch.py (Gazebo launcher)
│   └── amr_bot_navigation/
│       ├── config/
│       │   ├── nav2_params.yaml (Nav2 configuration)
│       │   ├── mapper_params_online_async.yaml (SLAM config)
│       │   └── nav2_default_view.rviz (RViz setup)
│       ├── launch/
│       │   ├── slam.launch.py
│       │   ├── navigation.launch.py
│       │   └── rviz.launch.py
│       └── maps/ (saved maps go here)
```

---

## Learning Resources

- **Nav2 Documentation**: https://navigation.ros.org/
- **SLAM Toolbox**: https://github.com/SteveMacenski/slam_toolbox
- **ROS 2 Tutorials**: https://docs.ros.org/en/humble/Tutorials.html
- **Gazebo Tutorials**: https://gazebosim.org/docs

---

## Next Steps

1. ✅ Complete workspace setup
2. ✅ Build all packages
3. ⬜ Test Gazebo simulation
4. ⬜ Test SLAM mapping
5. ⬜ Create and save a map
6. ⬜ Test autonomous navigation
7. ⬜ Tune navigation parameters
8. ⬜ Add advanced features (camera, IMU, etc.)
9. ⬜ Deploy to real hardware

---

## Author & License
- **Project**: Autonomous Mobile Robot Navigation
- **ROS Version**: ROS 2 Humble
- **Maintainer**: srinivas (srinivasraovenna1@gmail.com)
- **License**: Apache 2.0

---

**Happy Navigating! 🤖**
