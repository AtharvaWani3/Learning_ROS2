// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:srv/ControlTurtle.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__CONTROL_TURTLE__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__CONTROL_TURTLE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Request __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ControlTurtle_Request_
{
  using Type = ControlTurtle_Request_<ContainerAllocator>;

  explicit ControlTurtle_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_x = 0.0f;
      this->target_y = 0.0f;
    }
  }

  explicit ControlTurtle_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_x = 0.0f;
      this->target_y = 0.0f;
    }
  }

  // field types and members
  using _target_x_type =
    float;
  _target_x_type target_x;
  using _target_y_type =
    float;
  _target_y_type target_y;

  // setters for named parameter idiom
  Type & set__target_x(
    const float & _arg)
  {
    this->target_x = _arg;
    return *this;
  }
  Type & set__target_y(
    const float & _arg)
  {
    this->target_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Request
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Request
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlTurtle_Request_ & other) const
  {
    if (this->target_x != other.target_x) {
      return false;
    }
    if (this->target_y != other.target_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlTurtle_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlTurtle_Request_

// alias to use template instance with default allocator
using ControlTurtle_Request =
  my_robot_interfaces::srv::ControlTurtle_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Response __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ControlTurtle_Response_
{
  using Type = ControlTurtle_Response_<ContainerAllocator>;

  explicit ControlTurtle_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit ControlTurtle_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Response
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__srv__ControlTurtle_Response
    std::shared_ptr<my_robot_interfaces::srv::ControlTurtle_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlTurtle_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlTurtle_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlTurtle_Response_

// alias to use template instance with default allocator
using ControlTurtle_Response =
  my_robot_interfaces::srv::ControlTurtle_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_robot_interfaces

namespace my_robot_interfaces
{

namespace srv
{

struct ControlTurtle
{
  using Request = my_robot_interfaces::srv::ControlTurtle_Request;
  using Response = my_robot_interfaces::srv::ControlTurtle_Response;
};

}  // namespace srv

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__CONTROL_TURTLE__STRUCT_HPP_
