require 'spec_helper'
require 'stack/stack_list'

describe StackList do
  before do
    subject { StackList.new }
  end

  let(:item) { 22 }

  describe '#push' do
    it 'add an item to the top of the stack' do
      subject.push(item)
      expect(subject).not_to be_empty
    end

    it 'uses Array#push to acomplish the action' do
      expect(subject.list).to receive(:push).with(item)
      subject.push(item)
    end

    it 'does not add nil items' do
      subject.push(nil)
      expect(subject).to be_empty
    end
  end

  describe '#pop' do
    let(:first_item) { 1 }
    let(:last_item) { 3 }

    it 'removes and returns the last item from the stack' do
      subject.push(first_item)
      subject.push(last_item)
      expect(subject.pop).to be last_item
      expect(subject.list.length).to eq 1
    end

    it 'uses the Array#pop to acomplish the action' do
      expect(subject.list).to receive(:pop)
      subject.pop
    end
  end

  describe '#empty?' do
    it 'returns true when the stack is empty' do
      expect(subject.empty?).to be_truthy
    end

    it 'returns false when the stack is not empty' do
      subject.push(item)
      expect(subject.empty?).to be_falsy
    end
  end
end
