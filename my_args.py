from os import getenv


def bucket_arguments(parser):
    parser.add_argument('name', type=str, help="Pass bucket name.")

    parser.add_argument(
        "-cb",
        "--create_bucket",
        help="Flag to create bucket.",
        choices=["False", "True"],
        type=str,
        nargs="?",
        # https://jdhao.github.io/2018/10/11/python_argparse_set_boolean_params
        const="True",
        default="False")

    parser.add_argument("-bc",
                        "--bucket_check",
                        help="Check if bucket already exists.",
                        choices=["False", "True"],
                        type=str,
                        nargs="?",
                        const="True",
                        default="True")

    parser.add_argument(
        "-region",
        "--region",
        nargs="?",
        type=str,
        help="Region variable.",
        default=getenv("aws_s3_region_name", "us-west-2"),
    )

    parser.add_argument("-db",
                        "--delete_bucket",
                        help="flag to delete bucket",
                        choices=["False", "True"],
                        type=str,
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-be",
                        "--bucket_exists",
                        help="flag to check if bucket exists",
                        choices=["False", "True"],
                        type=str,
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-rp",
                        "--read_policy",
                        help="flag to read bucket policy.",
                        choices=["False", "True"],
                        type=str,
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-arp",
                        "--assign_read_policy",
                        help="flag to assign read bucket policy.",
                        choices=["False", "True"],
                        type=str,
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-amp",
                        "--assign_missing_policy",
                        help="flag to assign read bucket policy.",
                        choices=["False", "True"],
                        type=str,
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-lo",
                        "--list_objects",
                        type=str,
                        help="list bucket object",
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-ben",
                        "--bucket_encryption",
                        type=str,
                        help="bucket object encryption",
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-rben",
                        "--read_bucket_encryption",
                        type=str,
                        help="read bucket encryption",
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-vers",
                        "--versioning",
                        type=str,
                        help="list bucket object",
                        nargs="?",
                        default=None)

    parser.add_argument("-o_b",
                        "--organize_bucket",
                        help="list versions",
                        action='store_true')

    parser.add_argument("-pos",
                        "--purge_objects",
                        help="purges objects",
                        action='store_true')

    parser.add_argument("-sbt",
                        "--show_bucket_tree",
                        help="file name",
                        action='store_true')

    return parser


def object_arguments(parser):
    parser.add_argument('name', nargs="?", type=str, help="Pass object name.")

    parser.add_argument('bucket_name', type=str, help="Pass bucket name.")

    parser.add_argument("-du",
                        "--download_upload",
                        choices=["False", "True"],
                        help="download and upload to bucket",
                        type=str,
                        nargs="?",
                        const="True",
                        default="False")

    parser.add_argument("-ol",
                        "--object_link",
                        type=str,
                        help="link to download and upload to bucket",
                        default=None)

    parser.add_argument("-loc_o",
                        "--local_object",
                        type=str,
                        help="upload local object",
                        default=None)

    parser.add_argument("-k_f_n",
                        "--keep_file_name",
                        help="file name",
                        action='store_false')

    parser.add_argument("-u_t",
                        "--upload_type",
                        type=str,
                        help="upload function type",
                        choices=[
                            "upload_file", "upload_fileobj", "put_object",
                            "multipart_upload"
                        ])

    parser.add_argument("-l_v",
                        "--list_versions",
                        help="list versions",
                        action='store_true')

    parser.add_argument("-r_b_t",
                        "--roll_back_to",
                        type=str,
                        help="rollback to",
                        default=None)

    parser.add_argument("-sobap",
                        "--set_object_access_policy",
                        help="set object access policy",
                        action='store_true')
    parser.add_argument("-odelete",
                        "--delete_object",
                        help="set object access policy",
                        action='store_true')

    return parser


def host_arguments(parser):
    parser.add_argument('bucket_name', type=str, help="Pass bucket name.")

    parser.add_argument("-wc",
                        "--website_configuration",
                        choices=["False", "True"],
                        type=str,
                        help="set website configs",
                        default=None)

    parser.add_argument("-hs",
                        "--host_static",
                        type=str,
                        help="host static file",
                        default=None)


def vps_args(parser):
    parser.add_argument(
        "-l_vpc",
        "--list_vpc",
        help="list existed vpc.",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_vpc",
        "--create_vpc",
        help="create new vpc.",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-a_n_t",
        "--add_name_tag",
        help="add name tag to vpc.",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_igw",
        "--create_igw",
        help="create new igw",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_igw",
        "--create_or_get_igw",
        help="check if vpc has set igw or create new one",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-a_igw",
        "--attach_igw_to_vpc",
        help="attach iwg to vpc",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_r_t_w_r",
        "--create_route_table_with_route",
        help="create route table with route",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_r_t_n_r",
        "--create_route_table_without_route",
        help="create route table without route",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-a_r_t_s",
        "--associate_route_table_to_subnet",
        help="associate route table to subnet",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-e_a_p_i",
        "--enable_auto_public_ips",
        help="enable auto public ips",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_subnet",
        "--create_subnet",
        help="create new subnet",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument("--vpc_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--igw_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("r_t_n",
                        "--route_table_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("r_t_id",
                        "--route_table_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--subnet_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--cidr_block",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-s_name",
                        "--subnet_name",
                        type=str,
                        help="host static file",
                        default=None)



def ec2_args(parser):
    parser.add_argument(
        "-c_k_p",
        "--create_key_pair",
        help="create key pair",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_s_g",
        "--create_security_group",
        help="create security group",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-g_p_id",
        "--get_my_public_ip",
        help="get my public ip",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-a_ssh_a_sg",
        "--add_ssh_access_sg",
        help="add ssh access to security group",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-r_ec2",
        "--run_ec2",
        help="create new ec2",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--stop_ec2",
        help="stop ec2",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--start_ec2",
        help="start ec2",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--terminate_ec2",
        help="terminate ec2",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument("-k_name",
                        "--key_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--vpc_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-sg_id",
                        "--security_group_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--group_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--description",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--subnet_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-ec2_name",
                        "--instance_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-ec2_id",
                        "--instance_id",
                        type=str,
                        help="host static file",
                        default=None)


def database_args(parser):
    parser.add_argument(
        "-c_db",
        "--create_db_instance",
        help="create database instance",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-p_c_p",
        "--print_connection_params",
        help="print connection params",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--reboot_rds",
        help="reboot_rds",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--stop_rds",
        help="stop rds",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--start_rds",
        help="start rds",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "--update_rds_pass",
        help="update rds password",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_db_s_gr",
        "--create_db_subnet_group",
        help="create db subnet group",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-c_rds_s_gr",
        "--create_rds_security_group",
        help="create rds security group",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument("-db_eng",
                        "--database_engine",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-db_eng_v",
                        "--database_engine_version",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--db_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--db_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--new_pass",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-s_g_n",
                        "--subnet_group_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--subnet_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-sec_gr_n",
                        "--security_group_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("-ec2_sec_gr_id",
                        "--ec2_security_group_id",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--vpc_id",
                        type=str,
                        help="host static file",
                        default=None)


def sqs_args(parser):
    parser.add_argument(
        "-c_queue",
        "--create_queue",
        help="create queue",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-l_queue",
        "--list_queues",
        help="list queue",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-d_q_conf",
        "--display_queue_configuration",
        help="display queue configuration",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-u_q_conf",
        "--update_queue_configuration",
        help="update queue configuration",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-s_m",
        "--send_message",
        help="send message",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-r_q_m",
        "--receive_queue_message",
        help="receive queue message",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-d_q_m",
        "--delete_queue_message",
        help="delete queue message",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-g_q_url",
        "--get_queue_url",
        help="get queue url",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-r_d_m",
        "--receive_and_delete_message",
        help="receive and delete message",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-p_q",
        "--purge_queue",
        help="purge queue",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument(
        "-d_q",
        "--delete_queue",
        help="delete queue",
        choices=["False", "True"],
        type=str,
        nargs="?",
        const="True",
        default="False")

    parser.add_argument("--sqs_name",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--url",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--message",
                        type=str,
                        help="host static file",
                        default=None)

    parser.add_argument("--receipt_handle",
                        type=str,
                        help="host static file",
                        default=None)
