import pdb
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchant1 = Merchant("Overlook Hotel")
merchant_repository.save(merchant1)

merchant2 = Merchant("Stars Hollow Library")
merchant_repository.save(merchant2)

merchant3 = Merchant("Luke's Diner")
merchant_repository.save(merchant3)


tag1 = Tag("Holidays")
tag_repository.save(tag1)

tag2 = Tag("Self-development")
tag_repository.save(tag2)

tag3 = Tag("Eating out")
tag_repository.save(tag3)


pdb.set_trace