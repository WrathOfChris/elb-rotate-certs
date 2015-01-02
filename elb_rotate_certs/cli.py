import argparse
import fnmatch, re
import sys
from .util import common_parser, common_args, catch_sigint
from .RotateCerts import RotateCerts

def elb_rotate_certs():
    exitcode = 0
    catch_sigint()
    parser = common_parser('ELB Rotate Certificates')

    parser.add_argument(
            '--old',
            help='old server-certificate-name',
            required=True
            )
    parser.add_argument(
            '--new',
            help='new server-certificate-name',
            required=True
            )
    parser.add_argument(
            '--regex',
            help='use regex instead of simple match',
            action='store_true'
            )
    parser.add_argument(
            'elb',
            metavar='ELB',
            nargs='+',
            type=str,
            help='list of ELBs or regexes to match'
            )

    args = parser.parse_args()
    common_args(args)

    rc = RotateCerts(args.region)
    cert_arn_old = u'arn:aws:iam::%s:server-certificate/%s' % (
            rc.get_account_id(),
            args.old
            )
    cert_arn_new = u'arn:aws:iam::%s:server-certificate/%s' % (
            rc.get_account_id(),
            args.new
            )
    elbs = rc.get_all_elbs()

    for elb in elbs:
        # Match ELB names
        matches = 0
        for r in args.elb:
            if args.regex:
                match = re.match(r, elb.name)
            else:
                match = fnmatch.fnmatch(elb.name, r)
            if match:
                matches += 1;

        if matches == 0:
            continue

        for l in elb.listeners:
            if l.ssl_certificate_id == cert_arn_old:
                sys.stdout.write('update elb %s port %d\n' % (
                    elb.name,
                    l.load_balancer_port
                    ))
                ret = rc.update_elb(
                        elb.name,
                        l.load_balancer_port,
                        cert_arn_new
                        )
                if ret == False:
                    exitcode = 1

    sys.exit(exitcode)
