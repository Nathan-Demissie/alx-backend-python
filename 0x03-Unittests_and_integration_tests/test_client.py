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
from unittest.mock import patch, PropertyMock

class TestGithubOrgClient(unittest.TestCase):
    # ... previous tests ...

    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct repos_url from org"""
        test_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("test")
            result = client._public_repos_url

            self.assertEqual(result, test_payload["repos_url"])

from unittest.mock import patch

class TestGithubOrgClient(unittest.TestCase):
    # ... previous tests ...

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list of repo names"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(GithubOrgClient, "_public_repos_url", return_value="https://api.github.com/orgs/test/repos") as mock_url:
            client = GithubOrgClient("test")
            result = client.public_repos

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")
