import java.util.Iterator;
import java.util.NoSuchElementException;

public class SimpleList<T> implements ISimpleListIterable<T> {
    private Node<T> head;
    private int size;

    private static class Node<T> {
        T data;
        Node<T> next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    public SimpleList() {
        this.head = null;
        this.size = 0;
    }

    @Override
    public void add(T element) {
        Node<T> newNode = new Node<>(element);
        if (head == null) {
            head = newNode;
        } else {
            Node<T> current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        size++;
    }

    @Override
    public Iterator<T> iterator() {
        return new SimpleListIterator();
    }

    @Override
    public Iterator<T> skippingIterator(int n) {
        return new SimpleListSkippingIterator(n);
    }

    private class SimpleListIterator implements Iterator<T> {
        private Node<T> current = head;

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            T data = current.data;
            current = current.next;
            return data;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("Remove is not supported.");
        }
    }

    private class SimpleListSkippingIterator implements Iterator<T> {
        private Node<T> current = head;
        private final int step;
        private int index = 0;

        SimpleListSkippingIterator(int step) {
            if (step <= 0) {
                throw new IllegalArgumentException("Step must be greater than 0.");
            }
            this.step = step;
        }

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            T data = current.data;
            for (int i = 0; i < step && current != null; i++) {
                current = current.next;
            }
            return data;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("Remove is not supported.");
        }
    }
}