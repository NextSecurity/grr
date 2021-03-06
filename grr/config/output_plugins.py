#!/usr/bin/env python
"""Configuration parameters for server output plugins."""

from grr.lib import config_lib
from grr.lib import rdfvalue

config_lib.DEFINE_string("BigQuery.service_account", None,
                         "The service account email address for BigQuery.")

config_lib.DEFINE_string("BigQuery.private_key", None,
                         "The private key entry from the service account "
                         "credential file.")

config_lib.DEFINE_string("BigQuery.project_id", None,
                         "The BigQuery project_id.")

config_lib.DEFINE_string("BigQuery.dataset_id", "grr",
                         "The BigQuery project_id.")

config_lib.DEFINE_integer("BigQuery.max_file_post_size", 5 * 1000 * 1000,
                          "Max size of file to put in each POST "
                          "to bigquery. Note enforcement is not exact.")

config_lib.DEFINE_integer("BigQuery.retry_max_attempts", 2,
                          "Total number of times to retry an upload.")

config_lib.DEFINE_integer("BigQuery.max_upload_failures", 100,
                          "Total number of times to try uploading to BigQuery"
                          " for a given hunt or flow.")

config_lib.DEFINE_semantic(rdfvalue.Duration, "BigQuery.retry_interval", "2s",
                           "Time to wait before first retry.")

config_lib.DEFINE_integer("BigQuery.retry_multiplier", 2,
                          "For each retry, multiply last delay by this value.")

config_lib.DEFINE_integer_list("BigQuery.retry_status_codes",
                               [404, 500, 502, 503, 504],
                               "HTTP status codes on which we should retry.")
