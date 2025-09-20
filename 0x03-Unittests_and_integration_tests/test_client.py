#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class in client.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient.org method"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that GithubOrgClient.org returns correct payload"""
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
