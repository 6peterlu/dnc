import json

# AST node representation

class ASTNode:
	def __init__(self, type_str):
		self.children = []
		self.value = None
		self.type = type_str

INPUT_FILE = "test.txt"

def parse_AST_from_text_JSON(JSON_str):
	json_node_list = json.loads(JSON_str)
	node_count = len(json_node_list)
	ast_node_list = []

	for node_json in json_node_list:
		ast_node_list.append(ASTNode(node_json['type']))

	for i in range(node_count):
		cur_ast_node = ast_node_list[i]
		cur_node_json = json_node_list[i]
		if "children" in cur_node_json:
			for idx in cur_node_json["children"]:
				cur_ast_node.children.append(ast_node_list[idx])
		if "value" in cur_node_json:
			cur_ast_node.value = cur_node_json["value"]
	for ast_node in ast_node_list:
		print(vars(ast_node))

with open(INPUT_FILE, 'r') as input_file:
	input_text = input_file.read()
	parse_AST_from_text_JSON(input_text)





SAMPLE_JSON = '''[{"type":"Module", "children":[1,4]},
    {"type":"Assign", "children":[2,3]},
      {"type":"NameStore", "value":"x"},
      {"type":"Num", "value":"7"},
    {"type":"Print", "children":[5]},
      {"type":"BinOpAdd", "children":[6,7]},
        {"type":"NameLoad", "value":"x"},
        {"type": "Num", "value":"1"}]'''






# printing tree

# root = ast_node_list[0]

# # BFS

# node_array = [root]

# while node_array:


# print(vars(ast_node_list[0]))

