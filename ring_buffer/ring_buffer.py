class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item): # Method that adds a single item to the existing list (remove oldest and insert newest)
    self.storage[self.current] = item # The oldest item in the ring buffer is overwritten with the newest item
    if self.current < self.capacity - 1:
      self.current += 1
    else:
      self.current = 0

  def get(self): # Method that returns the value for the specified key if key is in dictionary
    new_array = [] # Returns elements in the buffer in an array
    for item in self.storage:
      if item is not None: # It should not return any `None` values in the list
        new_array.append(item) # Method that adds a single item to the existing list
    return new_array # Returns new array