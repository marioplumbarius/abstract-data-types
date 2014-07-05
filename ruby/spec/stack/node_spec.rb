require 'spec_helper'
require 'stack/node'

describe Node do
  it 'includes Comparable module' do
    expect(described_class).to include(Comparable)
  end


  describe '#new' do
    subject { Node.new cargo, nextt }
    let(:cargo) { 1 }
    let(:nextt) { Node.new(cargo*2) }

    it 'assigns @cargo' do
      expect(subject.cargo).to eq(cargo)
    end

    it 'assigns @nextt' do
      expect(subject.nextt).to eq(nextt)
      expect(subject.nextt).to be_a Node
    end

    context 'on attempt to assign a cargo of type other than an integer' do
      it 'raises ArgumentError' do
        expect{
          Node.new(nil)
        }.to raise_error(ArgumentError)
      end
    end

  end

  describe '#to_s' do
    subject { Node.new cargo }
    let(:cargo) { 22 }

    it 'prints its @cargo value' do
      expect(subject.to_s).to match(/cargo: #{cargo}/)
    end
  end

  describe '#<=>' do
    let(:node_greater) { Node.new cargo_greater }
    let(:node_lesser) { Node.new cargo_lesser }
    let(:cargo_greater) { 100 }
    let(:cargo_lesser) { 50 }

    it 'implements the comparisson using the @cargo attribute' do
      expect(node_greater > node_lesser).to eq(cargo_greater > cargo_lesser)
    end
  end

end