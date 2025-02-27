# Copyright (C) 2024 Robotec.AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import time
from typing import Type

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import tool
from langchain_core.tools import BaseTool


@tool
def sleep_max_5s(n: int):
    """Wait n seconds, max 5s"""
    if n > 5:
        n = 5

    time.sleep(n)


class WaitForSecondsToolInput(BaseModel):
    """Input for the WaitForSecondsTool tool."""

    seconds: int = Field(..., description="The number of seconds to wait")


class WaitForSecondsTool(BaseTool):
    """Wait for a specified number of seconds"""

    name: str = "WaitForSecondsTool"
    description: str = (
        "A tool for waiting. "
        "Useful for pausing execution for a specified number of seconds. "
        "Input should be the number of seconds to wait."
    )

    args_schema: Type[WaitForSecondsToolInput] = WaitForSecondsToolInput

    def _run(self, seconds: int):
        """Waits for the specified number of seconds."""
        time.sleep(seconds)
        return f"Waited for {seconds} seconds."
