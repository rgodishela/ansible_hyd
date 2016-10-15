#!/usr/bin/python
import boto.ec2
conn = boto.ec2.connect_to_region("us-east-1")
print conn.get_all_instance_status()
