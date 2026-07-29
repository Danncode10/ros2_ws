import rclpy
from example_interfaces.srv import Trigger
from rclpy.node import Node


class DiagnosticsServer(Node):
    def __init__(self):
        super().__init__('diagnostics_server')
        self.service = self.create_service(
            Trigger,
            '/run_diagnostics',
            self.run_diagnostics_callback,
        )
        self.get_logger().info('Diagnostics service is ready.')

    def run_diagnostics_callback(self, request, response):
        response.success = True
        response.message = 'Battery OK, motors OK, IMU OK'
        self.get_logger().info('Diagnostics request received.')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = DiagnosticsServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()