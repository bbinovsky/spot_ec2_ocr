import boto.ec2

import sys
import time

MAIN_IP = ''
MAIN_SG = 'sg-393df65c'
MAIN_KP = 'KeyPair1.pem'

class EC2Stuff:
    def __init__(self):
        self.conn = None
        self.access_key = 'Removed for security ...TAXQ'
        self.secret_key = 'Removed for security ...nJk/'
        self.region = 'us-west-2'

    def connect(self):
        self.conn = boto.ec2.connect_to_region("us-west-2", aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)

    def create_instance(self, instance_type='OCR', address=None):
        reservation = self.conn.run_instances('ami-f26d18c2', key_name='KeyPair1', instance_type='t1.micro')
        # , security_groups=['sg-393df65c'])
        print reservation
        instance = reservation.instances[0]
        time.sleep(10)
        while instance.state != 'running':
            time.sleep(5)
            instance.update()
            print "Instance state: %s" % (instance.state)

            print "instance %s done!" % (instance.id)

            if address:
                success = self.link_instance_and_ip(instance.id, address)
                if success:
                    print "Linked %s to %s" % (instance.id, address)
                else:
                    print "Failed to link %s to %s" % (instance.id, address)
                instance.update()
            return instance

    def link_instance_and_ip(self, instance_id, ip=MAIN_IP):
        success = self.conn.associate_address(instance_id=instance_id,
            public_ip=ip)
        if success:
            print "Sleeping for 60 seconds to let IP attach"
            time.sleep(60)
        return success

    def unlink_instance_and_ip(self, instance_id, ip=MAIN_IP):
        return self.conn.disassociate_address(instance_id=instance_id, public_ip=ip)

    def get_instances(self):
        return self.conn.get_all_instances()

def create_new_instance(address=MAIN_IP):
    a = EC2Stuff()
    a.connect()
    return a.create_instance(address=address)

create_new_instance()
