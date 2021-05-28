#
# Candidates:
#
# https://github.com/syrusakbary/snapshottest
import snapshottest


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class TestClown(snapshottest.TestCase):

    def test_point(self):
        point = Point(x=11, y=22)
        self.assertMatchSnapshot(point)
