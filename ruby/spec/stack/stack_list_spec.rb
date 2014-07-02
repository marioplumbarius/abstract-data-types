require 'spec_helper'
require 'stack/stack_list'

describe StackList do
  before do
    @stack = StackList.new
  end

  describe '#push' do
    it 'add a item to the top of the stack' do
      @stack.push(1)
      expect(@stack).not_to be_empty
    end

    it 'uses Array#push to acomplish the action' do
      item = 3
      expect(@stack.list).to receive(:push).with(item)
      @stack.push(item)
    end

    it 'does not add nil items' do
      @stack.push(nil)
      expect(@stack).to be_empty
    end
  end

  describe '#pop' do
    it 'removes and returns the last item from the stack' do
      first_item = 1
      last_item = 2
      @stack.push(first_item)
      @stack.push(last_item)
      expect(@stack.pop).to be last_item
      expect(@stack.list.length).to eq 1
    end

    it 'uses the Array#pop method to acomplish the action' do
      item = 3
      expect(@stack.list).to receive(:pop).and_return(item)
      @stack.pop
    end
  end

  describe '#empry?' do
    it 'returns true when the stack is empty' do
      expect(@stack.empty?).to be_truthy
    end

    it 'returns false when the stack is not empty' do
      @stack.push(1)
      expect(@stack.empty?).to be_falsy
    end
  end
end
