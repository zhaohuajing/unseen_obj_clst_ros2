cmake_minimum_required(VERSION 3.5)
project(unseen_obj_clst_ros2)

# Core dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate service interface
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SegImage.srv"
)
ament_export_dependencies(rosidl_default_runtime)

# Install your Python executables (ROS 2 nodes)
install(PROGRAMS
  unseen_obj_clst_ros2/segmentation_server.py
  unseen_obj_clst_ros2/segmentation_client.py
  DESTINATION lib/${PROJECT_NAME}
)

# (Optional) include resource files like launch or config
# install(DIRECTORY launch DESTINATION share/${PROJECT_NAME}/)

ament_package()
