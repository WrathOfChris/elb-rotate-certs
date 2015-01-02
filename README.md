elb-rotate-certs
================

ELB Certificate Rotation tool

# Install
elb-rotate-certs is available from PyPi and can be installed via pip:

```
pip install elb-rotate-certs
```

# Example

## Update all ELBs postfixed with '-stage'

```
elb-rotate-certs --old mycert-2014 --new mycert-2015 '*-stage'
```

# Usage

## elb-rotate-certs

```
usage: elb-rotate-certs [-h] [-a] [-r REGION] --old OLD --new NEW [--regex]
                        ELB [ELB ...]

ELB Rotate Certificates

positional arguments:
  ELB                   list of ELBs or regexes to match

optional arguments:
  -h, --help            show this help message and exit
  -a, --auto            auto-detect (default: False)
  -r REGION, --region REGION
                        ec2 region (default: None)
  --old OLD             old server-certificate-name (default: None)
  --new NEW             new server-certificate-name (default: None)
  --regex               use regex instead of simple match (default: False)
```
