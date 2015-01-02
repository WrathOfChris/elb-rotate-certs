import argparse

def common_parser(description='untitled'):
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
            '-a',
            '--auto',
            help='auto-detect',
            action='store_true'
            )

    parser.add_argument(
            '-r',
            '--region',
            help='ec2 region'
            )

    return parser

import boto.utils
def common_args(args):

    # Region setting:
    # 1. Prefer command-line --region
    # 2. Use instance metadata when --auto
    # 3. Default to us-east-1
    local_region = None
    if args.auto:
        identity = boto.utils.get_instance_identity(timeout=1, num_retries=5)
        try:
            local_region = identity['document']['region']
        except KeyError:
            pass
    if not args.region:
        args.region = local_region
    else:
        local_region = args.region
    if not args.region:
        args.region = 'us-east-1'

import signal
import sys
def cli_signal_handler(signal, frame):
    sys.exit(1)
def catch_sigint():
    signal.signal(signal.SIGINT, cli_signal_handler)
