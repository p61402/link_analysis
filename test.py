import graph
import numpy as np
from transaction import preprocess

def read_txt(file_path):
    with open(file_path, 'r') as f:
        nodes = set()
        lines = f.read().splitlines()
        for line in lines:
            a, b = line.split(',')
            nodes.add(a)
            nodes.add(b)
        
        adj_matrix = np.zeros(shape=(len(nodes), len(nodes)))
        
        for line in lines:
            a, b = line.split(',')
            adj_matrix[int(a) - 1, int(b) - 1] = 1
    
    return adj_matrix

def main():
    for i in range(5):
        print('Graph no.', i + 1)
        adj_matrix = read_txt('hw3dataset/graph_' + str(i + 1) + '.txt')
        g = graph.Graph(adj_matrix)
        print('- adjacency matrix:\n')
        print(g.adj_matrix)
        h, a = g.hits(num_iterations=100)
        print('- hubs:\n', h)
        print('- authorities:\n', a)
        print('- pagerank:\n', g.pagerank())
        if i < 4:
            print('simrank:', g.simrank(num_iteration=100))
        print('-' * 10)
    
    print("Bidir transaction")
    bidir_graph = preprocess('hw3dataset/transaction_data.txt', bidirect=True)
    g = graph.Graph(bidir_graph)
    h, a = g.hits(num_iterations=100)
    print('-hubs:', h)
    print('-authorities:', a)
    print('-pagerank:', g.pagerank())
    print('-' * 10)

    print("Dir transaction")
    dir_graph = preprocess('hw3dataset/transaction_data.txt', bidirect=False)
    g = graph.Graph(dir_graph)
    h, a = g.hits(num_iterations=100)
    print('-hubs:', h)
    print('-authorities:', a)
    print('-pagerank:', g.pagerank())
    print('-' * 10)


if __name__ == "__main__":
    main()
