from .apple import _TypeNum

class matrix:
  newvalues = []
  def __init__(self, _matrix: tuple, positional: int=0) -> None:
    self._matrix = _matrix
    self.positional = positional -1
    
  def create(rows: int, columns: int) -> tuple:
    _values = [0]*rows
    for i in range(columns):
      _values[i] = [0]*columns
    return _values
  
  def create_multiple(rows: int, columns: int, names: str) -> tuple:
    _values, n = [0]*rows, 0
    list_ = []
    def make_matrix():
      for i in range(columns):
        _values[i] = [0]*columns
      return _values
    names: tuple = names.replace(' ', '').split(';')
    result = [make_matrix() for i in range(len(names))]
    return result
  
  def iterate(self, y_matrix: tuple, z_matrix: tuple|None = None, rtype: str = 'add') -> tuple:
    for i in range(len(self._matrix)):
      for j in range(len(self._matrix[self.positional])):
        matrix_x = self._matrix[i][j]; matrix_y = y_matrix[i][j]
        match rtype:
          case 'mult':
            z_matrix[i][j] = matrix_x * matrix_y
          case 'add':
            z_matrix[i][j] = matrix_x + matrix_y
          case 'sub':
            z_matrix[i][j] = matrix_x - matrix_y
          case 'div':
            z_matrix[i][j] = matrix_x / matrix_y
          case 'pow':
            z_matrix[i][j] = matrix_x ** matrix_y
    return z_matrix
  
  def get(self, rtype: str) -> tuple:
    ArrayColumn = [x for x in self._matrix[self.positional]]
    match rtype:
      case "column":
        return ArrayColumn
      case "row":
        for value in self._matrix:
          self.newvalues.append(value[self.positional])
        return self.newvalues
      case "matrix":
        return self._matrix
  
  def overwrite(self, value: any) -> tuple:
    if len(value) > len(self._matrix[self.positional]):
      value = value[:len(self._matrix[self.positional])]
    self._matrix[self.positional] = value
    return self._matrix
  
  def create_column(self) -> tuple:
    self._matrix.append([0]*len(self._matrix))
    return self._matrix

class locate_matrix:
  import json
  def __init__(self, _matrix: tuple, namefile: str) -> None:
    self._matrix = _matrix
    self.namefile = namefile
  
  def injson(self, section, position: int, section_value: str) -> any:
    position = position-1
    if not self.namefile.endswith('.json'):
      raise ValueError("File must end with \".json\"!")
    with open(file=self.namefile, mode='r+') as file_:
      data = self.json.load(file_)
      data[section][position][section_value] = self._matrix
      file_.seek(0)
      self.json.dump(data, file_)
      file_.truncate()
  
  def intxt(self) -> any:
    if not self.namefile.endswith(".txt"):
      raise ValueError("File must end with \".txt\"!")
      return None
    value = f"{self._matrix}\n\t"
    with open(self.namefile, mode="w") as file_dottxt:
      file_dottxt.write(("matrix: "+f"{value}\n"))
      return file_dottxt

class matharray:
  def __init__(self, values: tuple[_TypeNum]) -> None:
    self.values = values
  
  def sum(self, number: _TypeNum) -> _TypeNum:
    result = [x + number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result
  
  def multiply(self, number: _TypeNum) -> _TypeNum:
    result = [x * number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result
  
  def divide(self, number: _TypeNum) -> _TypeNum:
    result = [x/number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result
  
  def subtract(self, number: _TypeNum) -> _TypeNum:
    result = [x - number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result
  
  def maxSum(self) -> _TypeNum:
    """
    Sum values by itself
    ## Example
    >>> matharray([1, 2, 3, 4, 5]).maxSum()
    >>> 9 # (1 + 2) -> (2 + 3) -> (3 + 4) -> (4 + 5)
    """
    lenght, maxSum = len(self.values)-1, float("-Infinity")
    for i in range(0, lenght):
      sum_ = self.values[i] + self.values[i+1]
      if sum_ > maxSum:
        maxSum = sum_
    if len(self.values) > 1:
      return maxSum
    elif len(self.values) == 1:
      return self.values[0]
    else:
      return f"{self.values} must be greater or equal than 1 element"

  def __str__(self) -> str:
    return self.values


class Array:
  
  empty_arr = []
  
  def __init__(self, array, position: int|None = None):
    self.tup = array; self.position = position -1
    
  def createArrayInside(self) -> tuple[tuple]:
    n = 0
    values = [x for x in self.tup]
    newArrayInside = self.empty_arr.insert(1, values)
    self.tup.insert(1, newArrayInside)
    for i in range (len(self.tup)-1):
      n = n * i
      self.tup[self.position].insert(1, n)
    self.tup[self.position].insert(1, newArrayInside)
    return self.tup
  
  def intersect(self, array_b: tuple) -> tuple:
    intersection = []
    for items_array_x in self.tup:
      for items_array_y in array_b:
        if not items_array_x in intersection and items_array_x == items_array_y:
          intersection.append(items_array_x)
    return intersection
  
  def union(self, array_b: tuple) -> tuple:
    for items_array_b in array_b:
      self.tup.append(items_array_b)
    return self.tup
  
  def bignotation(self, notation_type, value: _TypeNum):
    def log_notation(vector: tuple, value) -> int:
      left, right, middle = 0, len(self.tup), ...
      result = None
      for i in range(left, right):
        middle = ((left+right)//2)
        if vector[middle] == value:
          (result:= middle)
        elif vector[middle] > value:
          (result:= middle-1)
        elif vector[middle] < value:
          (result:= middle+1)
      
      if vector[result] < value:
        result = result+1
      elif not vector[result] == value:
        result = result-1
      return result
    
    def quadratic_notation(vector: tuple):
      return [element for element in vector for _ in range(2)]
    
    match notation_type:
      case 'O(log n)':
        return log_notation(self.tup, value)
      case 'O(1)':
        return self.tup[self.position]
      case 'O(n^2)':
        return quadratic_notation(self.tup)
  
  def Reverse(self) -> tuple:
    n,length = 0, len(self.tup)
    for range_search in range(length):
      n = n + 1
      reversing = self.tup[-n]
      self.empty_arr.append(reversing)
    return self.empty_arr
