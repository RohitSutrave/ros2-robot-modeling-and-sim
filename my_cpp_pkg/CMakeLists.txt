cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED) # Required for the new Int64 node
find_package(example_interfaces REQUIRED)
find_package(my_robot_interfaces REQUIRED)

# ---------------------------------------------------
# NODE 1: Your existing node
# ---------------------------------------------------
add_executable(my_cpp_node src/my_cpp_node.cpp)
ament_target_dependencies(my_cpp_node rclcpp)

# ---------------------------------------------------
# NODE 2: Your new Int64 Publisher
# ---------------------------------------------------
# "cpp_pub" is the executable name you will use with `ros2 run`
add_executable(cpp_pub src/cpp_pub.cpp)
ament_target_dependencies(cpp_pub rclcpp example_interfaces)


add_executable(cpp_sub src/cpp_sub.cpp)
ament_target_dependencies(cpp_sub rclcpp example_interfaces)

add_executable(drone_sub_node src/drone_sub.cpp)
ament_target_dependencies(drone_sub_node rclcpp my_robot_interfaces)

add_executable(reset_counter_client_node src/reset_counter_client.cpp)
ament_target_dependencies(reset_counter_client_node rclcpp my_robot_interfaces)


# 4. Install ALL targets
install(TARGETS
  my_cpp_node
  cpp_pub
  cpp_sub
  drone_sub_node
  reset_counter_client_node
          # <-- Add your new executable name here
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()