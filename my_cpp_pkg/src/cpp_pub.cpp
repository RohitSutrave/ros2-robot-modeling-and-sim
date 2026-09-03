#include <chrono>
#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp" 

using namespace std::chrono_literals;

class Int64Publisher : public rclcpp::Node
{
public:
  Int64Publisher()
  : Node("cpp_num_pub"), count_(0)
  {
    publisher_ = this->create_publisher<example_interfaces::msg::Int64>("Num", 10);
    
    timer_ = this->create_wall_timer(
      500ms, std::bind(&Int64Publisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto message = example_interfaces::msg::Int64();
    
    message.data = count_++;
    
    RCLCPP_INFO(this->get_logger(), "Publishing: '%ld'", message.data);
    
    publisher_->publish(message);
  }
  
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
  int64_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Int64Publisher>());
  rclcpp::shutdown();
  return 0;
}