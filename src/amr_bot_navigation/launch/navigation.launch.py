import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    
    # Configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    params_file = LaunchConfiguration('params_file', default=os.path.join(
                get_package_share_directory('amr_bot_navigation'), 'config', 'nav2_params.yaml'))
    
    nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/bringup_launch.py']),
            launch_arguments={
                'map': '', 
                'use_sim_time': use_sim_time,
                'params_file': params_file,
                'autostart': 'true',
                'use_composition': 'True',
                'slam': 'False' # We run SLAM separately, but we need to be careful. 
                                # Actually, to avoid conflict, we should use Nav2's SLAM argument if we want both.
                                # But since we have a custom slam.launch.py running, we need to disable AMCL here.
                                # The cleanest way is to NOT launch localization if SLAM is running.
                                # nav2_bringup doesn't have a "no_localization" flag easily exposed except via 'slam'.
            }.items(),
        ),
    ])
