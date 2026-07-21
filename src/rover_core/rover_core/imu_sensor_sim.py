import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ImuSensorSim(Node):
    """
    A ROS 2 Node that simulates an Inertial Measurement Unit (IMU) sensor.
    It publishes simulated pitch and roll (tilt) readings to the '/imu/tilt' topic
    every second as String messages.
    """

    def __init__(self):
        # Initialize the node with the name 'imu_sensor_sim'
        super().__init__('imu_sensor_sim')
        
        # Create a publisher on the '/imu/tilt' topic using String messages
        # A queue size of 10 is used for QoS (Quality of Service)
        self.publisher = self.create_publisher(String, '/imu/tilt', 10)
        
        # Create a timer that calls the publish_tilt method every 1.0 second
        self.timer = self.create_timer(1.0, self.publish_tilt)
        
        # List of fake tilt readings to simulate sensor data
        self.readings = [
            'pitch: 5.0, roll: -2.0',
            'pitch: 8.0, roll: 1.0',
            'pitch: 16.0, roll: 3.0',
            'pitch: 4.0, roll: -12.0',
        ]
        self.index = 0

    def publish_tilt(self):
        """Timer callback that publishes the next fake tilt reading."""
        message = String()
        message.data = self.readings[self.index]
        
        # Publish the simulated readings message
        self.publisher.publish(message)
        
        # Log the published data to the console
        self.get_logger().info(f'Published tilt: {message.data}')
        
        # Cycle through the simulated readings list
        self.index = (self.index + 1) % len(self.readings)


def main(args=None):
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)
    
    # Instantiate the node
    node = ImuSensorSim()
    
    try:
        # Keep the node alive and processing callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C
        pass
    finally:
        # Destroy the node explicitly and clean up rclpy
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()