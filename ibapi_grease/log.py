# Copyright 2017 QuantRocket - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pkgutil
import ibapi

def noop(*args, **kwargs):
    """
    Do nothing.
    """
    return

def silence_ibapi_logging():
    """
    Silences the excessive ibapi logging to the root logger.
    """
    for _, module_name, _ in pkgutil.iter_modules(ibapi.__path__):
        module = __import__("ibapi.{0}".format(module_name), fromlist="ibapi")
        if not hasattr(module, "logging"):
            continue
        module.logging.debug = module.logging.info = module.logging.error = noop