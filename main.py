from auth import init_client
from bucket.crud import list_buckets, create_bucket, delete_bucket, bucket_exists, show_bucket_tree, purge_bucket
from bucket.policy import read_bucket_policy, assign_policy
from bucket.versioning import versioning
from bucket.encryption import set_bucket_encryption, read_bucket_encryption
from bucket.organize import object_per_extension
from object.crud import download_file_and_upload_to_s3, get_objects, upload_local_file, delete_object
from object.versioning import list_object_versions, rollback_to_version
from object.policy import set_object_access_policy
from inspire.quotes import random_quote
from host_static.host_web_page_files import static_web_page_file
from host_static.host_web_configuration import set_bucket_website_policy
from vpc.crud import *
from ec2.crud import *
from database.crud import *
from queue.crud import *
from my_args import bucket_arguments, object_arguments, host_arguments, vps_args, ec2_args, database_args, sqs_args
import argparse

parser = argparse.ArgumentParser(
    description="CLI program that helps with S3 buckets.",
    prog='main.py',
    epilog='DEMO APP - 2 FOR BTU_AWS'
)


subparsers = parser.add_subparsers(dest='command')

bucket_arguments(subparsers.add_parser("bucket", help="work with Bucket/s"))
object_arguments(subparsers.add_parser("object", help="work with Object/s"))
host_arguments(subparsers.add_parser("host", help="host static Website"))
vps_args(subparsers.add_parser("vpc", help="work with vpc"))
ec2_args(subparsers.add_parser("ec2", help="work with ec2"))
sqs_args(subparsers.add_parser("sqs", help="work with sqs"))
database_args(subparsers.add_parser("database", help="host static Website"))
subparsers.add_parser("list_buckets", help="List already created buckets.")
subparsers.add_parser("inspire", help="List already created buckets.")


def main():
    args = parser.parse_args()

    match args.command:

        case "bucket":
            s3_client = init_client("s3")
            if args.create_bucket == "True":
                if (args.bucket_check == "True") and bucket_exists(s3_client, args.name):
                    parser.error("Bucket already exists")
                if create_bucket(s3_client, args.name, args.region):
                    print(f"Bucket: {args.name} successfully created")

            if (args.delete_bucket == "True") and delete_bucket(s3_client, args.name):
                print("Bucket successfully deleted")

            if args.purge_objects:
                print(f'Bucket: {args.name}, Purged: {purge_bucket(s3_client, args.name)}')

            if args.bucket_exists == "True":
                print(f"Bucket exists: {bucket_exists(s3_client, args.name)}")

            if args.read_policy == "True":
                print(read_bucket_policy(s3_client, args.name))

            if args.list_objects == "True":
                get_objects(s3_client, args.bucket_name)

            if args.assign_read_policy == "True":
                assign_policy(s3_client, "public_read_policy", args.name)

            if args.assign_missing_policy == "True":
                assign_policy(s3_client, "multiple_policy", args.name)

            if args.bucket_encryption == "True":
                if set_bucket_encryption(s3_client, args.name):
                    print("Encryption set")

            if args.read_bucket_encryption == "True":
                print(read_bucket_encryption(s3_client, args.name))

            if args.versioning == "True":
                versioning(s3_client, args.name, True)
                print("Enabled versioning on bucket %s." % args.name)

            if args.versioning == "False":
                versioning(s3_client, args.name, False)
                print("Disabled versioning on bucket %s." % args.name)

            if args.organize_bucket:
                object_per_extension(s3_client, args.name)
                print("organized")
            if args.show_bucket_tree:
                show_bucket_tree(s3_client, args.name, '', True)

        case "object":
            s3_client = init_client("s3")

            if args.object_link:
                if args.download_upload == "True":
                    print(download_file_and_upload_to_s3(s3_client, args.bucket_name, args.object_link, args.keep_file_name))

            if args.local_object:
                print(upload_local_file(s3_client, args.bucket_name, args.local_object, args.keep_file_name, args.upload_type))

            if args.name:
                if args.list_versions:
                    list_object_versions(s3_client, args.bucket_name, args.name)

                if args.roll_back_to:
                    rollback_to_version(s3_client, args.bucket_name, args.name, args.roll_back_to)

                if args.set_object_access_policy:
                    set_object_access_policy(s3_client, args.bucket_name, args.name)

                if args.delete_object:
                    delete_object(s3_client, args.bucket_name, args.name)

        case "host":
            s3_client = init_client("s3")

            if not args.bucket_name:
                parser.error("bucket_name is required")
            if args.website_configuration is not None:
                if set_bucket_website_policy(s3_client, args.bucket_name, (True if args.website_configuration == "True" else False)):
                    print("website configuration assigned")
                else:
                    print("website configuration unassigned")
            if args.host_static:
                print(static_web_page_file(s3_client, args.bucket_name, args.host_static))

        case "list_buckets":
            s3_client = init_client("s3")

            buckets = list_buckets(s3_client)
            if buckets:
                for bucket in buckets['Buckets']:
                    print(f' Name:  {bucket["Name"]}')

        case "inspire":
            print(random_quote())

        case "vpc":
            ec2_client = init_client("ec2")

            if args.list_vpc == "True":
                list_vpcs(ec2_client)

            if args.create_vpc == "True":
                create_vpc(ec2_client)

            if args.vpc_id and add_name_tag == "True":
                add_name_tag(ec2_client, args.vpc_id)

            if args.create_igw == "True":
                create_igw(ec2_client)

            if args.create_or_get_igw == "True" and args.vpc_id:
                create_or_get_igw(ec2_client, args.vpc_id)

            if args.attach_igw_to_vpc == "True" and args.vpc_id and args.igw_id:
                attach_igw_to_vpc(ec2_client, args.vpc_id, args.igw_id)

            if args.create_route_table_with_route == "True" and args.route_table_name and args.vpc_id and args.igw_id:
                create_route_table_with_route(ec2_client, args.vpc_id, args.route_table_name, args.igw_id)

            if args.create_route_table_without_route == "True" and args.vpc_id:
                create_route_table_without_route(ec2_client, args.vpc_id)

            if args.associate_route_table_to_subnet == "True" and args.route_table_id and args.subnet_id:
                associate_route_table_to_subnet(ec2_client, args.route_table_id, args.subnet_id)

            if args.enable_auto_public_ips == "True" and args.subnet_id:
                enable_auto_public_ips(ec2_client, args.subnet_id, True)

            if args.create_subnet == "True" and args.subnet_name and args.vpc_id and args.cidr_block:
                create_subnet(ec2_client, args.vpc_id, args.cidr_block, args.subnet_name)

        case "ec2":
            ec2_client = init_client("ec2")

            if args.create_key_pair == "True" and args.key_name:
                create_key_pair(ec2_client, args.key_name)

            if args.create_security_group == "True" and args.group_name and args.description and args.vpc_id:
                create_security_group(ec2_client, args.group_name, args.description, args.vpc_id)

            if args.get_my_public_ip == "True":
                get_my_public_ip()

            if args.add_ssh_access_sg == "True" and args.security_group_id:
                public_ip = get_my_public_ip()
                add_ssh_access_sg(ec2_client, args.security_group_id, public_ip)

            if args.run_ec2 == "True" and args.security_group_id and args.subnet_id and args.instance_name:
                run_ec2(ec2_client, args.security_group_id, args.subnet_id, args.instance_name)

            if args.start_ec2 == "True" and args.instance_id:
                start_ec2(ec2_client, args.instance_id)

            if args.stop_ec2 == "True" and args.instance_id:
                stop_ec2(ec2_client, args.instance_id)

            if args.terminate_ec2 == "True" and args.instance_id:
                terminate_ec2(ec2_client, args.instance_id)

        case "database":
            rds_client = init_client("rds")

            if args.create_db_instance == "True" and args.database_engine \
                    and args.database_engine_version and args.db_name:
                create_db_instance(rds_client, args.database_engine, args.database_engine_version, args.db_name)

            if args.print_connection_params == "True" and args.db_id:
                print_connection_params(rds_client, args.db_id)

            if args.reboot_rds == "True" and args.db_id:
                reboot_rds(rds_client, args.db_id)

            if args.stop_rds == "True" and args.db_id:
                stop_rds(rds_client, args.db_id)

            if args.start_rds == "True" and args.db_id:
                start_rds(rds_client, args.db_id)

            if args.update_rds_pass == "True" and args.db_id and args.new_pass:
                update_rds_pass(rds_client, args.db_id, args.new_pass)

            if args.create_db_subnet_group == "True" and args.subnet_group_name and args.subnet_id:
                create_db_subnet_group(rds_client, args.subnet_group_name, args.subnet_id)

            if args.create_rds_security_group == "True" and args.security_group_name and args.vpc_id \
                    and args.ec2_security_group_id:
                ec2_client = init_client("ec2")
                create_rds_security_group(ec2_client, args.security_group_name, args.vpc_id, args.ec2_security_group_id)

        case "sqs":
            sqs_client = init_client("sqs")

            if args.create_queue == "True" and args.sqs_name:
                create_queue(sqs_client, args.sqs_name)

            if args.list_queues == "True":
                list_queues(sqs_client)

            if args.display_queue_configuration == "True" and args.url:
                display_queue_configuration(sqs_client, args.url)

            if args.update_queue_configuration == "True" and args.url:
                update_queue_configuration(sqs_client, args.url)

            if args.send_message == "True" and args.url and args.message:
                send_message(sqs_client, args.url, args.message)

            if args.receive_queue_message == "True" and args.url:
                receive_queue_message(sqs_client, args.url)

            if args.delete_queue_message == "True" and args.url and args.receipt_handle:
                delete_queue_message(sqs_client, args.url, args.receipt_handle)

            if args.get_queue_url == "True" and args.sqs_name:
                get_queue_url(sqs_client, args.sqs_name)

            if args.receive_and_delete_message == "True" and args.url:
                receive_and_delete_message(sqs_client, args.url)

            if args.purge_queue == "True" and args.url:
                purge_queue(sqs_client, args.url)

            if args.delete_queue == "True" and args.url:
                delete_queue(sqs_client, args.url)






main()
