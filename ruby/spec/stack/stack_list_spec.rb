require 'spec_helper'
require 'stack/stack_list'
require 'stack/stack_interface'

describe StackList do

  subject(:stack) { StackList.new }
  let(:item) { 22 }

  it 'inherits from StackInterface' do
    expect(stack).to be_a StackInterface
  end

  describe '#initialize' do

    it 'creates an empty stack list' do
      expect(stack.list).to eq []
    end

  end

  describe '#push' do
    it 'add an item to the top of the stack' do
      stack.push(item)
      expect(stack).not_to be_empty
    end

    it 'uses Array#push to acomplish the action' do
      expect(stack.list).to receive(:push).with(item)
      stack.push(item)
    end

    it 'does not add nil items' do
      stack.push(nil)
      expect(stack).to be_empty
    end
  end

  describe '#pop' do
    let(:first_item) { 1 }
    let(:last_item) { 3 }

    it 'removes and returns the last item from the stack' do
      stack.push(first_item)
      stack.push(last_item)
      expect(stack.pop).to be last_item
      expect(stack.list.length).to eq 1
    end

    it 'uses the Array#pop to acomplish the action' do
      expect(stack.list).to receive(:pop)
      stack.pop
    end
  end

  describe '#empty?' do

    context 'when the stack is empty' do
      it 'returns true' do
        expect(stack.empty?).to be_truthy
      end
    end

    context 'when the stack is not empty' do
      before do
        stack.push(item)
      end

      it 'returns false' do
        expect(stack.empty?).to be_falsy
      end
    end

  end
end
