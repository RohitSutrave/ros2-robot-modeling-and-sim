import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    # 1. Resolve the absolute path to the installed bringup package
    bringup_dir = get_package_share_directory('my_robot_bringup')
    
    # 2. Construct the exact path to the target XML file
    xml_file_path = os.path.join(bringup_dir, 'launch', 'number_app.launch.xml')

    # 3. Create the inclusion action
    include_number_app = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(xml_file_path)
    )

    # 4. Add the action to the launch description
    ld.add_action(include_number_app)

    return ld