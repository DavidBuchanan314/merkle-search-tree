# merkle-search-tree
An abstract implementation of a Merkle Search Tree, structurally comparible with ATProto's instantiation.

The goal of this implementation is to be simple and understandable, but not necessarily useful for any real-world applications.

Normally, a MST is layered over some existing key/value store. For simplicity, this one is not, which limits its usefulness. The tree structure exists only in memory. Although you can quite easily write code to serialise and deserialise a tree from, say, an atproto CAR file, you need to load the *whole* tree - there is no support for "lazy" loading of nodes on an ad-hoc basis. Again, this is for simplicity.

CRUD operations are implemented, tree diffing operations are coming next, maybe.

I also plan to write a version that *does* layer over an existing key/value store.
