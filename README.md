# merkle-search-tree
An abstract implementation of a Merkle Search Tree, structurally compatible with ATProto's instantiation.

As described in https://inria.hal.science/hal-02303490/document (*"Alex Auvolat, François Taïani. Merkle Search Trees: Efficient State-Based CRDTs in Open Networks. SRDS 2019 - 38th IEEE International Symposium on Reliable Distributed Systems, Oct 2019, Lyon, France. pp.1-10, ff10.1109/SRDS.2019.00032"*) and https://atproto.com/specs/repository

The goal of this implementation is to be simple and understandable, but not necessarily useful for any real-world applications.

Normally, a MST is layered over some existing key/value store. For simplicity, this one is not, which limits its usefulness. The tree structure exists only in memory. Although you can quite easily write code to serialise and deserialise a tree from, say, an atproto CAR file, you need to load the *whole* tree - there is no support for "lazy" loading of nodes on an ad-hoc basis. Again, this is for simplicity.

CRUD operations are implemented, tree diffing operations are coming next, maybe.

I also plan to write a version that *does* layer over an existing key/value store.

Also included is a script for generating graphviz graphs of a tree. Sample output:

![image](https://github.com/DavidBuchanan314/merkle-search-tree/assets/13520633/4647265a-29aa-4d76-8928-b863f5b300f9)

Specializing the MSTNode class for use with ATProto's hash function and fanout (of 4) might look like this:

```py
from mst import MSTNode
import hashlib

class ATNode(MSTNode):
	@staticmethod
	def key_height(key: str) -> int:
		digest = int.from_bytes(hashlib.sha256(key.encode()).digest(), "big")
		leading_zeroes = 256 - digest.bit_length()
		return leading_zeroes // 2
```
