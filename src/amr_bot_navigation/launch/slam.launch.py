import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    slam_params_file = LaunchConfiguration('slam_params_file', default=os.path.join(
                get_package_share_directory('amr_bot_navigation'), 'config', 'mapper_params_online_async.yaml'))

    slam_launch_file_dir = os.path.join(get_package_share_directory('slam_toolbox'), 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([slam_launch_file_dir, '/online_async_launch.py']),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'slam_params_file': slam_params_file
            }.items(),
        ),
    ])
