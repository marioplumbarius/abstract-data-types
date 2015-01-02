require_relative "./stack_interface"

class StackList < StackInterface
  attr :list

  def initialize
    @list = []
  end

  def push(item)
    @list.push(item) if item
  end

  def pop
    @list.pop()
  end

  def empty?
    @list.empty?
  end
end