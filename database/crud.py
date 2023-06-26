import requests


def create_db_instance(rds_client, engine, engine_version, db_name):
    """Creates a new RDS instance that is associated with the given security group."""
    response = rds_client.create_db_instance(
        DBName='postgres',
        DBInstanceIdentifier='demo-pg-db-1',
        AllocatedStorage=50,
        DBInstanceClass='db.t4g.micro',
        Engine=engine,
        MasterUsername='admin',
        MasterUserPassword='admin123',
        # VpcSecurityGroupIds=[security_group_id],
        BackupRetentionPeriod=7,
        Port=5432,
        MultiAZ=False,
        EngineVersion=engine_version,
        AutoMinorVersionUpgrade=True,
        # Iops=123, # Necessary when StorageType is 'io1'
        PubliclyAccessible=True,
        Tags=[
            {
                'Key': 'Name',
                'Value': db_name
            },
        ],
        StorageType='gp2',
        EnablePerformanceInsights=True,
        PerformanceInsightsRetentionPeriod=7,
        DeletionProtection=False,
    )

    _id = response.get("DBInstance").get("DBInstanceIdentifier")
    print(f"Instance {_id} was created")

    return response


def print_connection_params(rds_client, identifier):
    response = rds_client.describe_db_instances(DBInstanceIdentifier=identifier)
    instance = response.get("DBInstances")[0]
    endpoint = instance.get("Endpoint")
    host = endpoint.get("Address")
    port = endpoint.get("Port")
    username = instance.get("MasterUsername")
    db_name = instance.get("DBName")
    print("DB Host:", host)
    print("DB port:", port)
    print("DB user:", username)
    print("DB database:", db_name)


def reboot_rds(rds_client, identifier):
    rds_client.reboot_db_instance(DBInstanceIdentifier=identifier)
    print(f"RDS - {identifier} rebooted successfully")


def stop_rds(rds_client, identifier):
    response = rds_client.stop_db_instance(
        DBInstanceIdentifier=identifier, DBSnapshotIdentifier="stop-snapshot001")

    print(response)


def start_rds(rds_client, identifier):
    response = rds_client.start_db_instance(DBInstanceIdentifier=identifier)

    print(response)


def update_rds_pass(rds_cient, identifer, password):
    response = rds_cient.modify_db_instance(DBInstanceIdentifier=identifer,
                                            MasterUserPassword=password)

    print(response)


def create_db_subnet_group(rds_client, subnet_group_name, subnet_ids):
    description = "auto-description"
    response = rds_client.create_db_subnet_group(
        DBSubnetGroupName=subnet_group_name,
        DBSubnetGroupDescription=description,
        SubnetIds=subnet_ids)

    print(f"DB subnet group {subnet_group_name} has been created successfully.")
    return response['DBSubnetGroup'].get("DBSubnetGroupName")


def create_rds_security_group(ec2_client, security_group_name,
                              vpc_id, ec2_security_group_id):

    source_security_group_id = ec2_security_group_id
    try:
        response = ec2_client.describe_security_groups(
            GroupNames=[security_group_name])
        security_group_id = response['SecurityGroups'][0]['GroupId']
        print(
            f"Security Group {security_group_name} already exists with ID {security_group_id}"
        )
    except ec2_client.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidGroup.NotFound':
            response = ec2_client.create_security_group(
                GroupName=security_group_name,
                Description='Security Group for RDS',
                VpcId=vpc_id)
            security_group_id = response['GroupId']
            print(
                f"Security Group {security_group_name} created with ID {security_group_id}"
            )
        else:
            raise e

    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 5432,
                'ToPort': 5432,
                'UserIdGroupPairs': [
                    {
                        'GroupId': source_security_group_id,
                    },
                ],
            },
        ],
    )
    print("security group id: ", security_group_id)
    return security_group_id
