#include <ros/ros.h>
#include <std_msgs/Int64.h>
#include <stdlib.h>

int main (int argc, char **argv){
    ros::init(argc, argv, "number_publisher");
    ros::NodeHandle nh;
    
    ros::Publisher pub = nh.advertise<std_msgs::Int64>("/number",10);
    ros::Rate rate(2);

    while(ros::ok()){
        std_msgs::Int64 msg;
        msg.data = rand()%10 +1;
        pub.publish(msg);
        rate.sleep();
    }
}