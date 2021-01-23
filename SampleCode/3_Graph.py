class Graph:
    """ A Python Implementation of a Basic Directed Graph.
    """
    class Vertex:
        """A basic Vertex or graph node that can store a color, and has an adjacency list.
        """
        def __init__(self, key, color=None):
            """Returns a newly created `Vertex` object.
            :param key: The unique value by which to retrieve the desired value.
            :param color: The optional color of the vertex.
            """
            self.key = key
            self.color = color
            self.adj = []

        def edge_list(self):
            """Prints basic list of edges."""
            return_str = ""
            for edge in self.adj:
                return_str += f"{edge}\n"

            return return_str

        def get_edges(self):
            """ Returns a list of out edges from the existing vertex."""
            return self.adj

        def out_degree(self):
            """Returns the Out Degree of the Vertex"""
            return len(self.adj)

        def add_edge(self, edge):
            self.adj.append(edge)

        def __str__(self):
            """Returns a string representation of a node, including the ids and colors of its left and right links.
            The pattern used is: `(left.key)<-[Red|Black]--(node.key)--[Red|Black]->(right.key)
            If either left or right nodes are blank, the key is `None` and the link color defaults to `Black`.

            :return: String representation of the desired node.
            """
            color_str = "" if self.color is None else f":{self.color}"
            return f"({self.key}{color_str})"

    class Edge:
        """Simple Edge class that stores a source and target and a weight."""

        def __init__(self, source, target, weight=None):
            self.source = source
            self.target = target
            self.weight = weight

        def __str__(self):
            weight_str = "" if self.weight is None else f"[{self.weight}]"
            return f"{self.source}-{weight_str}->{self.target}"

    def __init__(self):
        """Creates an empty graph with no Vertices and no Edges."""
        self.V = 0
        self.E = 0
        self.vertices = {}

    def __str__(self):
        """Prints basic information about the graph."""
        return f"Vertices:{self.V}, Edges:{self.E}, Degree:{self.degree()}"

    def degree(self):
        """Returns the total degree from all nodes in graph G"""
        return sum([self.vertices[x].out_degree() for x in self.vertices.keys()])

    def add_vertex(self, key, color=None):
        """ Adds new vertex of optional color to the Graph. Throws a Key error if he vertex key is already used."""
        if key in self.vertices.keys():
            raise KeyError(f"Key: {key} already exists in the graph.  Trying to update?  Use update_vertex instead.")
        else:
            self.vertices[key] = Graph.Vertex(key, color)
            self.V += 1
            return self.vertices[key]

    def add_edge(self, source, target, weight=None, bi=False):
        """ Add a new edge to the Graph.  If ether the source or target vertex is not yet in the Graph it will be
        automatically added without a color.
        :param source: The key of the vertex to be used as the "from" vertex.
        :param target: The key of the vertex to be used as the "to" vertex.
        :param weight: The optional weight of the edge.
        :param bi: Boolean indicating whether or not to create a bi-directional edge.  This is implemented as creating
        a second edge to the graph from the target to the source.
        :return: None
        """

        if source not in self.vertices.keys():
            v_src = self.add_vertex(source)
        else:
            v_src = self.vertices[source]
        if target not in self.vertices.keys():
            v_tar = self.add_vertex(target)
        else:
            v_tar = self.vertices[target]

        new_edge = Graph.Edge(v_src, v_tar, weight)
        self.vertices[source].add_edge(new_edge)
        self.E += 1

        if bi:
            back_edge = Graph.Edge(v_tar, v_src, weight)
            self.vertices[target].add_edge(back_edge)
            self.E += 1

    def depth_first_search(self, start):
        if start not in self.vertices.keys():
            raise KeyError(f"Key: {start} does not exist in the graph.")

        stack = [self.vertices[start]]
        visited = []
        while stack:
            curr = stack.pop()
            if curr in visited:  # SKIP NODES WE'VE ALREADY SEEN
                continue
            visited.append(curr)
            for edge in curr.get_edges():
                if edge.target not in visited:
                    stack.append(edge.target)

            yield curr

    def is_acyclic(self):
        """Performs a complete search of the graph, halting when a cycle is found or when all vertices in
         the graph have been traversed.
         :returns: True if no cycle is detected, false otherwise. An empty graph will return True"""

        if not self.vertices:
            return True

        # VERTICES TO TRAVERSE FROM
        white_vertices = list(self.vertices.keys())

        # VERTICES THAT HAVE ALL BEEN VISITED
        black_vertices = []

        # VERTICES THAT ARE ON THE CURRENT TRAVERSAL PATH
        grey_vertices = []
        while white_vertices:
            start = white_vertices.pop()
            stack = [self.vertices[start]]
            while stack:
                curr = stack.pop()

                if curr.key in white_vertices:
                    white_vertices.remove(curr.key)

                grey_vertices.append(curr.key)

                # HOW MANY NEIGHBORS TO TRAVERSE
                trav_neighbors = []
                for edge in curr.get_edges():
                    if edge.target.key in grey_vertices: # we found a cycle!
                        return False
                    elif edge.target.key in white_vertices:
                        trav_neighbors.append(edge.target)

                if len(trav_neighbors) > 0:
                    stack.append(curr)
                    for n in trav_neighbors:
                        stack.append(n)
                else:
                    grey_vertices.remove(curr.key)
                    black_vertices.append(curr.key)

        # We have traversed the entire tree without a cycle.
        return True



if __name__ == "__main__":
    g = Graph()
    g.add_edge('a','b')
    g.add_edge('a','c')
    g.add_edge('b','d')
    g.add_edge('b','c')
    g.add_edge('d','c')
    g.add_edge('c','b')
    g.add_edge('b','a')

    for v in g.depth_first_search('a'):
        print(v)

    cycle = Graph()
    cycle.add_edge('a','b')
    cycle.add_edge('a','c')
    cycle.add_edge('c','d')
    cycle.add_edge('e','f')
    cycle.add_edge('f','g')

    print("Should be acyclic")
    print(cycle.is_acyclic())

    cycle.add_edge('g','e')
    print("Should no longer be acyclic")
    print(cycle.is_acyclic())

    g2 = Graph()

    g2.add_edge('a', 'b')
    g2.add_edge('b', 'c')
    g2.add_edge('c', 'd')
    g2.add_edge('b', 'd')
    g2.add_edge('d', 'e')
    g2.add_edge('e', 'g')

    g2.is_acyclic()

    g3 = Graph()
    g3.add_edge('a','a')
    print(f"Self loop graph is_acyclic?:{g3.is_acyclic()}")

