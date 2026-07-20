import rclpy


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node("rover_heartbeat_minimal")

    try:
        while rclpy.ok():
            node.get_logger().info("Rover heartbeat: core system is alive")
            rclpy.spin_once(node, timeout_sec=1.0)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()