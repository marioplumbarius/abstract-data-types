require "spec_helper"
require "queues/queue_list"
require "queues/queue_interface"

describe QueueList do
    subject(:queue) { described_class.new }

    it "inherits from QueueInterface class" do
        expect(queue).to be_a QueueInterface
    end

    describe "#initialize" do

        it "initializes an empty queue" do
            expect(queue.list).to be_empty
        end

    end

    describe "#empty?" do

        context "when the queue is empty" do
            it "returns true" do
                expect(queue.empty?).to be_truthy
            end
        end

        context "when the queue is not empty" do
            before do
                queue.insert(22)
            end

            it "returns false" do
                expect(queue.empty?).to be_falsy
            end
        end

    end

    describe "#insert" do
        let(:cargo) { 22 }
        let(:stubbed_node) { Node.new(0) }

        before do
            allow(Node).to receive(:new).and_return(stubbed_node)
        end

        after do
            queue.insert(cargo)
        end

        it "creates a new node from the cargo" do
            expect(Node).to receive(:new).with(cargo)
        end

        it "adds the node to the queue" do
            expect(queue.list).to receive(:push).with(stubbed_node)
        end
    end

    describe "#remove" do
        before { queue.insert(44) }
        after { queue.remove }

        it "removes the top node from the queue" do
            expect(queue.list).to receive(:shift)
        end
    end
end