<h1>A repository to track progress of learning ROS2.</h1>
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
<h2>Important Concepts use ROS2 to its full potential</h2>
<ol>
    <li><h3>Message</h3>
        <p>A Message is definition of structure of the data published over a topic. It maintains a standardized format of the data being sent over a topic so it is easy to access and process the data in other nodes. ROS2 has many in-built message definitions and a custom message definition can also be created in the form of a .msg file.<br>The structure of the message definition is as follows:<br>datatype variable_name_1<br>datatype variable_name_2<br>...</p></li>
</ol>