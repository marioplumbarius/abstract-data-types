require 'node'

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

    node.next = @head unless empty?

    @head = node
    @length+=1
  end

  def pop
    raise IndexError, 'the stack is empty!' if empty?
    removed_node = @head
    @head = @head.next
    @length-=1
    removed_node
  end
end