from auth import aws_client
import argparse


def create_key_pair(ec2_client, key_name):
    response = ec2_client.create_key_pair(KeyName=key_name,
                                          KeyType="rsa",
                                          KeyFormat="pem")
    key_id = response.get("KeyPairId")
    with open(f"{key_name}.pem", "w") as file:
        file.write(response.get("KeyMaterial"))
    print("Key pair id - ", key_id)
    return key_id


def list_vpcs(vpc_client):
    result = vpc_client.describe_vpcs()
    vpcs = result.get("Vpcs")
    print(vpcs)


def update_rds_pass(rds_cient, identifer, password):
    response = rds_cient.modify_db_instance(DBInstanceIdentifier=identifer,
                                            MasterUserPassword=password)

    print(response)


def main():
    parser = argparse.ArgumentParser(description="Final Example CLI")

    # https://docs.python.org/3/library/argparse.html#dest
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    ec2_parser = subparsers.add_parser("ec2")
    ec2_parser.add_argument("-key_pair",
                            action="store_true",
                            help="Generate Key Pair")
    ec2_parser.add_argument("-n", type=str, help="Key Name")
    ec2_parser.add_argument("-pem", action="store_true", help="Extension")

    vpc_parser = subparsers.add_parser("vpc")
    vpc_parser.add_argument("-list", action="store_true")

    rds_parser = subparsers.add_parser("rds")
    rds_parser.add_argument("-new_pass", type=str)
    rds_parser.add_argument("-dbInstanceId", type=str)

    args = parser.parse_args()

    # python main.py ec2 -key_pair -n "k" -pem
    if args.command == "ec2":
        client = aws_client("ec2")
        if args.key_pair and args.n and args.pem:
            create_key_pair(client, args.n)
    # python main.py vpc -list
    elif args.command == "vpc":
        client = aws_client("ec2")
        # client = list_vpcs(client)

    # python main.py rds -new_pass "12344" -dbInstanceId "456"
    elif args.command == "rds":
        client = aws_client("rds")
        if args.new_pass and args.dbInstanceId:
            update_rds_pass(client, args.dbInstanceId, args.new_pass)


if __name__ == "__main__":
    main()
