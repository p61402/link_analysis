import numpy as np

class Graph():
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.node_count = self.adj_matrix.shape[0]

    def hits(self, num_iterations=100, tol=1e-06):
        A = self.adj_matrix
        At = A.T
        auth = np.ones(self.node_count)
        hub = np.ones(self.node_count)
        tol_matrix = tol * np.ones_like(auth)
        for step in range(num_iterations):
            hub_prev, auth_prev = hub.copy(), auth.copy()
            hub = np.dot(A, auth)
            hub /= hub.sum()
            auth = np.dot(At, hub)
            auth /= auth.sum()
            if (np.abs(hub_prev - hub) < tol_matrix).all() and (np.abs(auth_prev - auth) < tol_matrix).all():
                break
        return auth, hub

    def pagerank(self, d=0.85, num_iteration=100, tol=1e-06):
        v = self.adj_matrix.sum(axis=1)[:,np.newaxis]
        M = np.divide(self.adj_matrix, v, out=np.zeros_like(self.adj_matrix), where=v!=0)
        M = M.T
        X = X_0 = np.ones(self.node_count) / self.node_count
        tol_matrix = tol * np.ones_like(X)
    
        for step in range(num_iteration):
            X_prev = X.copy()
            X = d * np.dot(M, X) + (1 - d) * X_0
            if (np.abs(X_prev - X) < tol_matrix).all():
                break
        
        return X

    def simrank(self, c=0.85, num_iteration=100):
        C = self.adj_matrix.sum(axis=0)
        l = np.dot(C[:,np.newaxis], C[np.newaxis,:])
        C = np.divide(c, l, out=np.zeros_like(l), where=l!=0)
        np.fill_diagonal(C, 1)
        
        S = np.identity(self.node_count)
        for step in range(num_iteration):
            temp_S = np.ones_like(S)
            for i in range(self.node_count):
                for j in range(self.node_count):
                    if i != j:
                        a = self.adj_matrix[:,i]
                        b = self.adj_matrix[:,j]
                        temp_S[i,j] = (np.dot(a[:,np.newaxis], b[np.newaxis,:]) * S).sum()
            S = C * temp_S
        
        return S
