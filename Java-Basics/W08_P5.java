public class W08_P5 {

    // Shared class with a number
    static class Counter {
        int count = 0;

        // Synchronized method to safely increase number
        public synchronized void increment() {
            count++;
        }
    }

    // Thread class to run increment
    static class MyThread extends Thread {
        Counter c;

        MyThread(Counter c) {
            this.c = c;
        }

        @Override
        public void run() {
            // Call increment() 1000 times using loop
            for (int i = 0; i < 1000; i++) {
                c.increment();
            }
        }
    }

    public static void main(String[] args) {

        Counter c = new Counter();

        // Create two threads
        MyThread t1 = new MyThread(c);
        MyThread t2 = new MyThread(c);

        // Start both threads
        t1.start();
        t2.start();

        try {
            // Wait for both threads to finish
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("The main thread was interrupted.");
        }

        // Print final count
        System.out.println("Final count is: " + c.count);
        System.out.println("This is the final output.");
    }
}
