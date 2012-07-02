#!/usr/bin/python
#-*- coding: utf-8 -*-

""" Basic unit-tests for the pkgwat API. """

import unittest
from pkgwat.api.api import (bugs, builds, changelog, contents, releases,
                            search, updates)

PKG = 'guake'


class APItests(unittest.TestCase):
    """ Unit-tests for the pkgwat API. """

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
        expected_keys = [u'display_date', u'author', u'text',
            u'date_ts', u'version', u'date', u'email']
        self.assertEqual(guake_changelog['rows'][0].keys(), expected_keys)

    def test_contents(self):
        """ Test the contents function from the API. """
        guake_contents = contents(PKG)
        expected_keys = [u'state', u'data', u'children']
        self.assertEqual(guake_contents[0].keys(), expected_keys)
        self.assertEqual(guake_contents[0]['state'], 'open')
        expected_data = {u'icon': u'jstree-directory', u'title': u'usr'}
        self.assertEqual(guake_contents[0]['data'], expected_data)

    def test_releases(self):
        """ Test the releases function from the API. """
        guake_releases = releases(PKG)
        expected_keys = [u'release', u'testing_version', u'stable_version']
        self.assertEqual(guake_releases['rows'][0].keys(), expected_keys)
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
        expected_keys = [u'status', u'date_pushed', u'name',
            u'package_name', u'title', u'versions', u'actions',
            u'date_submitted_display', u'karma_str', u'dist_updates',
            u'releases', u'details', u'request_id',
            u'date_pushed_display', u'karma_level', u'id', u'nvr']

        self.assertEqual(guake_updates['rows'][0].keys(), expected_keys)
        self.assertEqual(guake_updates['rows'][0]['name'], PKG)
        self.assertTrue(guake_updates['rows'][0]['title'].startswith(PKG))
        self.assertEqual(guake_updates['rows'][0]['package_name'], PKG)


SUITE = unittest.TestLoader().loadTestsFromTestCase(APItests)
unittest.TextTestRunner(verbosity=2).run(SUITE)
