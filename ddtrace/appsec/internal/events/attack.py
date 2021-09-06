from typing import List
from typing import Mapping
from typing import Optional
from typing import Union

import attr

from ddtrace.appsec.internal.events.context import Context_0_1_0


@attr.s(frozen=True)
class Rule(object):
    """The rule that detected an attack."""

    id = attr.ib(type=str)
    name = attr.ib(type=str)
    tags = attr.ib(type=Mapping[str, str])


@attr.s(frozen=True)
class RuleMatchParameter(object):
    address = attr.ib(type=str)
    key_path = attr.ib(type=List[str])
    value = attr.ib(type=Optional[str], default=None)


@attr.s(frozen=True)
class RuleMatch(object):
    """The rule operator result that detected an attack."""

    operator = attr.ib(type=str)
    operator_value = attr.ib(type=str)
    parameters = attr.ib(type=List[RuleMatchParameter])
    highlight = attr.ib(type=Optional[List[str]], default=None)


@attr.s(frozen=True)
class Attack_1_0(object):
    """An event representing an AppSec Attack."""

    event_id = attr.ib(type=str)
    detected_at = attr.ib(type=str)
    rule = attr.ib(type=Rule)
    rule_match = attr.ib(type=RuleMatch)
    context = attr.ib(type=Union[Context_0_1_0])
    event_type = attr.ib(default="appsec")
    event_version = attr.ib(default="1.0")
