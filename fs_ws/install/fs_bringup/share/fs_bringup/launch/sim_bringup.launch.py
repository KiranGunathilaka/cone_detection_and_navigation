from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    world_file = PathJoinSubstitution([FindPackageShare("fs_world"), "fs_world", "fs_oval.world"])
    urdf_file  = PathJoinSubstitution([FindPackageShare("fs_vehicle"), "urdf", "ackermann_car.urdf.xacro"])
    ctrl_yaml  = PathJoinSubstitution([FindPackageShare("fs_vehicle"), "config", "controllers.yaml"])

    # Start Gazebo (gz sim)
    gz = ExecuteProcess(cmd=["gz","sim", "-r", world_file], output="screen")

    # Spawn the car
    spawn = ExecuteProcess(
        cmd=["ros2","run","ros_gz_sim","create","-name","fs_car","-file", urdf_file, "-x","0","-y","-6","-z","0.15"],
        output="screen")

    # Bridge camera -> ROS and control topics
    # Camera image: /camera (gz) -> /camera/image_raw (ROS)
    cam_bridge = Node(
      package="ros_gz_bridge", executable="parameter_bridge", output="screen",
      arguments=[
        "/camera@sensor_msgs/msg/Image@gz.msgs.Image",
        "/camera/info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo",
      ])

    # Velocity command: ROS Ackermann -> gz topic
    cmd_bridge = Node(
      package="ros_gz_bridge", executable="parameter_bridge", output="screen",
      arguments=["/cmd_ackermann@ackermann_msgs/msg/AckermannDrive@gz.msgs.VehicleCmd"])

    # Controllers (spin up manager)
    ctrl_mgr = Node(
      package="controller_manager", executable="ros2_control_node", output="screen",
      parameters=[{"robot_description": urdf_file}, ctrl_yaml])

    return LaunchDescription([gz, spawn, cam_bridge, cmd_bridge, ctrl_mgr])
