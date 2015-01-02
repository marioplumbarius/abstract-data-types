require_relative '../list/node'
require_relative './queue_interface'

class QueueList < QueueInterface

    attr_accessor :list

    def initialize
        @list = []
    end

    def empty?
        @list.empty?
    end

    def insert(cargo)
        node = Node.new(cargo)
        @list.push(node)
    end

    def remove
        @list.shift
    end

end