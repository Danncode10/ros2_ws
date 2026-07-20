import rclpy


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node("rover_status_beacon")

    try:
        while rclpy.ok():
            node.get_logger().info("status: rover is ready")
            rclpy.spin_once(node, timeout_sec=2.0)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
