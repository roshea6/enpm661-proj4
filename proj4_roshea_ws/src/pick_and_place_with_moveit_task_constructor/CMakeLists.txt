cmake_minimum_required(VERSION 3.8)
project(pick_and_place_with_moveit_task_contructor)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_task_constructor_core REQUIRED)
find_package(moveit_core REQUIRED)

add_executable(mtc_tutorial src/mtc_node.cpp)
target_include_directories(mtc_tutorial PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(mtc_tutorial PUBLIC c_std_99 cxx_std_17) 
# ament_target_dependencies(mtc_tutorial ${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_target_dependencies(
  mtc_tutorial
  "moveit_ros_planning_interface"
  "moveit_task_constructor_core"
  "rclcpp"
)

add_executable(minimal_mtc_tutorial src/minimal.cpp)
target_include_directories(minimal_mtc_tutorial PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(minimal_mtc_tutorial PUBLIC c_std_99 cxx_std_17) 
# ament_target_dependencies(minimal_mtc_tutorial ${THIS_PACKAGE_INCLUDE_DEPENDS})

ament_target_dependencies(
  minimal_mtc_tutorial
  "moveit_ros_planning_interface"
  "moveit_task_constructor_core"
  "rclcpp"
)

install(TARGETS mtc_tutorial minimal_mtc_tutorial
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
