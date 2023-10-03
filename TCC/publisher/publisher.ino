#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle nh;

std_msgs::Int32 int_msg;
ros::Publisher smoke("smoke", &int_msg);

int randNumber;
int smokeA0 = A5

void setup() {
  
  nh.initNode();
  nh.advertise(smoke);
  randomSeed(analogRead(0));
  pinMode(smokeA0, INPUT);

}

void loop() {
  
  int analogSensor = analogRead(smokeA0);
  int_msg.data = analogSensor;
  smoke.publish( &int_msg );
  nh.spinOnce();
  delay(1000);

}
