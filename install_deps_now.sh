#!/bin/bash
# Quick install script for AMR Navigation dependencies

set -e

echo "=========================================="
echo "Installing AMR Navigation Dependencies"
echo "=========================================="
echo ""

# Update package list
echo "Updating package list..."
sudo apt update

echo ""
echo "Installing ROS 2 packages..."
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

echo ""
echo "=========================================="
echo "✅ Dependencies installed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Build workspace:"
echo "   cd /home/srinivas/amr_nav_ws"
echo "   source /opt/ros/humble/setup.bash"
echo "   colcon build --symlink-install"
echo ""
echo "2. Source and run:"
echo "   source install/setup.bash"
echo "   ros2 launch amr_bot_gazebo launch_sim.launch.py"
echo ""
