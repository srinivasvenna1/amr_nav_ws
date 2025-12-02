# Troubleshooting Guide - AMR Navigation Project

## Common Issues and Solutions

### 1. Build Errors

#### Issue: "Package not found" during colcon build
**Solution:**
```bash
# Make sure dependencies are installed
sudo ./setup_dependencies.sh

# Update rosdep
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

#### Issue: CMake errors about missing directories
**Solution:**
```bash
# Ensure all directory structures exist
mkdir -p src/amr_bot_navigation/maps
mkdir -p src/amr_bot_navigation/scripts
mkdir -p src/amr_bot_gazebo/worlds
```

---

### 2. Gazebo Issues

#### Issue: Gazebo doesn't start or crashes
**Solution:**
```bash
# Kill any hung Gazebo processes
killall gzserver gzclient

# Try launching again
ros2 launch amr_bot_gazebo launch_sim.launch.py
```

####  Issue: Robot doesn't appear in Gazebo
**Solution:**
```bash
# Check if robot description is published
ros2 topic echo /robot_description --once

# Verify spawner node
ros2 node list | grep spawn
```

#### Issue: Robot falls through the floor
**Solution:**
- Check URDF inertial properties
- Ensure collision geometries are defined
- Verify gz model has proper physics

---

### 3. SLAM Issues

#### Issue: No map being built
**Checklist:**
- [ ] Robot is moving (SLAM needs motion to build map)
- [ ] LIDAR data is being published: `ros2 topic echo /scan`
- [ ] TF transforms are correct: `ros2 run tf2_tools view_frames`
- [ ] SLAM Toolbox node is running: `ros2 node list | grep slam`

**Solution:**
```bash
# Check SLAM params
ros2 param list /slam_toolbox

# Verify scan topic
ros2 topic hz /scan
ros2 topic info /scan

# Check transform tree
ros2 run rqt_tf_tree rqt_tf_tree
```

#### Issue: Map quality is poor
**Solution:**
Tune SLAM parameters in `mapper_params_online_async.yaml`:
- Increase `resolution` for finer maps (but slower)
- Adjust `minimum_travel_distance` and `minimum_travel_heading`
- Enable/tune loop closure parameters

---

### 4. Navigation Issues

#### Issue: Robot doesn't navigate to goal
**Checklist:**
- [ ] Initial pose set in RViz (2D Pose Estimate)
- [ ] Valid map loaded
- [ ] Nav2 lifecycle nodes active
- [ ] Goal is reachable (not in obstacle)

**Solution:**
```bash
# Check Nav2 nodes
ros2 node list

# Check lifecycle state
ros2 lifecycle list /controller_server
ros2 lifecycle list /planner_server

# View planned path
ros2 topic echo /plan

# Check costmaps
ros2 topic echo /global_costmap/costmap --once
ros2 topic echo /local_costmap/costmap --once
```

#### Issue: Robot gets stuck or oscillates
**Solution:**
Tune DWB controller params in `nav2_params.yaml`:
```yaml
FollowPath:
  max_vel_x: 0.26  # Reduce for stability
  min_vel_x: 0.0
  max_vel_theta: 1.0  # Reduce rotation speed
  acc_lim_x: 2.5  # Reduce for smoother motion
```

#### Issue: "No path found" error
**Possible causes:**
- Goal is in obstacle or unknown space
- Robot footprint too large for narrow passages
- Costmap inflation too aggressive

**Solution:**
```yaml
# In nav2_params.yaml
global_costmap:
  global_costmap:
    ros__parameters:
      robot_radius: 0.20  # Reduce if needed
      inflation_radius: 0.45  # Reduce inflation
```

---

### 5. RViz Issues

#### Issue: RViz won't start or crashes
**Solution:**
```bash
# Reset RViz config
rm -rf ~/.rviz2

# Launch with default config
rviz2
```

#### Issue: Can't see robot model in RViz
**Solution:**
- Set Fixed Frame to `map` or `odom`
- Add RobotModel display
- Check that `/robot_description` topic is published:
  ```bash
  ros2 topic echo /robot_description --once
  ```

#### Issue: No map visible in RViz
**Solution:**
- Add Map display
- Set topic to `/map`
- Ensure SLAM or map_server is running
- Check if map is being published:
  ```bash
  ros2 topic hz /map
  ```

---

### 6. TF Transform Issues

#### Issue: "Transform timeout" or "Frame doesn't exist"
**Solution:**
```bash
# View TF tree
ros2 run tf2_tools view_frames
evince frames.pdf

# Expected chain: map → odom → base_link → laser_frame

# Check specific transform
ros2 run tf2_ros tf2_echo map base_link

# List all frames
ros2 topic echo /tf --once
ros2 topic echo /tf_static --once
```

#### Issue: TF tree is broken or incomplete
**Checklist:**
- [ ] robot_state_publisher running
- [ ] SLAM or AMCL publishing map→odom
- [ ] Gazebo publishing odom→base_link

**Solution:**
```bash
# Check which nodes are publishing TF
ros2 run tf2_ros tf2_monitor

# Verify robot_state_publisher
ros2 node info /robot_state_publisher
```

---

### 7. Topic/Communication Issues

#### Issue: No data on expected topics
**Solution:**
```bash
# List all topics
ros2 topic list

# Check topic info
ros2 topic info /scan
ros2 topic info /cmd_vel

# Echo topic to see data
ros2 topic echo /scan
```

#### Issue: Latency or delayed updates
**Solution:**
```bash
# Check topic frequency
ros2 topic hz /scan
ros2 topic hz /odom

# Monitor system resources
htop
```

---

### 8. Package/Dependency Issues

#### Issue: "command not found: ros2"
**Solution:**
```bash
# Source ROS 2
source /opt/ros/humble/setup.bash

# Add to .bashrc for persistence
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

#### Issue: Workspace not sourced
**Solution:**
```bash
cd /home/srinivas/amr_nav_ws
source install/setup.bash

# Add to .bashrc
echo "source /home/srinivas/amr_nav_ws/install/setup.bash" >> ~/.bashrc
```

---

### 9. Simulation Performance Issues

#### Issue: Gazebo runs very slowly
**Solution:**
- Reduce physics update rate in world file
- Decrease sensor update rates
- Close unnecessary applications
- Run Gazebo in headless mode:
  ```bash
  ros2 launch amr_bot_gazebo launch_sim.launch.py gui:=false
  ```

---

### 10. Debugging Tools

#### Essential ROS 2 debugging commands:
```bash
# Node information
ros2 node list
ros2 node info /node_name

# Topic inspection
ros2 topic list
ros2 topic echo /topic_name
ros2 topic hz /topic_name
ros2 topic info /topic_name

# Parameter inspection
ros2 param list /node_name
ros2 param get /node_name parameter_name

# Service inspection
ros2 service list
ros2 service call /service_name service_type "{args}"

# TF debugging
ros2 run tf2_tools view_frames
ros2 run tf2_ros tf2_echo frame1 frame2

# Log messages
ros2 topic echo /rosout

# Launch file testing
ros2 launch --show-args package_name launch_file
```

#### Visualization tools:
```bash
# RQT tools
rqt_graph  # Node graph
rqt_tf_tree  # TF tree
rqt_console  # Log viewer
rqt_plot  # Real-time plotting

# RViz TF visualization
rviz2
```

---

## Getting Help

If you're still stuck:

1. **Check the logs:**
   ```bash
   cd /home/srinivas/amr_nav_ws
   cat log/latest_build/*/stderr.log
   ```

2. **Enable debug logging:**
   ```bash
   ros2 launch amr_bot_gazebo launch_sim.launch.py --ros-args --log-level debug
   ```

3. **Community Resources:**
   - [ROS Answers](https://answers.ros.org/)
   - [Nav2 GitHub Issues](https://github.com/ros-planning/navigation2/issues)
   - [ROS Discourse](https://discourse.ros.org/)
   - [Gazebo Community](https://community.gazebosim.org/)

4. **Documentation:**
   - [Nav2 Documentation](https://navigation.ros.org/)
   - [ROS 2 Humble Docs](https://docs.ros.org/en/humble/)
   - [SLAM Toolbox Wiki](https://github.com/SteveMacenski/slam_toolbox)

---

**Note:** Most issues can be resolved by:
1. Sourcing the workspace properly
2. Checking that all nodes are running
3. Verifying TF transforms
4. Ensuring topics are publishing data
