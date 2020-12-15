import pdb
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository

merchant1 = Merchant("Overlook Hotel")
merchant_repository.save(merchant1)

merchant2 = Merchant("Stars Hollow Library")
merchant_repository.save(merchant2)

merchant3 = Merchant("Luke's Diner")
merchant_repository.save(merchant3)




pdb.set_trace