from mst import MST, MSTNode
from typing import Dict
import graphviz

class GraphableMST(MST):
	def graph(self, title: str=None):
		dot = graphviz.Digraph(node_attr={"shape": "record"})
		if title is not None:
			dot.attr(label=title, labelloc="t")
		dot.node("root", "root")
		dot.edge("root", str(id(self.root)))
		self.graph_node(dot, {}, self.root)
		return dot

	def graph_node(self, dot: graphviz.Digraph, clusters: Dict[int, graphviz.Digraph], node: MSTNode):
		members = []
		sub = node.subtrees[0]
		members.append(f"<{id(sub)}> ⬤")
		if sub is not None:
			dot.edge(f"{id(node)}:{id(sub)}:s", f"{id(sub)}:n")
			self.graph_node(dot, clusters, sub)
		for sub, k in zip(node.subtrees[1:], node.keys):
			members.append(f"\"{k}\"\\l({node.key_height(k)})")
			members.append(f"<{id(sub)}> ⬤")
			if sub is not None:
				dot.edge(f"{id(node)}:{id(sub)}:s", f"{id(sub)}:n")
				self.graph_node(dot, clusters, sub)
		level = node.height()
		if level not in clusters:
			clusters[level] = graphviz.Digraph()
			clusters[level].attr(rank="same")
		clusters[level].node(str(id(node)), " | ".join(members), fontname="monospace", fontsize="8pt")
		dot.subgraph(clusters[level])

if __name__ == "__main__":
	class StrlenNode(MSTNode):
		@staticmethod
		def key_height(key: str) -> int:
			return len(key)
	
	tree = GraphableMST.new_with(StrlenNode)

	tree["apple"] = "apple"
	tree["cherry"] = "cherry"
	tree["banana"] = "banana"
	tree["grape"] = "grape"
	tree["berry"] = "berry"
	tree["plums"] = "plums"
	tree["melon"] = "melon"
	tree["pear"] = "pear"

	tree.graph("MST with key_height=strlen").render("vis")

