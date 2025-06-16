# Beginner Tutorials

## Setup

> ROS version (ROS Noetic): https://wiki.ros.org/noetic
> 
> Build system (catkin): http://wiki.ros.org/catkin
>
> Reference: https://wiki.ros.org/ROS/Tutorials

### Create a ROS Package

Create a ROS package named `beginner_tutorials` and add default dependencies
```sh
cd /catkin_ws/src
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp # Use the catkin_create_pkg script to create a new package called 'beginner_tutorials' which depends on std_msgs, roscpp, and rospy:
```

General command to create a ROS package

```sh
# This is an example, do not try to run this
# catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
```

### Build a catkin workspace and source the setup file

Build the catkin workspace
```sh
cd /catkin_ws/
catkin clean # Cleans your catkin workspace by deleting the build/, devel/, and optionally the install/ directories.
catkin_make
```
After the workspace has been built it has created a similar structure in the devel subfolder as you usually find under /opt/ros/$ROSDISTRO_NAME.

To add the workspace to your ROS environment, you need to source the generated setup file:

```sh
. ~/catkin_ws/devel/setup.bash
```

## Practice 1: Create a Publisher/Subscriber

```sh
roscd beginner_tutorials
mkdir scripts
cd scripts
```

Then download the example script talker.py to your new scripts directory and make it executable:

```sh
wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
chmod +x talker.py
```

Download the listener.py file into your scripts directory:

```sh
roscd beginner_tutorials/scripts/
wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
chmod +x listener.py
```

Then, edit the catkin_install_python() call in your CMakeLists.txt so it looks like the following:

```sh
catkin_install_python(PROGRAMS scripts/talker.py scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
Building your nodes

```sh
cd ~/catkin_ws
catkin_make
```

Run the Publisher/Subscriber

```sh
# Make sure that a roscore is up and running:
roscore
cd catkin_ws
source ./devel/setup.bash
rosrun beginner_tutorials talker.py
rosrun beginner_tutorials listener.py
```

## Practice 2: Create a Publisher/Subscriber to add two numbers

## Practice 3: Create a Service/Client

```sh
roscd beginner_tutorials
cd scripts
```

Create scripts/[add_two_ints_server.py](https://github.com/chengjie-lu/egia-ros-leorover/blob/main/src/beginner_tutorials/scripts/add_two_ints_server.py)

Create scripts/[add_two_ints_client.py](https://github.com/chengjie-lu/egia-ros-leorover/blob/main/src/beginner_tutorials/scripts/add_two_ints_client.py)

