#!/bin/bash

echo "======================================"
echo "AMR Navigation - Quick Start"
echo "======================================"
echo ""
echo "This script will help you get started with the autonomous mobile robot navigation."
echo ""
echo "What would you like to do?"
echo ""
echo "1) Build the workspace"
echo "2) Launch SLAM mapping session (4 terminals)"
echo "3) Launch navigation session (4 terminals)"  
echo "4) Test Gazebo only"
echo "5) Save current map"
echo ""
read -p "Enter your choice [1-5]: " choice

case $choice in
    1)
        echo "Building workspace..."
        cd /home/srinivas/amr_nav_ws
        colcon build
        echo ""
        echo "Build complete! Don't forget to source the workspace:"
        echo "  source /home/srinivas/amr_nav_ws/install/setup.bash"
        ;;
    2)
        echo ""
        echo "SLAM Mapping Session Instructions:"
        echo "=================================="
        echo ""
        echo "Open 4 terminals and run the following commands:"
        echo ""
        echo "Terminal 1 - Gazebo Simulation:"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 launch amr_bot_gazebo launch_sim.launch.py"
        echo ""
        echo "Terminal 2 - SLAM:"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 launch amr_bot_navigation slam.launch.py"
        echo ""
        echo "Terminal 3 - RViz2:"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 launch amr_bot_navigation rviz.launch.py"
        echo ""
        echo "Terminal 4 - Teleop (drive the robot):"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 run teleop_twist_keyboard teleop_twist_keyboard"
        echo ""
        echo "Use i,j,k,l keys to drive around and build the map!"
        ;;
    3)
        echo ""
        echo "Navigation Session Instructions:"
        echo "==============================="
        echo ""
        echo "Open 3 terminals and run the following commands:"
        echo ""
        echo "Terminal 1 - Gazebo Simulation:"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 launch amr_bot_gazebo launch_sim.launch.py"
        echo ""
        echo "Terminal 2 - Navigation:"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 launch amr_bot_navigation navigation.launch.py"
        echo ""
        echo "Terminal 3 - RViz2:"
        echo "  cd /home/srinivas/amr_nav_ws"
        echo "  source install/setup.bash"
        echo "  ros2 launch amr_bot_navigation rviz.launch.py"
        echo ""
        echo "In RViz:"
        echo "  1. Set initial pose with '2D Pose Estimate' button"
        echo "  2. Set navigation goal with 'Nav2 Goal' button"
        ;;
    4)
        echo ""
        echo "Launching Gazebo simulation only..."
        cd /home/srinivas/amr_nav_ws
        source install/setup.bash
        ros2 launch amr_bot_gazebo launch_sim.launch.py
        ;;
    5)
        echo ""
        read -p "Enter map name (without extension): " mapname
        cd /home/srinivas/amr_nav_ws/src/amr_bot_navigation/maps
        ros2 run nav2_map_server map_saver_cli -f $mapname
        echo "Map saved as $mapname.pgm and $mapname.yaml"
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        ;;
esac
