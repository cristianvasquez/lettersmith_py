# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestLoadBareDoc::test_content 1'] = (
    '/home/cvasquez/github.com/cristianvasquez/lettersmith_py/test/package_data/fixtures/Bare doc.md',
    '/home/cvasquez/github.com/cristianvasquez/lettersmith_py/test/package_data/fixtures/Bare doc.md',
    '/home/cvasquez/github.com/cristianvasquez/lettersmith_py/test/package_data/fixtures/Bare doc.md',
    GenericRepr('datetime.datetime(2020, 12, 23, 20, 20, 3, 636745)'),
    GenericRepr('datetime.datetime(2020, 12, 23, 20, 20, 3, 636745)'),
    'Bare doc',
    'Lorem ipsum',
    {
    },
    ''
)

snapshots['TestParseFrontmatter::test_content 1'] = (
    '/home/cvasquez/github.com/cristianvasquez/lettersmith_py/test/package_data/fixtures/Doc with meta.md',
    '/home/cvasquez/github.com/cristianvasquez/lettersmith_py/test/package_data/fixtures/Doc with meta.md',
    '/home/cvasquez/github.com/cristianvasquez/lettersmith_py/test/package_data/fixtures/Doc with meta.md',
    GenericRepr('datetime.datetime(2020, 12, 23, 20, 20, 3, 636745)'),
    GenericRepr('datetime.datetime(2020, 12, 23, 20, 20, 3, 636745)'),
    'Doc with meta',
    'Lorem ipsum',
    {
        'created': GenericRepr('datetime.date(2018, 1, 28)'),
        'summary': 'The summary',
        'title': 'Doc title'
    },
    ''
)
