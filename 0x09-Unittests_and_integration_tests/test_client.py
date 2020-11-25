#!/usr/bin/env python3
""" Unit test Test client
"""
import unittest
import json
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
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
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        '''self descriptive'''
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = client.GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))
