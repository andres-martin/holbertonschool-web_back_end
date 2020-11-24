#!/usr/bin/env python3
""" Unit test Test client
"""
import unittest
import json
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch, Mock
from client import GithubOrgClient


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
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)
