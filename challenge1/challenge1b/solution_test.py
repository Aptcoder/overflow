import unittest

from solution import identify_router, read_nodes_into_graph

# 1 -> 2 -> 3 -> 5 -> 2 -> 1 = 2 *since router 2 has 2 inbound links and 2 outbound links

# 1 -> 3 -> 5 -> 6 -> 4 -> 5 -> 2 -> 6 = 5 * since router 5 has 2 inbound links and 2 outbound link

# 2 -> 4 -> 6 -> 2 -> 5 -> 6 = 2, 6 * since router 2 has 1 inbound link and 2 outbound links and 6 has 2 inbound links and 1 outbound link


class TestIdentifyRouter(unittest.TestCase):

    def test_identify_router(self):
        graph1 = read_nodes_into_graph('1 -> 2 -> 3 -> 5 -> 2 -> 1')
        graph2 = read_nodes_into_graph('1 -> 3 -> 5 -> 6 -> 4 -> 5 -> 2 -> 6')
        graph3 = read_nodes_into_graph('2 -> 4 -> 6 -> 2 -> 5 -> 6')

        self.assertEqual(identify_router(graph1), '2')
        self.assertEqual(identify_router(graph2), '5')
        self.assertEqual(identify_router(graph3), '2,6')



if __name__ == "__main__":
    unittest.main()
