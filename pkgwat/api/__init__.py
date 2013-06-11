# -*- coding: utf-8 -*-
# This file is part of pkgwat.
# Copyright (C) 2012 Red Hat, Inc.
#
# pkgwat is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# pkgwat is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with pkgwat; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
""" This is a python API for https://apps.fedoraproject.org/packages

That webapp is a replacement for the `old fedora-community
<https://admin.fedoraproject.org/community/>`_.  It indexes a ton of
information from Fedora Infrastructure and presents it in a
package-centric way.  It was developed by `J5 <http://www.j5live.com/>`_,
`Luke Macken <http://lewk.org>`_, and `Máirín Duffy
<http://blog.linuxgrrl.com/>`_.

In this module, almost all of the methods have a similar signature for limiting
the number of rows, paging data results, specifying releases to query against,
etc.  If the results are problematic (or awesome), you can drop a note in
``#fedora-apps`` on freenode.

You can find the source for this project at
http://github.com/fedora-infra/pkgwat.api

:Author: Ralph Bean <rbean@redhat.com>

"""

import time
import json
import requests

import pkgwat.api
import pkgwat.api.utils

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

# TODO -- how can this be dynamically linked to setup.py?
__version__ = "0.8"

try:
    # This only works on older versions of python-requests
    import requests.defaults
    requests.defaults.defaults['base_headers']['User-Agent'] = \
        'pkgwat/' + __version__
except ImportError:
    # If it doesn't exist, no biggie.  But we should fix this in the future.
    pass


# TODO -- Tie this into cliff's verbosity options
DEBUG_REQUESTS = False
if DEBUG_REQUESTS:
    import sys

    class myobj(object):
        def write(self, message):
            print("DEBUG:", message)

    try:
        requests.defaults.defaults['verbose'] = myobj()
    except AttributeError:
        pass


BASE_URL = "https://apps.fedoraproject.org/packages/fcomm_connector"

koji_build_states = OrderedDict((
    ('all', ''),
    ('building', '0'),
    ('success', '1'),
    ('failed', '3'),
    ('cancelled', '4'),
    ('deleted', '2'),
))

bodhi_releases = [
    "all",
    "f17",
    "f16",
    "f15",
    "el6",
    "el5",
]

bodhi_statuses = [
    "all",
    "stable",
    "testing",
    "pending",
    "obsolete",
]

yum_releases = [
    'Rawhide',
    'Fedora 16',
    'Fedora 16 Testing',
    'Fedora 15',
    'Fedora 15 Testing',
    'Fedora 14',
    'Fedora 14 Testing',
]

yum_arches = [
    'x86_64',
    'i686',
]

bugzilla_releases = OrderedDict((
    ('all', ''),
    ('f17', '17'),
    ('f16', '16'),
    ('f15', '15'),
    ('el6', '6'),
    ('el5', '5'),
))


def _make_request(path, query, strip_tags):
    """ Internal util function to make a request of the connector API. """
    query_as_json = json.dumps(query)
    url = "/".join([BASE_URL, path, query_as_json])
    response = requests.get(url)
    d = response.json

    if callable(d):
        d = d()

    if strip_tags:
        d = pkgwat.api.utils.strip_tags(d)

    return d


def search(pattern, rows_per_page=10, start_row=0, strip_tags=True):
    """ Search for a pattern in package names, descriptions, and tags.

    :view: https://apps.fedoraproject.org/packages/s/python-pkgwat-api

    >>> import pkgwat.api
    >>> pkgwat.api.search("python-pkgwat-api")

    Should give something like::

      {u'rows': [{u'description': u'Python API for pkgwat',
            u'devel_owner': u'ralph',
            u'icon': u'package_128x128',
            u'link': u'python-pkgwat-api',
            u'name': u'python-pkgwat-api',
            u'sub_pkgs': [{u'description': u'Python API for pkgwat',
               u'icon': u'package_128x128',
               u'link': u'python3-python-pkgwat-api',
               u'name': u'python3-python-pkgwat-api',
               u'summary': u'Python API for querying the packages webapp'}],
            u'summary': u'Python API for querying the packages webapp',
            u'upstream_url': u'http://pypi.python.org/pypi/pkgwat.api'}],
       u'rows_per_page': 10,
       u'start_row': 0,
       u'total_rows': 1,
       u'visible_rows': 1}
    """

    path = "xapian/query/search_packages"
    query = {
        "filters": {"search": pattern},
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def get(package):
    """ Return metadata about a package.

    Raises a KeyError if no such package can be found.

    :view: https://apps.fedoraproject.org/packages/python-pkgwat-api

    >>> import pkgwat.api
    >>> pkgwat.api.get("python-pkgwat-api")

    Should give something like::

      {
         u'description': u'Python API for pkgwat',
         u'devel_owner': u'ralph',
         u'icon': u'package_128x128',
         u'link': u'python-pkgwat-api',
         u'name': u'python-pkgwat-api',
         u'sub_pkgs': [{u'description': u'Python API for pkgwat',
             u'icon': u'package_128x128',
             u'link': u'python3-python-pkgwat-api',
             u'name': u'python3-python-pkgwat-api',
             u'summary': u'Python API for querying the packages webapp'}],
         u'summary': u'Python API for querying the packages webapp',
         u'upstream_url': u'http://pypi.python.org/pypi/pkgwat.api'
      }
    """
    results = search(package)
    for pkg in results['rows']:

        if pkg['name'] == package:
            return pkg

        for subpkg in pkg['sub_pkgs']:
            if subpkg['name'] == package:
                return subpkg

    if len(results['rows']) > 0:
        raise KeyError("Exact package name not found. Some hits are close.")

    raise KeyError("No such package %r found" % package)


def releases(package, rows_per_page=10, start_row=0, strip_tags=True):
    """ Search for a pattern in package names, descriptions, and tags

    :view: https://apps.fedoraproject.org/packages/nethack

    >>> import pkgwat.api
    >>> pkgwat.api.releases("nethack")

    The above will return a list of release information::

        {u'rows': [{u'release': u'Rawhide',
                    u'stable_version': u'3.4.3-27.fc18',
                    u'testing_version': u'Not Applicable'},
                   {u'release': u'Fedora 18',
                    u'stable_version': u'3.4.3-27.fc18',
                    u'testing_version': u'None'},
                   {u'release': u'Fedora 17',
                    u'stable_version': u'3.4.3-26.fc17',
                    u'testing_version': u'None'},
                   {u'release': u'Fedora 16',
                    u'stable_version': u'3.4.3-25.fc15',
                    u'testing_version': u'None'},
                   {u'release': u'Fedora EPEL 6',
                    u'stable_version': u'None',
                    u'testing_version': u'None'},
                   {u'release': u'Fedora EPEL 5',
                    u'stable_version': u'3.4.3-12.el5.1',
                    u'testing_version': u'None'}],
         u'rows_per_page': 10,
         u'start_row': 0,
         u'total_rows': 6,
         u'visible_rows': 6}
    """

    path = "bodhi/query/query_active_releases"
    query = {
        "filters": {"package": package},
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def builds(package, state='all', rows_per_page=10,
           start_row=0, strip_tags=True):
    """ Retrieve a list of the latest koji builds for a package.

    :view: https://apps.fedoraproject.org/packages/ccze/builds

    >>> import pkgwat.api
    >>> pkgwat.api.builds("ccze", rows_per_page=2)

    The above will return a list of koji builds that looks like::

        {u'rows': [{u'build_id': 332286,
                    u'completion_time': u'2012-07-19 04:01:20.495063',
                    u'completion_time_display': {u'elapsed': u'4 minutes',
                                                 u'time': u'04:01 AM UTC',
                                                 u'when': u'27 days ago'},
                    u'completion_ts': 1342670480.49506,
                    u'creation_event_id': 4896507,
                    u'creation_time': u'2012-07-19 03:57:20.152193',
                    u'creation_ts': 1342670240.15219,
                    u'epoch': None,
                    u'name': u'ccze',
                    u'nvr': u'ccze-0.2.1-10.fc18',
                    u'owner_id': 131,
                    u'owner_name': u'ausil',
                    u'package_id': 8962,
                    u'package_name': u'ccze',
                    u'release': u'10.fc18',
                    u'state': 1,
                    u'state_str': u'complete',
                    u'task_id': 4250727,
                    u'version': u'0.2.1',
                    u'volume_id': 0,
                    u'volume_name': u'DEFAULT'},
                   {u'build_id': 298617,
                    u'completion_time': u'2012-02-10 13:15:51.600556',
                    u'completion_time_display': {u'elapsed': u'3 minutes',
                                                 u'time': u'01:15 PM UTC',
                                                 u'when': u'6 months ago'},
                    u'completion_ts': 1328879751.60056,
                    u'creation_event_id': 4407860,
                    u'creation_time': u'2012-02-10 13:12:44.186579',
                    u'creation_ts': 1328879564.18658,
                    u'epoch': None,
                    u'name': u'ccze',
                    u'nvr': u'ccze-0.2.1-9.fc18',
                    u'owner_id': 1374,
                    u'owner_name': u'ppisar',
                    u'package_id': 8962,
                    u'package_name': u'ccze',
                    u'release': u'9.fc18',
                    u'state': 1,
                    u'state_str': u'complete',
                    u'task_id': 3778561,
                    u'version': u'0.2.1',
                    u'volume_id': 0,
                    u'volume_name': u'DEFAULT'}],
         u'rows_per_page': 2,
         u'start_row': 0,
         u'total_rows': 15,
         u'visible_rows': 2}
    """

    if state not in koji_build_states.values():
        state = koji_build_states[state]

    path = "koji/query/query_builds"
    query = {
        "filters": {
            "package": package,
            "state": state,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def updates(package, release="all", status="all", rows_per_page=10,
            start_row=0, strip_tags=True):
    """ Retrieve a list of bodhi updates for a package.

    :view: https://apps.fedoraproject.org/packages/ccze/updates

    >>> import pkgwat.api
    >>> pkgwat.api.updates("ccze")

    The above will return a list of updates with comments and more::

      {u'rows': [{u'actions': '',
            u'date_pushed': u'10 Aug 2010',
            u'date_pushed_display': u'2 years  ago',
            u'date_submitted_display': u'2 years  ago',
            u'details': u'10 Aug 2010',
            u'dist_updates': [{
               u'approved': None,
               u'bugs': [
                 {u'bz_id': 578958,
                  u'parent': False,
                  u'security': False,
                  u'title': u'[abrt] crash in ccze-0.2.1-5.fc12: Process \
/usr/bin/ccze was killed by signal 11'},
                 {u'bz_id': 612866,
                  u'parent': False,
                  u'security': False,
                  u'title': u'[abrt] crash in ccze-0.2.1-5.fc12: \
parse_opt: Process /usr/bin/ccze was killed by signal 11 (SIGSEGV)'}],
                   u'builds': [{u'nvr': u'ccze-0.2.1-6.el5',
                    u'package': {
                     u'committers': [u'hubbitus'],
                     u'name': u'ccze',
                     u'suggest_reboot': False}}],
                   u'close_bugs': True,
                   u'comments': [{u'anonymous': False,
                      u'author': u'bodhi',
                      u'group': None,
                      u'karma': 0,
                      u'text': u'This update has been submitted for \
testing by hubbitus. ',
                      u'timestamp': u'2010-08-10 07:30:07',
                      u'update_title': u'ccze-0.2.1-6.el5'},
                     {u'anonymous': False,
                      u'author': u'bodhi',
                      u'group': None,
                      u'karma': 0,
                      u'text': u'This update has been pushed to testing',
                      u'timestamp': u'2010-08-10 17:55:25',
                      u'update_title': u'ccze-0.2.1-6.el5'},
                     {u'anonymous': False,
                      u'author': u'bodhi',
                      u'group': None,
                      u'karma': 0,
                      u'text': u'This update has reached 14 days in \
testing and can be pushed to stable now if the maintainer wishes',
                      u'timestamp': u'2010-08-24 23:06:30',
                      u'update_title': u'ccze-0.2.1-6.el5'},
                     {u'anonymous': False,
                      u'author': u'bodhi',
                      u'group': None,
                      u'karma': 0,
                      u'text': u'This update has been submitted for \
stable by hubbitus. ',
                      u'timestamp': u'2010-08-25 08:00:11',
                      u'update_title': u'ccze-0.2.1-6.el5'},
                     {u'anonymous': False,
                      u'author': u'bodhi',
                      u'group': None,
                      u'karma': 0,
                      u'text': u'This update has been pushed to stable',
                      u'timestamp': u'2010-08-25 18:54:46',
                      u'update_title': u'ccze-0.2.1-6.el5'}],
                   u'critpath': False,
                   u'critpath_approved': True,
                   u'date_modified': None,
                   u'date_pushed': u'2010-08-10 17:23:39',
                   u'date_submitted': u'2010-08-10 07:29:56',
                   u'karma': 0,
                   u'nagged': None,
                   u'notes': '',
                   u'release': {
                        u'dist_tag': u'dist-5E-epel',
                        u'id_prefix': u'FEDORA-EPEL',
                        u'locked': False,
                        u'long_name': u'Fedora EPEL 5',
                        u'name': u'EL-5'},
                   u'release_name': u'Fedora EPEL 5',
                   u'request': None,
                   u'stable_karma': 3,
                   u'status': u'stable',
                   u'submitter': u'hubbitus',
                   u'title': u'ccze-0.2.1-6.el5',
                   u'type': u'bugfix',
                   u'unstable_karma': -3,
                   u'updateid': u'FEDORA-EPEL-2010-3205',
                   u'version': u'0.2.1-6.el5'}],
            u'id': u'ccze-0.2.1-6.el5',
            u'karma_level': u'meh',
            u'karma_str': u' 0',
            u'name': u'ccze',
            u'nvr': u'ccze-0.2.1-6.el5',
            u'package_name': u'ccze',
            u'releases': [u'Fedora EPEL 5'],
            u'request_id': u'ccze021-6el5',
            u'status': u'stable',
            u'title': u'ccze-0.2.1-6.el5',
            u'versions': [u'0.2.1-6.el5']}],
       u'rows_per_page': 10,
       u'start_row': 0,
       u'total_rows': 2,
       u'visible_rows': 1}
    """

    if release not in bodhi_releases:
        raise ValueError("Invalid bodhi release. %r %r" % (
            release, bodhi_releases))

    if status not in bodhi_statuses:
        raise ValueError("Invalid bodhi status. %r %r" % (
            status, bodhi_statuses))

    if release == "all":
        release = ""

    if status == "all":
        status = ""

    path = "bodhi/query/query_updates"
    query = {
        "filters": {
            "package": package,
            "release": release,
            "status": status,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def bugs(package, release="all", rows_per_page=10,
         start_row=0, strip_tags=True):
    """ Return a list of bugs for a given package and release.

    :view: https://apps.fedoraproject.org/packages/python-prettytable/bugs

    >>> import pkgwat.api
    >>> pkgwat.api.bugs("python-prettytable")

    The above will yield a list of bugs on the given package::

        {u'rows': [{u'bug_class': '',
                    u'description': u'Python3 support',
                    u'id': 837087,
                    u'last_modified': u'4 decades, 2 years, 7 months, \
14 days and 22 hours',
                    u'release': u'Fedora 17',
                    u'status': u'Assigned'}],
         u'rows_per_page': 10,
         u'start_row': 0,
         u'total_rows': 1,
         u'visible_rows': 1}
    """

    if release not in bugzilla_releases.values():
        release = bugzilla_releases[release]

    path = "bugzilla/query/query_bugs"
    query = {
        "filters": {
            "package": package,
            "version": release,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def contents(package, arch="x86_64", release="Rawhide", strip_tags=True):
    """ Returns the contents of a package.

    :view: https://apps.fedoraproject.org/packages/mutt/contents

    :warning: This one behaves a little differently.
    """

    if release not in yum_releases:
        raise ValueError("Invalid yum release. %r %r" % (
            release, yum_releases))

    if arch not in yum_arches:
        raise ValueError("Invalid yum arch.  %r %r" % (
            arch, yum_arches))

    path = "yum/get_file_tree"
    query = {
        "package": package,
        "arch": arch,
        "repo": release,
    }
    url = "/".join([BASE_URL, path])
    response = requests.get(url, params=query)
    d = response.json

    # In newer versions of python-requests, response.json is a method and must
    # be invoked.  In older versions, it was just an attribute to be accessed.
    if callable(d):
        d = d()

    if strip_tags:
        d = pkgwat.api.utils.strip_tags(d)

    return d


def changelog(package, rows_per_page=10, start_row=0, strip_tags=True):
    """ Returns the changelog of a package.

    :view: https://apps.fedoraproject.org/packages/vim/changelog

    >>> import pkgwat.api
    >>> pkgwat.api.changelog("vim", rows_per_page=2)

    The above will return the changelog of a package.. something like::

        {u'rows': [{u'author': u'Karsten Hopp ',
                    u'date': u'2012-08-06 12:00:00',
                    u'date_ts': 1344254400,
                    u'display_date': u'06 Aug 2012',
                    u'email': u'karsten@redhat.com',
                    u'text': u'- drop vim-6.1-rh3.patch, (bz #754801)',
                    u'version': u'7.3.604-1'},
                   {u'author': u'Karsten Hopp ',
                    u'date': u'2012-08-06 12:00:00',
                    u'date_ts': 1344254400,
                    u'display_date': u'06 Aug 2012',
                    u'email': u'karsten@redhat.com',
                    u'text': u'- patchlevel 622',
                    u'version': u'7.3.622-1'}],
         u'rows_per_page': 2,
         u'start_row': 0,
         u'total_rows': 71,
         u'visible_rows': 2}
    """

    build_id = builds(package)['rows'][0]['build_id']

    path = "koji/query/query_changelogs"
    query = {
        "filters": {
            "build_id": build_id,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def dependencies(package, arch="noarch", release="Rawhide", version=None,
                 rows_per_page=10, start_row=0, strip_tags=True):
    """ Returns the packages that a given package depends on.

    :view: https://apps.fedoraproject.org/packages/pkgwat/relationships/

    >>> import pkgwat.api
    >>> pkgwat.api.dependencies("pkgwat")

    The above will return the deps of a package.. something like::

        {u'rows': [{u'flags': None,
                    u'name': u'python-pkgwat-api',
                    u'ops': None,
                    u'provided_by': [u'python-pkgwat-api'],
                    u'version': ''},
                {u'flags': None,
                    u'name': u'python-fabulous',
                    u'ops': None,
                    u'provided_by': [u'python-fabulous'],
                    u'version': ''},
                {u'flags': None,
                    u'name': u'python-cliff',
                    u'ops': None,
                    u'provided_by': [u'python-cliff'],
                    u'version': ''},
                {u'flags': u'EQ',
                    u'name': u'python(abi)',
                    u'ops': u'=',
                    u'provided_by': [u'python', u'python3'],
                    u'version': u'0-2.7'},
                {u'flags': None,
                    u'name': u'/usr/bin/python',
                    u'ops': None,
                    u'provided_by': [u'python'],
                    u'version': ''}],
        u'rows_per_page': 10,
        u'start_row': 0,
        u'total_rows': 5,
        u'visible_rows': 5}
    """

    if not version:
        rels = releases(package)['rows']
        relevant_releases = [r for r in rels if r['release'] == release]
        if not relevant_releases:
            return []

        version = relevant_releases[0]['stable_version']
        if version == 'None':
            version = relevant_releases[0]['testing_version']

    path = "yum/query/query_requires"
    query = {
        "filters": {
            "package": package,
            "repo": release,
            "arch": arch,
            "version": version,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def dependants(package, arch="noarch", release="Rawhide", version=None,
               rows_per_page=10, start_row=0, strip_tags=True):
    """ Returns the packages that depend on a given package.

    :view: https://apps.fedoraproject.org/packages/pkgwat/relationships/

    >>> import pkgwat.api
    >>> pkgwat.api.dependants("python-pkgwat-api")

    The above will return the packages that depend on a package.. something
    like::

        {u'rows': [{u'name': u'pkgwat',
                    u'requires': {u'flags': None,
                                u'name': u'python-pkgwat-api',
                                u'ops': None,
                                u'provided_by': None,
                                u'version': ''}},
                {u'name': u'gnome-shell-search-fedora-packages',
                    u'requires': {u'flags': None,
                                u'name': u'python-pkgwat-api',
                                u'ops': None,
                                u'provided_by': None,
                                u'version': ''}}],
        u'rows_per_page': 10,
        u'start_row': 0,
        u'total_rows': 2,
        u'visible_rows': 2}

    """

    if not version:
        rels = releases(package)['rows']
        relevant_releases = [r for r in rels if r['release'] == release]
        if not relevant_releases:
            return []

        version = relevant_releases[0]['stable_version']
        if version == 'None':
            version = relevant_releases[0]['testing_version']

    path = "yum/query/query_required_by"
    query = {
        "filters": {
            "package": package,
            "repo": release,
            "arch": arch,
            "version": version,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def provides(package, arch="noarch", release="Rawhide", version=None,
             rows_per_page=10, start_row=0, strip_tags=True):
    """ Returns that which is provided by a given package.

    :view: https://apps.fedoraproject.org/packages/pkgwat/relationships/

    >>> import pkgwat.api
    >>> pkgwat.api.provides("guake", version="0.4.2-6.fc17", arch="x86_64")

    The above should return something like::

        {u'rows': [{u'flags': u'EQ',
                    u'name': u'guake(x86-64)',
                    u'ops': None,
                    u'provided_by': None,
                    u'version': u'0-0.4.4-8.fc19'},
                {u'flags': u'EQ',
                    u'name': u'guake',
                    u'ops': None,
                    u'provided_by': None,
                    u'version': u'0-0.4.4-8.fc19'},
                {u'flags': None,
                    u'name': u'globalhotkeys.so()(64bit)',
                    u'ops': None,
                    u'provided_by': None,
                    u'version': ''}],
        u'rows_per_page': 10,
        u'start_row': 0,
        u'total_rows': 3,
        u'visible_rows': 3}


    """

    if not version:
        rels = releases(package)['rows']
        relevant_releases = [r for r in rels if r['release'] == release]
        if not relevant_releases:
            return []

        version = relevant_releases[0]['stable_version']
        if version == 'None':
            version = relevant_releases[0]['testing_version']

    path = "yum/query/query_provides"
    query = {
        "filters": {
            "package": package,
            "repo": release,
            "arch": arch,
            "version": version,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def obsoletes(package, arch="noarch", release="Rawhide", version=None,
              rows_per_page=10, start_row=0, strip_tags=True):
    """ Returns that which is obsoleted by a given package.

    :view: https://apps.fedoraproject.org/packages/pkgwat/relationships/

    >>> import pkgwat.api
    >>> pkgwat.api.obsoletes("guake", version="0.4.2-6.fc17", arch="x86_64")

    """

    if not version:
        rels = releases(package)['rows']
        relevant_releases = [r for r in rels if r['release'] == release]
        if not relevant_releases:
            return []

        version = relevant_releases[0]['stable_version']
        if version == 'None':
            version = relevant_releases[0]['testing_version']

    path = "yum/query/query_obsoletes"
    query = {
        "filters": {
            "package": package,
            "repo": release,
            "arch": arch,
            "version": version,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }

    return _make_request(path, query, strip_tags)


def conflicts(package, arch="noarch", release="Rawhide", version=None,
              rows_per_page=10, start_row=0, strip_tags=True):
    """ Returns that which is marked as "conflict" by a given package.

    :view: https://apps.fedoraproject.org/packages/pkgwat/relationships/

    >>> import pkgwat.api
    >>> pkgwat.api.conflicts("guake", version="0.4.2-6.fc17", arch="x86_64")

    """

    if not version:
        rels = releases(package)['rows']
        relevant_releases = [r for r in rels if r['release'] == release]
        if not relevant_releases:
            return []

        version = relevant_releases[0]['stable_version']
        if version == 'None':
            version = relevant_releases[0]['testing_version']

    path = "yum/query/query_conflicts"
    query = {
        "filters": {
            "package": package,
            "repo": release,
            "arch": arch,
            "version": version,
        },
        "rows_per_page": rows_per_page,
        "start_row": start_row,
    }
    return _make_request(path, query, strip_tags)


def history(package, categories=None, order="desc",
            rows_per_page=10, page=1, strip_tags=True):
    """ Returns a truncated history of fedmsg messages regarding the package.

    Unlike all the other function in this module that query the
    fedora-packages API, this function queries the datagrepper API at
    https://apps.fedoraproject.org/datagrepper/.  It is here for convenience
    purposes.

    :view: https://apps.fedoraproject.org/datagrepper/

    >>> import pkgwat.api
    >>> pkgwat.api.history("guake", categories=["bodhi"])
    """

    url = "https://apps.fedoraproject.org/datagrepper/raw/"
    categories = categories or []
    response = requests.get(
        url,
        params=dict(
            package=package,
            start=1, end=time.time(),
            meta=['subtitle', 'link'],
            category=categories,
            rows_per_page=rows_per_page,
            page=page,
            order=order,
        ),
    )
    return response.json()
