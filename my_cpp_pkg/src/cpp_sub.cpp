#include <memory>

// Include the ROS 2 C++ client library
#include "rclcpp/rclcpp.hpp"
// Include the message type we established for compatibility
#include "example_interfaces/msg/int64.hpp"

// This allows us to use _1 as a placeholder for the callback parameter
using std::placeholders::_1;

class NumberCounterNode : public rclcpp::Node
{
public:
  NumberCounterNode()
  : Node("cpp_num_sub"), counter_(0)
  {
    // 1. Create the subscription
    // Interface type: example_interfaces::msg::Int64
    // Topic: "Num"
    // Queue size: 10
    // Callback: topic_callback (bound to this class instance)
    subscription_ = this->create_subscription<example_interfaces::msg::Int64>(
      "Num", 10, std::bind(&NumberCounterNode::topic_callback, this, _1));

    RCLCPP_INFO(this->get_logger(), "C++ Number counter has been started.");
  }

private:
  // This function runs every time a message is received on the "Num" topic
  void topic_callback(const example_interfaces::msg::Int64 & msg)
  {
    // Extract the data, add it to our running total
    counter_ += msg.data;
    
    // Print the current total to the terminal
    RCLCPP_INFO(this->get_logger(), "Current count: '%ld'", counter_);
  }
  
  // Declare internal variables
  rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscription_;
  int64_t counter_;
};

int main(int argc, char * argv[])
{
  // Initialize ROS 2
  rclcpp::init(argc, argv);

  // Spin the node so it stays awake to listen for incoming messages
  rclcpp::spin(std::make_shared<NumberCounterNode>());

  // Clean up when Ctrl+C is pressed
  rclcpp::shutdown();
  return 0;
}
