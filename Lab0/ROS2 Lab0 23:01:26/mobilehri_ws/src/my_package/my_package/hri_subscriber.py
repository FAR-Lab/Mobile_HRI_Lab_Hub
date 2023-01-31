import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HRISubscriber(Node):

    def __init__(self):
        super().__init__('hri_subscriber')
        self.subscription = self.create_subscription(
            String, 'hri_topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_logger().info("I am not doing so well. I failed my Turing test. ")


def main(args=None):
    rclpy.init(args=args)
    hri_subscriber = HRISubscriber()
    rclpy.spin(hri_subscriber)
    hri_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
