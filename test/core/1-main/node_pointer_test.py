#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2014, Nigel Small
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


from py2neo import NodePointer


def test_node_pointer_equality():
    p1 = NodePointer(42)
    p2 = NodePointer(42)
    assert p1 == p2


def test_node_pointer_inequality():
    p1 = NodePointer(42)
    p2 = NodePointer(69)
    assert p1 != p2
