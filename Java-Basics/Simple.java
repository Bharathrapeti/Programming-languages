import java.util.Scanner;
class Simple { 
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("-----Driver Details-----");
        System.out.print("Enter the number of drivers: ");
        int n = sc.nextInt();
        sc.nextLine();
        String[] driverNames = new String[n];
        int[] driverAges = new int[n];
        String[] driverPhoneNumbers = new String[n];

        for(int i = 0; i < n; i++){
            System.out.println("\nEnter details for driver " + (i + 1) + ":");
            System.out.print("Name: ");
            driverNames[i] = sc.nextLine();
            System.out.print("Age: ");
            driverAges[i] = sc.nextInt();
            sc.nextLine();
            System.out.print("Phone number: ");
            driverPhoneNumbers[i] = sc.nextLine();
        }

        System.out.println("Driver categories:");
        for(int i = 0; i < n; i++){
            String category;
            if(driverAges[i] >= 30){
                category = "Professional Driver";
            } else if(driverAges[i] >= 15){
                category = "Amateur Driver";
            }
            else{
                category = "Beginner Driver";
            }

            System.out.println("Name: " + driverNames[i]
                    + ", Age: " + driverAges[i]
                    + ", Phone: " + driverPhoneNumbers[i]
                    + ", Category: " + category);
        }
    }
}
