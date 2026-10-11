import java.util.Scanner;
class sorted {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int temp;
        System.out.println("Enter the number of elements in the array:");
        int n = sc.nextInt();

        int arr[] = new int[n];
        System.out.println("Enter the elements of the array:"); 
        for(int i = 0; i < n ; i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Elements before Sorted");
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i] + " ");
        }
        for(int i = 0;i<n;i++){
            for(int j = i+1;j<n;j++){
                if(arr[i]>arr[j]){
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
                else{
                    System.out.println("Array is already sorted");
                    break;
                }
            }
        }
        System.out.println("Elements after Sorted");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}