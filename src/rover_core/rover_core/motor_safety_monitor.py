import re

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MotorSafetyMonitor(Node):
    def __init__(self):
        super().__init__('motor_safety_monitor')
        self.subscription = self.create_subscription(
            String,
            '/imu/tilt',
            self.tilt_callback,
            10,
        )

    def tilt_callback(self, message):
        numbers = re.findall(r'-?\d+\.\d+', message.data)
        if len(numbers) != 2:
            self.get_logger().warning(f'Could not read tilt: {message.data}')
            return

        pitch, roll = (float(number) for number in numbers)
        if abs(pitch) > 10.0 or abs(roll) > 10.0:
            self.get_logger().warning(
                f'SAFETY WARNING: high tilt. pitch={pitch}, roll={roll}'
            )
        else:
            self.get_logger().info(
                f'Safe to continue. pitch={pitch}, roll={roll}'
            )


def main(args=None):
    rclpy.init(args=args)
    node = MotorSafetyMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()