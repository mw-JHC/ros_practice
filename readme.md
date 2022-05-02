# ros_practice
## ROS practice with C++ and Python3  
### 1. Day1: Create Catkin workspace, ROS Package and Nodes with C++ und Python3 
Enviroment: WSL, Unbuntu 20.04, ROS-Noetic, C++, Python3
This material is intended as a review of the ROS practice for my self.
#### 1.1 Catkin Workspace
* What is a catkin workspace?  
Catkin is the official bulit system for ROS  
* How to a create catkin workspace?
  ```console  
  $ mkdir catkin_ws
  $ cd catkin_ws
  $ mkdir src
  $ catkin_make
  $ source devel/setup.bash
  ```  
  Catkin_make is the command to build the ROS Workspace.
#### 1.2 ROS Package
* What is a ROS Package?  
ROS Package will allow us to separate our code into resusable block so the development and maintenance of the application will be easier
* How to create a ROS Package?
  ```console
  $ catkin_create_pkg {name of a package} {dependencies of the package}
  ```
  for example
  ```console
  $ catkin_create_pkg robot_package roscpp rospy std_msgs
  ```
  it mean we create a ROS Package with the dependencies roscppp(for c++), rospy(for Python) and std_msgs(the basic ROS package Standard Messages).  
#### 1.3 ROS Node
* What is a ROS Node?(according to ROS Wiki)
  > A ROS node is a process that performs computation. Nodes are combined together into a graph and communicate with one another using streaming topic, RPC services, and the Parameter Server. 
* How to create a ROS Node through Python?  
  Make first a script folder under the Package folder and create a python file in that the contents of a node will be written.  
  For example
  ```console
  $ cd catkin_ws/src/robot_package
  $ mkdir scripts
  $ touch first_python_node.py
  $ chmod +x first_python_node.py
  ```
  The Python code below will be wirtten to the generated Python file(first_python_node)
  ```python
  #!/usr/bin/env python3

  import rospy

  if __name__ == '__main__':
    rospy.init_node('first_python_node')
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown(): # if the node is not shutdowned, it work again
        rospy.loginfo("Hellow")
        rate.sleep()
  ```
  This Python wirtten node shows us a loginformation "hellow" every 10 seconds.
  The node can be executed with this linux command
  ```console
  $ cd catkin_ws/src/robot_package/scripts
  $ python3 first_python_node
  ```
* How to create a ROS Node through C++?  
  Now we try to write a new node in C++ with the same functionality as the node above.
  A node is written under src folder of the Package directly.  
  For example  
  ```console
  $ cd catkin_ws/src/robot_package/src
  $ touch first_cpp_node.py
  $ chmod +x first_cpp_node.py
  ```  
  The C++ code below will be wirtten to the generated C++ file(first_cpp_node)
  ```cpp
  #include <ros/ros.h>

  int main(int argc, char **argv)
  {
  ros::init(argc, argv, "my_first_cpp_node");
  ros::NodeHandle nh;
  ROS_INFO("Node has been started");

  ros::Rate rate(10);

  while(ros::ok()){
      ROS_INFO("Hellow");
      rate.sleep(); //sleep 0.1 second
    }
  }
  ```
  The node written in c++ require compilation. For that we need to add the codes below in the CMakeList.txt under the Package Folder. we can find a exaple code in the CMakeList file.
  ```txt
  add_executable(node_cpp src/first_cpp_node.cpp)
  target_link_libraries(node_cpp ${catkin_LIBRARIES})
  ```
  And now because we has modified the CMakelist.txt we must rebuild the Package.
  ```console
  $ cd catkin_ws
  $ cd catkin_make
  ```
  After the rebuild the catkin workspace, the cpp node can be executed with this linux command.
  ```console
  $ cd catkin_ws/devel/lib/robot_package
  ./node_cpp# ros_practice
## ROS practice with C++ and Python3  
### 1. Day1: Create Catkin workspace, ROS Package and Nodes with C++ und Python3 
Enviroment: WSL, Unbuntu 20.04, ROS-Noetic, C++, Python3
This material is intended as a review of the ROS practice for my self.
#### 1.1 Catkin Workspace
* What is catkin workspace?  
Catkin is the official bulit system for ROS  
* How to create catkin workspace?
  ```console  
  $ mkdir catkin_ws
  $ cd catkin_ws
  $ mkdir src
  $ catkin_make
  $ source devel/setup.bash
  ```  
  Catkin_make is the command to build the ROS Workspace.
#### 1.2 ROS Package
* What is a ROS Package?  
ROS Package will allow us to separate our code into resusable block so the development and maintenance of the application will be easier
* How to create a ROS Package?
  ```console
  $ catkin_create_pkg {name of a package} {dependencies of the package}
  ```
  for example
  ```console
  $ catkin_create_pkg robot_package roscpp rospy std_msgs
  ```
  it mean we create a ROS Package with the dependencies roscppp(for c++), rospy(for Python) and std_msgs(the basic ROS package Standard Messages).  
#### 1.3 ROS Node
* What is a ROS Node?(according to ROS Wiki)
  > A ROS node is a process that performs computation. Nodes are combined together into a graph and communicate with one another using streaming topic, RPC services, and the Parameter Server. 
* How to create a ROS Node through Python?  
  Make first a script folder under the Package folder and create a python file in that the contents of a node will be written.  
  For example
  ```console
  $ cd catkin_ws/src/robot_package
  $ mkdir scripts
  $ touch first_python_node.py
  $ chmod +x first_python_node.py
  ```
  The Python code below will be wirtten to the generated Python file(first_python_node)
  ```python
  #!/usr/bin/env python3

  import rospy

  if __name__ == '__main__':
    rospy.init_node('first_python_node')
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown(): # if the node is not shutdowned, it work again
        rospy.loginfo("Hellow")
        rate.sleep()
  ```
  This Python wirtten node shows us a loginformation "hellow" every 10 seconds.
  The node can be executed with this linux command
  ```console
  $ cd catkin_ws/src/robot_package/scripts
  $ python3 first_python_node
  ```
* How to create a ROS Node through C++?  
  Now we try to write a new node in C++ with the same functionality as the node above.
  A node is written under src folder of the Package directly.  
  For example  
  ```console
  $ cd catkin_ws/src/robot_package/src
  $ touch first_cpp_node.py
  $ chmod +x first_cpp_node.py
  ```  
  The C++ code below will be wirtten to the generated C++ file(first_cpp_node)
  ```cpp
  #include <ros/ros.h>

  int main(int argc, char **argv)
  {
  ros::init(argc, argv, "my_first_cpp_node");
  ros::NodeHandle nh;
  ROS_INFO("Node has been started");

  ros::Rate rate(10);

  while(ros::ok()){
      ROS_INFO("Hellow");
      rate.sleep(); //sleep 0.1 second
    }
  }
  ```
  The node written in c++ require compilation. For that we need to add the codes below in the CMakeList.txt under the Package Folder. we can find a exaple code in the CMakeList file.
  ```txt
  add_executable(node_cpp src/first_cpp_node.cpp)
  target_link_libraries(node_cpp ${catkin_LIBRARIES})
  ```
  And now because we has modified the CMakelist.txt we must rebuild the Package.
  ```console
  $ cd catkin_ws
  $ cd catkin_make
  ```
  After the rebuild the catkin workspace, the cpp node can be executed with this linux command.
  ```console
  $ cd catkin_ws/devel/lib/robot_package
  ./node_cpp
  ```
### 2. Day2: Communicate with ROS Topics
#### 2.1 Topic
* What is a ROS topic?  
According to ROS wiki a topic is named bus over which nodes exchange messages. It is a unidirectional data stream between publisher and subscriber, then What is a publisher and subscriber? Every node can be a publisher and subscriber.
A publisher is a ROS node, what publish a topic. And a subscriber is a ROS node that subscribe a topic, what publisher publish. A node can be worked as a publisher and a subscriber at the same time. For example, like our smartphone. We can think  a smartphone as a node. If someone sends to our smartphone a text, our smartphone accept a text, and we can read it(Subscriber) also we can send a text to someone(publisher).   
The small difference between smartphone SMS function and ROS Node is that publisher don't know who is subscriber and subscriber don't know too who is publisher. They just send a topic and accept it.

* How to creat a publisher with python?
