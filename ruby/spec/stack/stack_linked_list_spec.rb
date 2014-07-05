require 'spec_helper'
require 'stack/node'
require 'stack/stack_linked_list'

describe StackLinkedList do
  subject(:stack) { StackLinkedList.new }

  describe '#new' do
    it 'creates an empty stack' do
      expect(stack.head).to be_nil
      expect(stack.length).to be_zero
    end
  end

  describe '#push' do
    it 'add a new node at the top of the stack' do
      stack.push(11)
      stack.push(22)
      stack.push(33)
      expect(stack.head).to eq(Node.new(33))
      expect(stack.head).to be_a(Node)
    end

    it 'increments the length of the stack' do
      stack.push(99)
      stack.push(77)
      expect(stack.length).to eq(2)
    end

    context 'when the stack is empty' do
      it 'does not link the new node to the current @head node' do
        stack.push(33)
        expect(stack.head.nextt).to be_nil
      end
    end

    context 'when the stack is not empty' do
      it 'links the new node with the current @head node' do
        stack.push(22)
        stack.push(55)
        expect(stack.head.nextt).to eq(Node.new(22))
      end
    end
  end

  describe '#pop' do
    context 'when the stack is empty' do
      it 'raises RangeError' do
        expect{
          stack.pop
        }.to raise_error(RangeError)
      end
    end

    context 'when the stack is not empty' do
      it 'return and remove the top node from the stack' do
        stack.push(22)
        stack.push(11)
        stack.push(33)
        expect(stack.pop).to eq(Node.new(33))
      end

      it 'assigns the nextt node as the top of the stack' do
        stack.push(22)
        stack.push(55)
        stack.pop
        expect(stack.head).to eq(Node.new(22))
      end

      it 'decrements the length of the stack' do
        stack.push(22)
        stack.push(88)
        stack.pop
        expect(stack.length).to eq(1)
      end
    end
  end

  describe '#empty?' do
    context 'when the stack is empty' do
      it 'returns true' do
        expect(stack.empty?).to be_truthy
      end
    end

    context 'when the stack is not empty' do
      it 'returns false' do
        stack.push(66)
        expect(stack.empty?).to be_falsy
      end
    end
  end
end
