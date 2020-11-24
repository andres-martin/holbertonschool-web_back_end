#!/usr/bin/env python3
""" Unit test
"""
import unittest
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch, Mock
import client


class TestGithubOrgClient(unittest.TestCase):
    ''' self descriptive '''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        ''' self descriptive '''
        endpoint = f'https://api.github.com/orgs/{data}'
        spec = GithubOrgClient(url)
        spec.org()
        mock.assert_called_once_with(endpoint)
