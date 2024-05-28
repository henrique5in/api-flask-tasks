class Task:
  def __init__(self, id, name, description, status=False):
    self.id = id
    self.name = name
    self.description = description
    self.status = status

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'status': self.status
    }