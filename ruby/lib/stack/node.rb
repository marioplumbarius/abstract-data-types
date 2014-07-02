class Node
  include Comparable

  attr_accessor :cargo, :next

  def initialize(cargo=nil, nextt=nil)
    @cargo = cargo
    @next = nextt
  end

  def to_s
    "cargo: #@cargo"
  end

  def <=>(another)
    @cargo <=> another.cargo
  end
  
end