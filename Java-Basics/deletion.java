import java.util.Scanner;
class deletion {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the number of elements in the array:");
        int n = sc.nextInt();

        int arr[] = new int[n];
        System.out.println("Enter the elements of the array:"); 
        for(int i = 0; i < n ; i++){
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("Enter the element to be deleted:");
        int del = sc.nextInt();
        boolean found = false;
        for(int i = 0; i<n ; i++){
            if (arr[i] == del){
                for(int j = i; j < n - 1; j++){
                    arr[j] = arr[j + 1];
                }
                n--;
                found = true;
                break;
            }
        }
        if (found) {
            System.out.println("Elements after deletion:");
            for ( int i =0; i<n; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
        else {
            System.out.println("Element not found in the array.");
        }
    }

}