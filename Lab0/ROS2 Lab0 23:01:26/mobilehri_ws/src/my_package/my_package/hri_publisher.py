import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HRIPublisher(Node):

    def __init__(self):
        super().__init__('hri_publisher')
        self.publisher_ = self.create_publisher(String, 'hri_topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()     # could also encouter a message type called Point = Point()
        msg.data = 'Hey robot, how are you doing? (%d)' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Chatting with the robot: "%s"' %
                               msg.data)  # equivalent of print() in Python
        self.i += 1


def main(args=None):
    rclpy.init(args=args)   # intialize the eclpy library

    hri_publisher = HRIPublisher()

    rclpy.spin(hri_publisher)   # spin the node after a node is created
    # most relevant to timer callback function

    hri_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()  # called the main function above
