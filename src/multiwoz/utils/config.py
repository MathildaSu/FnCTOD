#!/bin/python3

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import logging, time, os


class Config20:
    def __init__(self, data_prefix):
        # data_prefix = r'../data/'
        self.data_prefix = data_prefix
        self._multiwoz_damd_init()

    def _multiwoz_damd_init(self):
        self.vocab_path_train = os.path.join(self.data_prefix, "multi-woz-2.0-processed/vocab")
        self.data_path = os.path.join(self.data_prefix, "multi-woz-2.0-processed/")
        self.data_file = "data_for_damd.json"
        self.dev_list = os.path.join(self.data_prefix, "multi-woz/valListFile.json")
        self.test_list = os.path.join(self.data_prefix, "multi-woz/testListFile.json")

        self.dbs = {
            "attraction": os.path.join(self.data_prefix, "db/attraction_db_processed.json"), 
            "hospital": os.path.join(self.data_prefix, "db/hospital_db_processed.json"), 
            "hotel": os.path.join(self.data_prefix, "db/hotel_db_processed.json"), 
            "police": os.path.join(self.data_prefix, "db/police_db_processed.json"), 
            "restaurant": os.path.join(self.data_prefix, "db/restaurant_db_processed.json"), 
            "taxi": os.path.join(self.data_prefix, "db/taxi_db_processed.json"), 
            "train": os.path.join(self.data_prefix, "db/train_db_processed.json"), 
        }
        self.domain_file_path = (
            os.path.join(self.data_prefix, "multi-woz-2.0-processed/domain_files.json")
        )
        self.slot_value_set_path = os.path.join(self.data_prefix, "db/value_set_processed.json")

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi

        self.enable_aspn = True
        self.use_pvaspn = False
        self.enable_bspn = True
        self.bspn_mode = "bspn"  # 'bspn' or 'bsdx'
        self.enable_dspn = False  # removed
        self.enable_dst = False

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi
        self.max_context_length = 900
        self.vocab_size = 3000


class Config21:
    def __init__(self, data_prefix):
        # data_prefix = r'../data/'
        self.data_prefix = data_prefix
        self._multiwoz_damd_init()

    def _multiwoz_damd_init(self):
        self.vocab_path_train = os.path.join(self.data_prefix, "multi-woz-2.1-processed/vocab")
        self.data_path = os.path.join(self.data_prefix, "multi-woz-2.1-processed/")
        self.data_file = "data_for_damd.json"
        self.dev_list = os.path.join(self.data_prefix, "multi-woz/valListFile.json")
        self.test_list = os.path.join(self.data_prefix, "multi-woz/testListFile.json")

        self.dbs = {
            "attraction": os.path.join(self.data_prefix, "db/attraction_db_processed.json"),
            "hospital": os.path.join(self.data_prefix, "db/hospital_db_processed.json"),
            "hotel": os.path.join(self.data_prefix, "db/hotel_db_processed.json"),
            "police": os.path.join(self.data_prefix, "db/police_db_processed.json"),
            "restaurant": os.path.join(self.data_prefix, "db/restaurant_db_processed.json"),
            "taxi": os.path.join(self.data_prefix, "db/taxi_db_processed.json"),
            "train": os.path.join(self.data_prefix, "db/train_db_processed.json"),
        }
        self.domain_file_path = (
            os.path.join(self.data_prefix, "multi-woz-2.1-processed/domain_files.json")
        )
        self.slot_value_set_path = os.path.join(self.data_prefix, "db/value_set_processed.json")

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi

        self.enable_aspn = True
        self.use_pvaspn = False
        self.enable_bspn = True
        self.bspn_mode = "bspn"  # 'bspn' or 'bsdx'
        self.enable_dspn = False  # removed
        self.enable_dst = False

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi
        self.max_context_length = 900
        self.vocab_size = 3000


class Config22:
    def __init__(self, data_prefix):
        # data_prefix = r'../data/'
        self.data_prefix = data_prefix
        self._multiwoz_damd_init()

    def _multiwoz_damd_init(self):
        self.vocab_path_train = os.path.join(self.data_prefix, "multi-woz-2.2-processed/vocab")
        self.data_path = os.path.join(self.data_prefix, "multi-woz-2.2-processed/")
        self.data_file = "data_for_damd.json"
        self.dev_list = os.path.join(self.data_prefix, "multi-woz/valListFile.json")
        self.test_list = os.path.join(self.data_prefix, "multi-woz/testListFile.json")

        self.dbs = {
            "attraction": os.path.join(self.data_prefix, "db/attraction_db_processed.json"),
            "hospital": os.path.join(self.data_prefix, "db/hospital_db_processed.json"),
            "hotel": os.path.join(self.data_prefix, "db/hotel_db_processed.json"),
            "police": os.path.join(self.data_prefix, "db/police_db_processed.json"),
            "restaurant": os.path.join(self.data_prefix, "db/restaurant_db_processed.json"),
            "taxi": os.path.join(self.data_prefix, "db/taxi_db_processed.json"),
            "train": os.path.join(self.data_prefix, "db/train_db_processed.json"),
        }
        self.domain_file_path = (
            os.path.join(self.data_prefix, "multi-woz-2.2-processed/domain_files.json")
        )
        self.slot_value_set_path = os.path.join(self.data_prefix, "db/value_set_processed.json")

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi

        self.enable_aspn = True
        self.use_pvaspn = False
        self.enable_bspn = True
        self.bspn_mode = "bspn"  # 'bspn' or 'bsdx'
        self.enable_dspn = False  # removed
        self.enable_dst = False

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi
        self.max_context_length = 900
        self.vocab_size = 3000


class Config23:
    def __init__(self, data_prefix):
        # data_prefix = r'../data/'
        self.data_prefix = data_prefix
        self._multiwoz_damd_init()

    def _multiwoz_damd_init(self):
        self.vocab_path_train = os.path.join(self.data_prefix, "multi-woz-2.3-processed/vocab")
        self.data_path = os.path.join(self.data_prefix, "multi-woz-2.3-processed/")
        self.data_file = "data_for_damd.json"
        self.dev_list = os.path.join(self.data_prefix, "multi-woz/valListFile.json")
        self.test_list = os.path.join(self.data_prefix, "multi-woz/testListFile.json")

        self.dbs = {
            "attraction": os.path.join(self.data_prefix, "db/attraction_db_processed.json"),
            "hospital": os.path.join(self.data_prefix, "db/hospital_db_processed.json"),
            "hotel": os.path.join(self.data_prefix, "db/hotel_db_processed.json"),
            "police": os.path.join(self.data_prefix, "db/police_db_processed.json"),
            "restaurant": os.path.join(self.data_prefix, "db/restaurant_db_processed.json"),
            "taxi": os.path.join(self.data_prefix, "db/taxi_db_processed.json"),
            "train": os.path.join(self.data_prefix, "db/train_db_processed.json"),
        }
        self.domain_file_path = (
            os.path.join(self.data_prefix, "multi-woz-2.3-processed/domain_files.json")
        )
        self.slot_value_set_path = os.path.join(self.data_prefix, "db/value_set_processed.json")

        self.exp_domains = ["all"]  # hotel,train, attraction, restaurant, taxi

        self.enable_aspn = True
        self.use_pvaspn = False
        self.enable_bspn = True
        self.bspn_mode = "bspn"  # 'bspn' or 'bsdx'
        self.enable_dspn = False  # removed
        self.enable_dst = False

        self.exp_domains = ["all"]  # hotel, train, attraction, restaurant, taxi
        self.max_context_length = 900
        self.vocab_size = 3000
