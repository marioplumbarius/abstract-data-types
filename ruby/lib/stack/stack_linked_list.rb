class StackLinkedList

  attr_accessor :head, :length

  def initialize
    @head = nil
    @length = 0
  end

  def empty?
    @length == 0
  end

  def push(cargo)
    node = Node.new(cargo)

    node.nextt = @head unless empty?

    @head = node
    @length+=1
  end

  def pop
    raise RangeError, 'the stack is empty!' if empty?
    removed_node = @head
    @head = @head.nextt
    @length-=1
    removed_node
  end
end
