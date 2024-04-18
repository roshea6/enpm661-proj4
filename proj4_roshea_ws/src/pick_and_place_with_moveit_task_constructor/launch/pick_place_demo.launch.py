from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    # moveit_config = MoveItConfigsBuilder("moveit_resources_panda").to_dict()
    moveit_config = MoveItConfigsBuilder("panda", package_name="package_roshea").to_dict()

    # MTC Demo node
    pick_place_demo = Node(
        # package="mtc_tutorial",
        # executable="mtc_tutorial",
        package="pick_and_place_with_moveit_task_contructor",
        executable="mtc_tutorial",
        output="screen",
        parameters=[
            moveit_config,
        ],
    )

    return LaunchDescription([pick_place_demo])
