#include <ros/ros.h>
#include <std_msgs/Int64.h>

int counter = 0;
ros::Publisher pub;

void callback_add_Ints(const std_msgs::Int64& msg){
    counter += msg.data;
    ROS_INFO("The answer of addtion : %i", counter);
    std_msgs::Int64 answer;
    answer.data = counter;
    pub.publish(answer);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "number_count");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("/number",1000, callback_add_Ints);
    pub = nh.advertise<std_msgs::Int64>("/number_count",10);
    ros::spin();
}