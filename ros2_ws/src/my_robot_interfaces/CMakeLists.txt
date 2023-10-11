cmake_minimum_required(VERSION 3.8)
project(my_robot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
#ENTER MSG FILES HERE TO COMPILE
  "msg/HardwareStatus.msg"
  "srv/ComputeRectangleArea.srv"
  "srv/SetLed.srv"
  "msg/LedStatus.msg"
  "msg/TargetList.msg"
  "srv/ControlTurtle.srv"
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
