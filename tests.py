#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" Basic unit-tests for the pkgwat API. """

import unittest
import six
from pkgwat.api import (bugs, builds, changelog, contents, releases,
                        search, updates)

PKG = 'guake'


class APItests(unittest.TestCase):
    """ Unit-tests for the pkgwat API. """

    def assert_keys_in_dict(self, d, expected):
        """ Utility for comparing dict keys. """
        self.assertTrue(all([key in d for key in expected]))
        self.assertTrue(all([key in expected for key in d]))

    def test_bugs(self):
        """ Test the bugs function from the API. """
        ## Let's assume there will always be at least one bug against
        ## guake.
        guake_bugs = bugs(PKG, release='all')
        self.assertTrue(len(guake_bugs) > 0)

    def test_builds(self):
        """ Test the builds function from the API. """
        guake_build = builds(PKG, state='all')
        self.assertEqual(guake_build['rows'][0]['package_name'], PKG)
        self.assertEqual(guake_build['rows'][0]['owner_name'], 'pingou')
        self.assertEqual(guake_build['rows'][0]['package_id'], 6454)

    def test_builds_completed(self):
        """ Test the builds function from the API for the builds that
        completed.
        """
        guake_build = builds(PKG, state='1')
        self.assertEqual(guake_build['rows'][0]['state_str'], 'complete')
        self.assertEqual(guake_build['rows'][0]['package_id'], 6454)
        self.assertEqual(guake_build['rows'][0]['owner_name'], 'pingou')

    def test_changelog(self):
        """ Test the changelog function from the API. """
        guake_changelog = changelog(PKG)
        self.assertTrue(len(guake_changelog['rows']) > 0)
        expected_keys = [six.u(key) for key in [
            'display_date',
            'author',
            'text',
            'date_ts',
            'version',
            'date',
            'email',
        ]]
        self.assert_keys_in_dict(guake_changelog['rows'][0], expected_keys)

    def test_contents(self):
        """ Test the contents function from the API. """
        guake_contents = contents(PKG)
        expected_keys = [six.u('state'), six.u('data'), six.u('children')]
        self.assert_keys_in_dict(guake_contents[0], expected_keys)
        self.assertEqual(guake_contents[0]['state'], 'open')
        expected_data = {
            six.u('icon'): six.u('jstree-directory'),
            six.u('title'): six.u('usr')
        }
        self.assertEqual(guake_contents[0]['data'], expected_data)

    def test_releases(self):
        """ Test the releases function from the API. """
        guake_releases = releases(PKG)
        expected_keys = [six.u(key) for key in [
            'release', 'testing_version', 'stable_version'
        ]]
        self.assert_keys_in_dict(guake_releases['rows'][0], expected_keys)
        self.assertEqual(guake_releases['rows'][0]['release'], 'Rawhide')

    def test_search(self):
        """ Test the search function of the API. """
        guake_search = search(PKG)
        self.assertEqual(guake_search['rows'][0]['upstream_url'],
            'http://www.guake.org/')
        self.assertEqual(guake_search['rows'][0]['devel_owner'],
            'pingou')
        self.assertEqual(guake_search['rows'][0]['link'], PKG)

    def test_updates(self):
        """ Test the updates function of the API. """
        guake_updates = updates(PKG)
        expected_keys = [six.u(key) for key in [
            'status',
            'date_pushed',
            'name',
            'package_name',
            'title',
            'versions',
            'actions',
            'date_submitted_display',
            'karma_str',
            'dist_updates',
            'releases',
            'details',
            'request_id',
            'date_pushed_display',
            'karma_level',
            'id',
            'nvr',
        ]]

        self.assert_keys_in_dict(guake_updates['rows'][0], expected_keys)
        self.assertEqual(guake_updates['rows'][0]['name'], PKG)
        self.assertTrue(guake_updates['rows'][0]['title'].startswith(PKG))
        self.assertEqual(guake_updates['rows'][0]['package_name'], PKG)


if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(APItests)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
