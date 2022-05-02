#include <ros/ros.h>
#include <std_msgs/Int64.h>
#include <std_srvs/SetBool.h>

int counter = 0;
ros::Publisher pub;

void callback_add_Ints(const std_msgs::Int64& msg){
    counter += msg.data;
    ROS_INFO("The answer of addtion : %i", counter);
    std_msgs::Int64 answer;
    answer.data = counter;
    pub.publish(answer);
}

//practice for ros service
bool callback_reset_counter(std_srvs::SetBool::Request &req,
                            std_srvs::SetBool::Response &res)
{
    if (req.data == 1){
        counter = 0;
        ROS_INFO("Counter has been reset!!!!");
        res.success = true;
        res.message = "Counter has been successfully reset";
    }
    else {
        res.success = true;
        res.message = "Counter has not been successfully reset";
    }
    return true;
}


int main(int argc, char **argv){
    ros::init(argc, argv, "number_count");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("/number",1000, callback_add_Ints);
    pub = nh.advertise<std_msgs::Int64>("/number_count",10);

    //practice for ros Service

    ros::ServiceServer server = nh.advertiseService("/reset_counter", callback_reset_counter);

    ros::spin();
}