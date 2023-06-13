# merkle-search-tree
An abstract implementation of a Merkle Search Tree, structurally compatible with ATProto's instantiation.

The goal of this implementation is to be simple and understandable, but not necessarily useful for any real-world applications.

Normally, a MST is layered over some existing key/value store. For simplicity, this one is not, which limits its usefulness. The tree structure exists only in memory. Although you can quite easily write code to serialise and deserialise a tree from, say, an atproto CAR file, you need to load the *whole* tree - there is no support for "lazy" loading of nodes on an ad-hoc basis. Again, this is for simplicity.

CRUD operations are implemented, tree diffing operations are coming next, maybe.

I also plan to write a version that *does* layer over an existing key/value store.

Also included is a script for generating graphviz graphs of a tree. Sample output:

![image](https://github.com/DavidBuchanan314/merkle-search-tree/assets/13520633/4647265a-29aa-4d76-8928-b863f5b300f9)
