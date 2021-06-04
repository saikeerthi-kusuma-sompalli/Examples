"""
This code is for testing calculator code
author: sompalli kusuma sai keerthi
date: 01/06/2021
time: 12:13 pm
"""
import pytest  # pylint: disable=unused-import

from calculator import add


def test_add_negative():
    """

    :return: true or false
    """
    assert add(-24, -65) == -89


def test_add_zero():
    """

    :return: true or false
    """
    assert add(0, 0) == 0


def test_add_big_int():
    """

    :return: true or false
    """
    assert add(764653536477646, 0) == 764653536477646
