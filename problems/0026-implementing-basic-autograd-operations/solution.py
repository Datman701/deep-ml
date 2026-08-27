def build_graph(x,visited,order):
	if(x == None):
		return 
	if(x in visited):
		return
	visited.add(x)

	for i in x._prev:
		build_graph(i , visited , order)
	order.append(x)





class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op
	def __repr__(self):
		def fmt(x):
			return int(x) if float(x).is_integer() else round(x, 4)
		return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"
			

	def __add__(self, other):

		if not (isinstance(other, Value)):
			other = Value(other)
		
		out = Value(self.data + other.data,(self , other) , '+')

		def backward():
			self.grad = self.grad + out.grad
			other.grad = other.grad + out.grad

		out._backward = backward

		 # Implement addition here
		return out


	def __mul__(self, other):
		if not (isinstance(other, Value)):
			other = Value(other)
		out = Value(self.data * other.data,(self , other) , '*')

		def backward():
			self.grad  = self.grad + out.grad * other.data
			other.grad = other.grad + out.grad * self.data

		out._backward = backward

		return out

	def relu(self):
		val = 0
		if(self.data > 0):
			val = self.data

		out  = Value(val,(self,), 'relu')

		def backward():
			if(out.data > 0):
				self.grad = self.grad + out.grad
		out._backward = backward

		# Implement ReLU here
		return out


	def backward(self):
		# Implement backward pass here

		self.grad = 1
		visited = set()
		order = []
		build_graph(self , visited , order)

		for i in order[::-1]:
			i._backward()
		



		pass