#!/usr/bin/env python3
"""
Simple navigation goal sender for AMR
This script allows you to send navigation goals to the robot programmatically.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
import sys


class NavigationGoalSender(Node):
    def __init__(self):
        super().__init__('navigation_goal_sender')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        
    def send_goal(self, x, y, yaw=0.0):
        """Send a navigation goal to Nav2"""
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.position.z = 0.0
        
        # Convert yaw to quaternion (simple 2D rotation)
        from math import sin, cos
        goal_msg.pose.pose.orientation.x = 0.0
        goal_msg.pose.pose.orientation.y = 0.0
        goal_msg.pose.pose.orientation.z = sin(yaw / 2.0)
        goal_msg.pose.pose.orientation.w = cos(yaw / 2.0)
        
        self.get_logger().info(f'Sending goal: x={x}, y={y}, yaw={yaw}')
        
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        
        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
        
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Goal reached!')
        rclpy.shutdown()
        
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        # Log current distance remaining (optional)
        pass


def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) < 3:
        print("Usage: ros2 run amr_bot_navigation send_goal.py <x> <y> [yaw]")
        print("Example: ros2 run amr_bot_navigation send_goal.py 2.0 3.0 1.57")
        sys.exit(1)
    
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    yaw = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    
    navigation_goal_sender = NavigationGoalSender()
    navigation_goal_sender.send_goal(x, y, yaw)
    
    rclpy.spin(navigation_goal_sender)


if __name__ == '__main__':
    main()
