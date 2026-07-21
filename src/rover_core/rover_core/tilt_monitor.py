import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TiltMonitor(Node):
    def __init__(self):
        super().__init__('tilt_monitor')
        self.subscription = self.create_subscription(
            String,
            '/imu/tilt',
            self.tilt_callback,
            10,
        )

    def tilt_callback(self, message):
        self.get_logger().info(f'Received tilt: {message.data}')


def main(args=None):
    rclpy.init(args=args)
    node = TiltMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()