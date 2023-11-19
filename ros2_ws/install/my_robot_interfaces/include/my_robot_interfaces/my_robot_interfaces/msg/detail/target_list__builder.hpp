// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:msg/TargetList.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__TARGET_LIST__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__TARGET_LIST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/msg/detail/target_list__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_TargetList_target_y
{
public:
  explicit Init_TargetList_target_y(::my_robot_interfaces::msg::TargetList & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::msg::TargetList target_y(::my_robot_interfaces::msg::TargetList::_target_y_type arg)
  {
    msg_.target_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::msg::TargetList msg_;
};

class Init_TargetList_target_x
{
public:
  explicit Init_TargetList_target_x(::my_robot_interfaces::msg::TargetList & msg)
  : msg_(msg)
  {}
  Init_TargetList_target_y target_x(::my_robot_interfaces::msg::TargetList::_target_x_type arg)
  {
    msg_.target_x = std::move(arg);
    return Init_TargetList_target_y(msg_);
  }

private:
  ::my_robot_interfaces::msg::TargetList msg_;
};

class Init_TargetList_name
{
public:
  Init_TargetList_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TargetList_target_x name(::my_robot_interfaces::msg::TargetList::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_TargetList_target_x(msg_);
  }

private:
  ::my_robot_interfaces::msg::TargetList msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::msg::TargetList>()
{
  return my_robot_interfaces::msg::builder::Init_TargetList_name();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__TARGET_LIST__BUILDER_HPP_
