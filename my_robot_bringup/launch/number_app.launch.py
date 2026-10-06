from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    python_publisher = Node(
        package="my_py_pkg",
        executable="pub_node",
        name="drone_1_pub", # Renames the node at runtime
        parameters=[
            {"confidence_threshold": 0.75},
            {"camera_name": "front_cam"}
        ],
        remappings=[
            ("num", "/swarm/global_telemetry") # (old_topic, new_topic)
        ]
    )
    
    cpp_subscriber = Node(
        package="my_cpp_pkg",
        executable="cpp_sub",
        name="drone_1_sub",
        remappings=[
            ("num", "/swarm/global_telemetry")
        ]
    )
    
    ld.add_action(python_publisher)
    ld.add_action(cpp_subscriber)
    
    return ld
