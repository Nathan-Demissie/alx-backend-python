#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class in client.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the org method of GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    def test_org(self, org_name, expected_payload):
        """
        Test that GithubOrgClient.org returns the correct payload
        and calls get_json with the correct URL
        """
        with patch("client.get_json", return_value=expected_payload) as mock_get_json:
            client = GithubOrgClient(org_name)
            self.assertEqual(client.org, expected_payload)
            mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
