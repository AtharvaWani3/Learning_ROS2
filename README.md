<h1>A repository to track progress of learning ROS2</h1>
<br>
<h2>Fundamental Concepts</h2>
<br>
<ol>
    <li><h3>Node</h3>
        <p>A Node is a standalone entity of the ROS2 framework that performs a specific task, process data, and communicate with other nodes to achieve a specific functionality from a robotic system. These can be programmed using Python, C++, or any other supported languages.</p></li>
    <li><h3>Topic</h3>
        <p>A Topic is a communication channel that enables data transfer between nodes. It implements the publisher-subscriber model. It is a one communication channel in which a node can publish on a topic or multiple topics and a topic can have multiple subscribers.</p></li>
    <li><h3>Service</h3>
        <p>A Service is another means of communication in ROS2. It implements the server-client protocol. It is a two way communication channel in which a client node makes a request to the server node and server node processes the request and sends back a response.</p></li>
</ol>
<br>
<h2>ROS2 Interfaces and Other concepts</h2>
<ol>
    <li><h3>Message</h3>
        <p>A Message is definition of structure of the data published over a topic. It maintains a standardized format of the data being sent over a topic so it is easy to access and process the data in other nodes. ROS2 has many in-built message definitions and a custom message definition can be created in the form of a .msg file.<br>The structure of a message definition is as follows:<br>
        <br>datatype variable_name_1
        <br>datatype variable_name_2
        <br>...</p></li>
    <li><h3>Service</h3>
        <p>A Service definition is the structure for data interchange between the server node and client node. It maintains a standardized format for the request is sent by a client node and the response sent by the server node for a particular service definition. ROS2 has many in-built service definitions and custom service definition can be created in the form of a .srv file.<br>The structure of a service definition is as follows:<br>
        <br>datatype request_variable_1
        <br>datatype request_variable_2
        <br>...
        <br>---
        <br>datatype response_variable_1
        <br>datatype response_variable_2
        <br>...</p></li>
    <li><h3>Parameters</h3>
        <p>Parameters are variables that can be used to configure a node. These can be used when certain properties of a node need to be changed at run time to make the same node definition compatible with different configurations of the robot. These are defined within the node definition.</p></li>
    <li><h3>Action</h3>
        <p>An action is communication architecture built by using services and topics. It functions similar to services with the difference that an action can be cancelled midway and actions provide a steady feedback as opposed to a single response. The communication flow between an action client and an action server is as follows:</p>
        <ol>
        <li>Action Client sends a Goal to the Action Server</li>
        <li>Action Server sends a response as accepted or rejected</li>
        <li>If accepted, the Action Client sends a response request and waits for the goal to be completed</li>
        <li>Optionally, the Server may send a feedback as it completes the action</li>
        <li>Optionally, the Client may send a cancel request to stop the execution of the action</li>
        <li>Optionally, the Server may send a goal status</li>
        <li>Once the Goal is accomplished, the Action server sends the result</li>
        </ol>
        <br>
        Goal State Machine<br>
        <img src="Resources/Screenshot from 2023-12-29 19-11-09.png">
        <p>There can be multiple Action Clients sending requests to a single Action Server. And one Action Client may send more than one requests to the same Server at the same time.</p>
        </li>
</ol>
<br>
<h2>Simulation concepts and tools</h2>
<ol>
    <li><h3>TransForm (tf)</h3>
        <p>Each component of a robotic system has its own coordiniate frame. TransForms refer to the calculation for relating component coordinate frames to a base / reference frame. It is important to do so to define where each component is located on a robot with respect to a datum coordinate frame</p></li>
    <li><h3>URDF</h3>
        <p>Unified Robotics Description Format is the description of the physical links and joints of a robot used in a simulation. The dimensions and physics properties such as collisions and inertia are defined in an XML file combined with Xacro and various plugins for seamless integration with gazebo and ros2.</p>
    </li>
</ol>

<h2> General Debugging notes </h2>
<ul>
<li>gzserver and gzclient starts but gui does not open (gazebo classic)- reinstall gazebo with sudo apt install ros-<distro>-gazebo*</li>
<li>Robot spawns correctly the first time but falls through the floor the second time - look for robot_state_publisher process and manually kill it.</li>
<li>https://github.com/ros-simulation/gazebo_ros_pkgs/tree/ros2/gazebo_plugins/include/gazebo_plugins</li>
<li>Gazebo does not open with ros2 launch add to ~/.bashrc -> source /usr/share/gazebo/setup.sh</li>
<li>tf's not getting published correctly despite perfect URDF and config files.
<br>sudo apt install ros-humble-gazebo-ros-pkgs
<br>sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control</li>
<li>http://classic.gazebosim.org/tutorials/browse</li>
<li>For Arduino IDE code not uploading to board run-> home/.arduino15/packages/arduino/hardware/mbed_nano/4.0.10/post_install.sh</li>
<li>To use camera sensor with OpenCV: https://answers.ros.org/question/232534/gazebo-camera-frame-is-inconsistent-with-rviz-opencv-convention/</li>
</ul>