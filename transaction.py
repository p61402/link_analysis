import numpy as np

def preprocess(file_path, bidirect=False):
    with open(file_path, "r") as f:
        lines = f.read().splitlines()
        nodes = set()
        for line in lines:
            a, b, c = line.split()
            if c != '0':
                nodes.add(b)
                nodes.add(c)
        
        adj_matrix = np.zeros(shape=(len(nodes), len(nodes)))
    
        if bidirect:
            for line in lines:
                a, b, c = line.split()
                if c != '0':
                    adj_matrix[int(b) - 1, int(c) - 1] = 1
                    adj_matrix[int(c) - 1, int(b) - 1] = 1
        else:
            for line in lines:
                a, b, c = line.split()
                if c != '0':
                    adj_matrix[int(b) - 1, int(c) - 1] = 1

        return adj_matrix
