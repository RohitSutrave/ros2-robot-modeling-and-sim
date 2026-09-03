import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import DroneState  # Import custom message

class SwarmDronePublisher(Node):
    def __init__(self):
        super().__init__("swarm_drone_publisher")
        
        # Publisher for swarm status updates
        self.publisher_ = self.create_publisher(DroneState, "swarm_status", 10)
        self.timer_ = self.create_timer(1.0, self.publish_drone_state)
        self.get_logger().info("Swarm Drone Publisher Node active.")

    def publish_drone_state(self):
        msg = DroneState()
        
        # Populate custom message fields
        msg.drone_id = 101
        msg.position_x = 12.4
        msg.position_y = -5.8
        msg.position_z = 15.0
        msg.battery_percentage = 88.5
        msg.is_leader = True
        msg.status_message = "Navigating to waypoint B"

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published Drone {msg.drone_id} status at Z={msg.position_z}m")

def main(args=None):
    rclpy.init(args=args)
    node = SwarmDronePublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()