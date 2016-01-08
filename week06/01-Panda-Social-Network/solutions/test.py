import unittest
from social import Panda, PandaSocialNetwork


class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.bg", "male")
        self.network = PandaSocialNetwork()

    def test_has_and_add_panda_in_network(self):
        self.network.add_panda(self.ivo)

        self.assertTrue(self.network.has_panda(self.ivo))

    def test_has_panda_when_panda_not_in_network(self):
        rado = Panda("Rado", "rado@pandamail.bg", "male")

        self.assertFalse(self.network.has_panda(rado))

    def test_make_and_are_friends(self):
        rado = Panda("Rado", "rado@pandamail.bg", "male")
        self.network.make_friends(self.ivo, rado)

        self.assertTrue(self.network.are_friends(self.ivo, rado))

    def test_connection_level(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavli", "pavlin@pandamail.com", "male")
        maria = Panda("maria", "maria@pandamail.com", "female")
        viktor = Panda("Viktor", "viktor@pandamail.com", "male")

        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(rado, pavli)
        self.network.make_friends(pavli, maria)

        self.assertEqual(self.network.connection_level(self.ivo, rado), 1)
        self.assertEqual(self.network.connection_level(self.ivo, pavli), 2)
        self.assertEqual(self.network.connection_level(self.ivo, maria), 3)
        self.assertEqual(self.network.connection_level(self.ivo, viktor), 1)




if __name__ == '__main__':
    unittest.main()