# -*- coding: utf-8 -*-
# @Time : 2019/11/2 19:56
# @Author : wangmengmeng

import pytest

@pytest.mark.P0
def test_01():
    print("1")
    assert 1 == 1


def test_02():
    assert 1 == 1

