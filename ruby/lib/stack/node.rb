class Node
  include Comparable

  attr_accessor :cargo, :nextt

  def initialize(cargo, nextt=nil)
    @cargo = cargo
    @nextt = nextt
  end

  def to_s
    "cargo: #@cargo"
  end

  def <=>(another)
    @cargo <=> another.cargo
  end
  
end