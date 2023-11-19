// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/ControlTurtle.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__CONTROL_TURTLE__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__CONTROL_TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/srv/detail/control_turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_ControlTurtle_Request_target_y
{
public:
  explicit Init_ControlTurtle_Request_target_y(::my_robot_interfaces::srv::ControlTurtle_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::ControlTurtle_Request target_y(::my_robot_interfaces::srv::ControlTurtle_Request::_target_y_type arg)
  {
    msg_.target_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::ControlTurtle_Request msg_;
};

class Init_ControlTurtle_Request_target_x
{
public:
  Init_ControlTurtle_Request_target_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlTurtle_Request_target_y target_x(::my_robot_interfaces::srv::ControlTurtle_Request::_target_x_type arg)
  {
    msg_.target_x = std::move(arg);
    return Init_ControlTurtle_Request_target_y(msg_);
  }

private:
  ::my_robot_interfaces::srv::ControlTurtle_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::ControlTurtle_Request>()
{
  return my_robot_interfaces::srv::builder::Init_ControlTurtle_Request_target_x();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_ControlTurtle_Response_success
{
public:
  Init_ControlTurtle_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::ControlTurtle_Response success(::my_robot_interfaces::srv::ControlTurtle_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::ControlTurtle_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::ControlTurtle_Response>()
{
  return my_robot_interfaces::srv::builder::Init_ControlTurtle_Response_success();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__CONTROL_TURTLE__BUILDER_HPP_
