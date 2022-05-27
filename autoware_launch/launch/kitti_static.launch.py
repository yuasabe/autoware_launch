from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()

    node1 = Node(package = "tf2_ros", 
                       executable = "static_transform_publisher",
                       arguments = ["0","0","0","0","0","0","base_link","velodyne_top_base_link"])

    ld.add_action(node1)

    node2 = Node(package = "tf2_ros", 
                       executable = "static_transform_publisher",
                       arguments = ["0","0","0","0","0","0","base_link","tamagawa/imu_link"])

    ld.add_action(node2)

    return ld