import unittest
from Winners.TSC_1 import Bookmakers_Full_Review
from Winners.TSC_2 import Add_Bookmakers
from Winners.TSC_3 import Routing_from_list
from Winners.TSC_5 import List_Section


pack = unittest.TestLoader().loadTestsFromTestCase(Bookmakers_Full_Review)
pack1 = unittest.TestLoader().loadTestsFromTestCase(Add_Bookmakers)
pack2 = unittest.TestLoader().loadTestsFromTestCase(Routing_from_list)
pack3 = unittest.TestLoader().loadTestsFromTestCase(List_Section)


TestSuits = unittest.TestSuite([pack, pack1, pack2, pack3])


unittest.TextTestRunner(verbosity=2).run(TestSuits)
