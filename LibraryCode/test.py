from weightedGraph import WeightedGraph 
wg = WeightedGraph()
wg.create_graph_with_rotation('CCCC', 'Clockwise')
wg.draw_graph()
print(wg.detect_rotation_direction())
print(wg.get_graph_string())
print(wg.calculate_rotation_value())
print(wg.find_kitty_corners_first())

wg = WeightedGraph()
wg.add_vertex('A', 'R')
wg.add_vertex('B', 'R')
wg.add_vertex('C', 'R')
wg.add_vertex('D', 'R')
wg.add_edge('A', 'B', 1, 'E')
wg.add_edge('B', 'C', 1, 'N')
wg.add_edge('C', 'D', 1, 'W')
wg.add_edge('D', 'A', 1, 'S')
wg.draw_graph()
print(wg.detect_rotation_direction())
print(wg.find_kitty_corners_first())

tg = WeightedGraph()
tg.create_graph_with_rotation('RCCRCCRCCRCC', 'AntiClockwise')
tg.draw_graph()
print(tg.detect_rotation_direction())
print(tg.get_graph_string())
print(tg.calculate_rotation_value())
print(tg.find_kitty_corners_first())

wg = WeightedGraph()
wg.add_vertex('A', 'R')
wg.add_vertex('B', 'R')
wg.add_vertex('C', 'R')
wg.add_vertex('D', 'R')
wg.add_edge('A', 'B', 1, 'E')
wg.add_edge('B', 'C', 2, 'N')
wg.add_edge('C', 'D', 1, 'W')
wg.add_edge('D', 'A', 1, 'S')
wg.draw_graph()
