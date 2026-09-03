#include <memory>
#include <chrono>
#include <functional> // Required for std::bind
#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals; // Required for '500ms'

class MyCustumNode : public rclcpp::Node 
{
public:
    MyCustumNode() : Node("My_counter_node"), counter_(0)
    {
        // Fixed: std::bind (two colons) and print_hello (lowercase h)
        timer_ = this->create_wall_timer(500ms, std::bind(&MyCustumNode::print_hello, this));
    }

private:
    void print_hello()
    {
        // Fixed: Added missing semicolon at the end
        RCLCPP_INFO(this->get_logger(), "Hello Ros2! Counter : %d", counter_++);
    }
    
    int counter_;
    // Fixed: rclcpp (added the missing 'c')
    rclcpp::TimerBase::SharedPtr timer_;
}; // Fixed: Added missing semicolon at the end of the class

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    
    // Create the node and spin it so the timer callbacks execute
    rclcpp::spin(std::make_shared<MyCustumNode>());
    
    rclcpp::shutdown();
    return 0;
}