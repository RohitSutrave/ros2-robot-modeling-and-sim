import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():
    # 1. Locate the package and the Xacro file
    pkg_share = get_package_share_directory('my_robot_description')
    xacro_file = os.path.join(pkg_share, 'urdf', 'my_robot_macro.urdf.xacro')

    # 2. Use the Command substitution to parse the Xacro file into raw XML dynamically
    # This bypasses the direct command-line execution that is throwing the Python 3.12 error
    robot_description = {'robot_description': Command(['xacro ', xacro_file])}

    # 3. Start the Robot State Publisher (Broadcasts the TF tree)
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen', 
        parameters=[robot_description]
    )

    # 4. Start the Joint State Publisher GUI (Gives you the sliders)
    jsp_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # 5. Start RViz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        rsp_node,
        jsp_gui_node,
        rviz_node
    ])