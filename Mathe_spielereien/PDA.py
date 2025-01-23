from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Define nodes (states)
dot.node('q0', 'q0 (start)')
dot.node('q1', 'q1 (reading a\'s)')
dot.node('q2', 'q2 (reading b\'s)')
dot.node('q3', 'q3 (reading c\'s)')
dot.node('q4', 'q4 (accept)', shape='doublecircle')
dot.node('q5', 'q5 (reject)')

# Define edges (transitions)
dot.edge('q0', 'q1', label='ε, Z → Z')
dot.edge('q1', 'q1', label='a, Z → AZ\na, A → AA')
dot.edge('q1', 'q2', label='b, A → ε')
dot.edge('q2', 'q2', label='b, A → ε')
dot.edge('q2', 'q3', label='ε, Z → Z')
dot.edge('q3', 'q3', label='c, A → ε')
dot.edge('q3', 'q4', label='ε, Z → Z')
dot.edge('q3', 'q5', label='c, Z → Z')

# Render the graph to a file
dot.render('pda', format='png', cleanup=True)

# Display the graph
dot.view()