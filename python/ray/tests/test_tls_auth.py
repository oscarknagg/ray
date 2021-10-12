# coding: utf-8
import os
import sys

import pytest

import logging

logger = logging.getLogger(__name__)


@pytest.mark.skipif(
    sys.platform == "darwin",
    reason=("Cryptography doesn't install in Mac build pipeline"))
@pytest.mark.parametrize("use_tls", [True], indirect=True)
def test_client_connect_to_tls_server(use_tls, init_and_serve):
    from ray.util.client import ray
    os.environ["RAY_USE_TLS"] = "0"
    with pytest.raises(ConnectionError):
        ray.connect("localhost:50051")

    os.environ["RAY_USE_TLS"] = "1"
    ray.connect("localhost:50051")
