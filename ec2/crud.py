import urllib


def create_key_pair(ec2_client, key_name):
    response = ec2_client.create_key_pair(KeyName=key_name,
                                          KeyType="rsa",
                                          KeyFormat="pem")
    key_id = response.get("KeyPairId")
    with open(f"{key_name}.pem", "w") as file:
        file.write(response.get("KeyMaterial"))
    print("Key pair id - ", key_id)
    return key_id


def create_security_group(ec2_client, group_name, description, vpc_id):
    response = ec2_client.create_security_group(Description=description,
                                                GroupName=group_name,
                                                VpcId=vpc_id)
    group_id = response.get("GroupId")

    print("Security Group Id - ", group_id)

    return group_id


def get_my_public_ip():
    external_ip = urllib.request.urlopen("https://ident.me").read().decode(
        "utf8")
    print("Public ip - ", external_ip)

    return external_ip


def add_ssh_access_sg(ec2_client, sg_id, ip_address):
    ip_address = f"{ip_address}/32"

    response = ec2_client.authorize_security_group_ingress(
        CidrIp=ip_address,
        FromPort=22,
        GroupId=sg_id,
        IpProtocol='tcp',
        ToPort=22,
    )
    if response.get("Return"):
        print("Rule added successfully")
    else:
        print("Rule was not added")


def run_ec2(ec2_client, sg_id, subnet_id, instance_name):
    response = ec2_client.run_instances(
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/sda1",
                "Ebs": {
                    "DeleteOnTermination": True,
                    "VolumeSize": 8,
                    "VolumeType": "gp2",
                    "Encrypted": False
                },
            },
        ],
        ImageId="ami-053b0d53c279acc90",
        InstanceType="t2.micro",
        KeyName="my-demo-key",
        MaxCount=1,
        MinCount=1,
        Monitoring={"Enabled": True},
        # SecurityGroupIds=[
        #     sg_id,
        # ],
        # SubnetId=subnet_id,
        UserData="""#!/bin/bash
echo "Hello I am from user data" > info.txt
""",
        InstanceInitiatedShutdownBehavior="stop",
        NetworkInterfaces=[
            {
                "AssociatePublicIpAddress": True,
                "DeleteOnTermination": True,
                "Groups": [
                    sg_id,
                ],
                "DeviceIndex": 0,
                "SubnetId": subnet_id,
            },
        ],
    )

    for instance in response.get("Instances"):
        instance_id = instance.get("InstanceId")
        print("InstanceId - ", instance_id)
    # pprint(response)

    # Create a name tag for the instance
    tag = {'Key': 'Name', 'Value': instance_name}

    # Assign the name tag to the instance
    ec2_client.create_tags(Resources=[instance_id], Tags=[tag])

    return None


def stop_ec2(ec2_client, instance_id):
    response = ec2_client.stop_instances(InstanceIds=[
        instance_id,
    ], )
    for instance in response.get("StoppingInstances"):
        print("Stopping instance - ", instance.get("InstanceId"))


def start_ec2(ec2_client, instance_id):
    response = ec2_client.start_instances(InstanceIds=[
        instance_id,
    ], )
    for instance in response.get("StartingInstances"):
        print("Starting instance - ", instance.get("InstanceId"))


def terminate_ec2(ec2_client, instance_id):
    response = ec2_client.terminate_instances(InstanceIds=[
        instance_id,
    ], )
    for instance in response.get("TerminatingInstances"):
        print("Terminating instance - ", instance.get("InstanceId"))
