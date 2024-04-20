from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    # Static TF
    # static_tf = Node(
    #     package="tf2_ros",
    #     executable="static_transform_publisher",
    #     name="static_transform_publisher",
    #     output="log",
    #     arguments=["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "world_frame", "panda_link0"],
    # )
    
    
    moveit_config = MoveItConfigsBuilder("panda", package_name="package_roshea").to_moveit_configs()
    return generate_demo_launch(moveit_config)
