public class Sorter {

    // (a) reverseSelectionSort
    public static <T extends Comparable<T>> void reverseSelectionSort(ISimpleList<T> list) {
        int n = list.size();
        for (int i = 0; i < n - 1; i++) {
            int maxIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (list.get(j).compareTo(list.get(maxIndex)) > 0) {
                    maxIndex = j;
                }
            }
            if (maxIndex != i) {
                list.swap(i, maxIndex);
            }
        }
    }

    // (b) reverseInsertionSort
    public static <T extends Comparable<T>> void reverseInsertionSort(ISimpleList<T> list) {
        int n = list.size();
        for (int i = 1; i < n; i++) {
            T key = list.get(i);
            int j = i - 1;
            while (j >= 0 && list.get(j).compareTo(key) < 0) {
                list.set(j + 1, list.get(j));
                j--;
            }
            list.set(j + 1, key);
        }
    }

    // (c) reverseBubbleSort
    public static <T extends Comparable<T>> void reverseBubbleSort(ISimpleList<T> list) {
        int n = list.size();
        boolean swapped;
        do {
            swapped = false;
            for (int i = 0; i < n - 1; i++) {
                if (list.get(i).compareTo(list.get(i + 1)) < 0) {
                    list.swap(i, i + 1);
                    swapped = true;
                }
            }
            n--; // Reduce the range of comparison
        } while (swapped);
    }
}
