def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    dict = {}
    for source in graph.nodes():
        if source not in dict:
            queue = deque([source])
            dict[source] = 'good'
            
            while pending:
                u = pending.popleft()
                first = dict[u]
                if first == 'good':
                    second = 'evil'
                else: 
                    second = 'good'
                
                for v in graph.neighbors(u):
                    if v not in dict:
                        dict[v] = second
                        pending.append(v)
                    elif dict[v] == first:
                        return None
                        
    return labels

