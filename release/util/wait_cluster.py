import argparse
import time

import ray
from ray.test_utils import wait_for_num_nodes

ray.init(address="auto")

parser = argparse.ArgumentParser()
parser.add_argument(
    "num_nodes",
    type=int,
    help="Wait for this number of nodes (includes head)")

parser.add_argument(
    "max_time_s", type=int, help="Wait for this number of seconds")

parser.add_argument(
    "--feedback_interval_s",
    type=int,
    default=10,
    help="Wait for this number of seconds")

args = parser.parse_args()

wait_for_num_nodes(args.num_nodes, args.max_time_s)
