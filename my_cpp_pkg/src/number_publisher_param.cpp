#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

#include <chrono>
#include <memory>
#include <functional>
#include <vector>

using namespace std::chrono_literals;

class NumberPublisherParamNode : public rclcpp::Node
{
public:
    NumberPublisherParamNode()
        : Node("number_publisher_param")
    {
        // Declare parameters
        this->declare_parameter("number", 2);
        this->declare_parameter("publish_period", 1.0);

        // Read parameters
        number_ = this->get_parameter("number").as_int();
        publish_period_ = this->get_parameter("publish_period").as_double();

        // Publisher
        publisher_ = this->create_publisher<example_interfaces::msg::Int64>(
            "number",
            10
        );

        // Timer
        timer_ = this->create_wall_timer(
            std::chrono::duration<double>(publish_period_),
            std::bind(&NumberPublisherParamNode::publishNumber, this)
        );

        // Parameter callback (matches PostSetParametersCallbackHandle)
        parameter_callback_handle_ = this->add_post_set_parameters_callback(
            std::bind(
                &NumberPublisherParamNode::parametersCallback,
                this,
                std::placeholders::_1
            )
        );

        RCLCPP_INFO(
            this->get_logger(),
            "Number: %ld | Publish period: %.2f",
            number_,
            publish_period_
        );
    }

private:
    void publishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_;
        publisher_->publish(msg);

        RCLCPP_INFO(
            this->get_logger(),
            "Publishing: %ld",
            number_
        );
    }

    void parametersCallback(const std::vector<rclcpp::Parameter> & parameters)
    {
        for (const auto & param : parameters)
        {
            if (param.get_name() == "number")
            {
                number_ = param.as_int();
                RCLCPP_INFO(
                    this->get_logger(),
                    "Number changed to: %ld",
                    number_
                );
            }
            else if (param.get_name() == "publish_period")
            {
                publish_period_ = param.as_double();

                // Reset timer with new duration so rate change takes effect
                timer_->cancel();
                timer_ = this->create_wall_timer(
                    std::chrono::duration<double>(publish_period_),
                    std::bind(&NumberPublisherParamNode::publishNumber, this)
                );

                RCLCPP_INFO(
                    this->get_logger(),
                    "Publish period changed to: %.2f",
                    publish_period_
                );
            }
        }
    }

    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

    // Correct handle type for add_post_set_parameters_callback
    rclcpp::node_interfaces::PostSetParametersCallbackHandle::SharedPtr parameter_callback_handle_;

    int64_t number_;
    double publish_period_;
};

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherParamNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}