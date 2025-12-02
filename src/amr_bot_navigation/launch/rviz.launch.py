import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Get directories
    amr_bot_navigation_dir = get_package_share_directory('amr_bot_navigation')
    
    # RViz config file
    rviz_config = os.path.join(amr_bot_navigation_dir, 'config', 'nav2_default_view.rviz')
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'
        )
    ])
