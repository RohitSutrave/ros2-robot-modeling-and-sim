#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/drone_state.hpp"

class SwarmDroneSubscriber : public rclcpp::Node
{
public:
    SwarmDroneSubscriber() : Node("swarm_drone_subscriber")
    {
        // Subscribe to the "swarm_status" topic
        subscription_ = this->create_subscription<my_robot_interfaces::msg::DroneState>(
            "swarm_status",
            10,
            std::bind(&SwarmDroneSubscriber::topic_callback, this, std::placeholders::_1)
        );
        RCLCPP_INFO(this->get_logger(), "Swarm Drone C++ Subscriber Node initialized.");
    }

private:
    void topic_callback(const my_robot_interfaces::msg::DroneState::SharedPtr msg) const
    {
        RCLCPP_INFO(this->get_logger(), "Received Drone [%ld] Status: '%s'", msg->drone_id, msg->status_message.c_str());
        RCLCPP_INFO(this->get_logger(), "Position: [X: %.2f, Y: %.2f, Z: %.2f] | Battery: %.1f%%",
                    msg->position_x, msg->position_y, msg->position_z, msg->battery_percentage);
    }

    rclcpp::Subscription<my_robot_interfaces::msg::DroneState>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SwarmDroneSubscriber>());
    rclcpp::shutdown();
    return 0;
}