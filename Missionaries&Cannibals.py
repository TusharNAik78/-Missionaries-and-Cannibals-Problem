
class State():
	def __init__(self, cl, ml, boat, cr, mr):
		self.cl = cl
		self.ml = ml
		self.boat = boat
		self.cr = cr
		self.mr = mr
		self.parent = None

	def is_goal(self):
		if self.cl == 0 and self.ml == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.ml >= 0 and self.mr >= 0 \
                   and self.cl >= 0 and self.cr >= 0 \
                   and (self.ml == 0 or self.ml >= self.cl) \
                   and (self.mr == 0 or self.mr >= self.cr):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.cl == other.cl and self.ml == other.ml \
                   and self.boat == other.boat and self.cr == other.cr \
                   and self.mr == other.mr

	def __hash__(self):
		return hash((self.cl, self.ml, self.boat, self.cr, self.mr))

def successors(cur_state):
	children = [];
	if cur_state.boat == 'left':
		new_state = State(cur_state.cl, cur_state.ml - 2, "==>>",cur_state.cr, cur_state.mr + 2)
		## Two missionaries cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl - 2, cur_state.ml, "==>>",cur_state.cr + 2, cur_state.mr)
		## Two cannibals cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl - 1, cur_state.ml - 1, "==>>",cur_state.cr + 1, cur_state.mr + 1)
		## One missionary and one cannibal cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl, cur_state.ml - 1, "==>>",cur_state.cr, cur_state.mr + 1)
		## One missionary crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl - 1, cur_state.ml, "==>>",cur_state.cr + 1, cur_state.mr)
		## One cannibal crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cl, cur_state.ml + 2, "<<==",cur_state.cr, cur_state.mr - 2)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl + 2, cur_state.ml, "<<==",cur_state.cr - 2, cur_state.mr)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl + 1, cur_state.ml + 1, 'left',cur_state.cr - 1, cur_state.mr - 1)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl, cur_state.ml + 1, "<<==",cur_state.cr, cur_state.mr - 1)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cl + 1, cur_state.ml, "left",cur_state.cr - 1, cur_state.mr)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print(" [ " + str(state.cl) +"C"+ "," + str(state.ml) \
                              + "M"+"------------" + state.boat + "------------" + str(state.cr)+"C" + "," + \
                              str(state.mr)+"M" + " ] ")


def main():
	solution = breadth_first_search()
	print("  Missionaries and Cannibals solution:\n")
	print(" [ C ,M ------------Boat------------C ,M ]")
	print_solution(solution)



# if called from the command line, call main()
if __name__ == "__main__":
    main()

print("\n\tThank you  ;)")